

student_scores = [52, 28, 95, 74, 64, 57, 66, 88, 92]

maximum_score = student_scores[0]

for student in student_scores:
    if maximum_score < student:
        maximum_score = student
print("The highest score in the class is",maximum_score)