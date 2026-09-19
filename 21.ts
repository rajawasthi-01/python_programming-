import Anthropic from '@anthropic-ai/sdk';
import { NextRequest } from 'next/server';

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

// Enforce Edge or Node runtime
export const runtime = 'nodejs';

const SYSTEM_PROMPT = `You are Pashuraksha AI Copilot — the official intelligent assistant of the Pashuraksha AI platform (Smart India Hackathon SIH26128).

Rules:
- Only answer questions related to livestock health, animal diseases (FMD, Lumpy Skin, Mastitis, Black Quarter, Brucellosis, etc.), and the Pashuraksha AI platform.
- Always reply in the same language the user is using (Marathi or English).
- When the user writes in Marathi or uses Marathi voice, reply in simple, respectful, farmer-friendly Marathi (मराठी).
- Be calm, practical, and accurate. Never prescribe restricted veterinary medicines or give dangerous medical procedures. Always advise calling the 1962 Mobile Veterinary Unit (MVU) or local Pashu Sakhi for critical cases.
- If a question is unrelated to livestock health, animal husbandry, or Pashuraksha AI, politely decline and state that you can only assist with livestock health and the platform.

Platform Knowledge:
- Mission: "From the first symptom to the first outbreak warning"
- 8 Nodes of Pashuraksha AI: Farmer → Report → Risk Engine → Field Visit (Pashu Sakhi) → Vet → Lab → GIS → Authority
- Key Features:
  1. Voice/Text symptom reporting in Marathi & English
  2. Camera-based disease scan (AI visual triage)
  3. Vaccine cold-chain tracking with IoT temperature alerts
  4. 1962 MVU (Mobile Veterinary Unit) ambulance dispatch
  5. Live GIS Outbreak & Disease Surveillance Map
  6. Automatic containment zones (5km alert ring, 10km quarantine ring)
- Active Demo Outbreak Scenario:
  - Disease: Foot & Mouth Disease (FMD / लाळ्या खुरकूत) Hotspot
  - Location: Baramati East, Maharashtra
  - Cluster ID: #RC-2026-014
  - Quarantine: Active 10km containment zone
- Covered Pilot Regions: Pune, Satara, Solapur districts of Maharashtra.`;

export async function POST(req: NextRequest) {
  try {
    const { messages } = await req.json();

    if (!messages || !Array.isArray(messages)) {
      return new Response(JSON.stringify({ error: 'Messages array is required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Stream from Anthropic Claude API
    const stream = await anthropic.messages.stream({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 1024,
      system: SYSTEM_PROMPT,
      messages: messages.map((m: { role: string; content: string }) => ({
        role: m.role as 'user' | 'assistant',
        content: m.content,
      })),
    });

    // Create a plain-text ReadableStream for smooth client streaming
    const responseStream = new ReadableStream({
      async start(controller) {
        const textEncoder = new TextEncoder();
        try {
          for await (const chunk of stream) {
            if (
              chunk.type === 'content_block_delta' &&
              chunk.delta.type === 'text_delta'
            ) {
              controller.enqueue(textEncoder.encode(chunk.delta.text));
            }
          }
          controller.close();
        } catch (err) {
          controller.error(err);
        }
      },
    });

    return new Response(responseStream, {
      headers: {
        'Content-Type': 'text/plain; charset=utf-8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
      },
    });
  } catch (error: any) {
    console.error('Claude API Error:', error);
    return new Response(
      JSON.stringify({ error: error?.message || 'Error processing request' }),
      {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  }
}