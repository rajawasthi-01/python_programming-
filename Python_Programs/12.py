import random


def play_game():
	print("\n=== Number Guessing Game ===")
	print("I am thinking of a number from 1 to 100.")

	secret_number = random.randint(1, 100)
	attempts = 0

	while True:
		try:
			guess = int(input("Enter your guess: "))
		except ValueError:
			print("Please enter a whole number.")
			continue

		if not 1 <= guess <= 100:
			print("Your guess must be between 1 and 100.")
			continue

		attempts += 1

		if guess < secret_number:
			print("Too low. Try again!")
		elif guess > secret_number:
			print("Too high. Try again!")
		else:
			print(f"Correct! You got it in {attempts} attempt(s).")
			break


while True:
	play_game()
	play_again = input("Play again? (y/n): ").strip().lower()
	if play_again != "y":
		print("Thanks for playing!")
		break
