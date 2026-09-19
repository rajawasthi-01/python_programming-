comment = input("Enter a comment: ").lower()

spam_keywords = [
	"make a lot of money",
	"buy now",
	"subscribe this",
	"click this",
]

if any(keyword in comment for keyword in spam_keywords):
	print("This comment is spam.")
else:
	print("This comment is not spam.")
