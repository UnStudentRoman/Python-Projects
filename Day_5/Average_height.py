#Average height

student_heights = [180, 154, 166, 197, 146, 172, 178, 170, 169]
sum_height = 0

for height in student_heights:
    sum_height += height
average_height = sum_height / len(student_heights)

print("The average student height is", round(average_height,2))