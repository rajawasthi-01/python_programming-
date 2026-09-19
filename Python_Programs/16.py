marks = []

for subject_number in range(1, 4):
	mark = float(input(f"Enter marks for subject {subject_number} (out of 100): "))

	if not 0 <= mark <= 100:
		print("Marks must be between 0 and 100.")
		break

	marks.append(mark)
else:
	total_percentage = sum(marks) / 3

	if total_percentage >= 40 and all(mark >= 33 for mark in marks):
		print("The student has passed.")
	else:
		print("The student has failed.")
