marks = float(input("Enter the student's marks: "))

if not 0 <= marks <= 100:
	print("Marks must be between 0 and 100.")
elif marks >= 90:
	print("Grade: Ex")
elif marks >= 80:
	print("Grade: A")
elif marks >= 70:
	print("Grade: B")
elif marks >= 60:
	print("Grade: C")
elif marks >= 50:
	print("Grade: D")
else:
	print("Grade: F")
