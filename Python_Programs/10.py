terms = int(input("Enter the number of terms: "))

first, second = 0, 1

if terms <= 0:
	print("Please enter a positive number of terms")
else:
	for _ in range(terms):
		print(first, end=" ")
		first, second = second, first + second
