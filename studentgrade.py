def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

num_subjects = int(input("Enter number of subjects: "))
marks = []

for i in range(num_subjects):
    mark = int(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

grade = calculate_grade(marks)
print(f"Average mark: {sum(marks) / len(marks)}")
print(f"Grade: {grade}")
