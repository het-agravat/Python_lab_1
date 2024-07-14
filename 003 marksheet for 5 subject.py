# Create a Marksheet for 5 subjects and calculate total, average and grade with if else.

def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

subject_marks = []
for i in range(5):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    subject_marks.append(marks)

total_marks = sum(subject_marks)

average_marks = total_marks / 5

grade = calculate_grade(average_marks)

print("\n-------- Marksheet --------")
for i in range(5):
    print(f"Subject {i+1}: {subject_marks[i]}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")
    print(f"Grade: {grade}")
