print("==== Student Marks Analyzer ====")

marks = []
grades = []
pass_count = 0
fail_count = 0

total_students = int(input("Enter total number of students: "))

# Input marks
for i in range(total_students):
    num = int(input("Enter marks of each student out of 100: "))
    marks.append(num)

# Highest & Lowest
print(f"The highest mark is {max(marks)}")
print(f"The lowest mark is {min(marks)}")

# Grade calculation
for m in marks:
    if m >= 90:
        pass_count += 1
        grades.append('A')
    elif m >= 80:
        pass_count += 1
        grades.append('B')
    elif m >= 70:
        pass_count += 1
        grades.append('C')
    elif m >= 60:
        pass_count += 1
        grades.append('D')
    else:
        fail_count += 1
        grades.append('F')

# Output
print(f"\nPassing students: {pass_count}")
print(f"Failing students: {fail_count}")

print("\n===== Grade Distribution =====")
print("Marks  || Grade")

for i in range(total_students):
    print(f"{marks[i]}     ||     {grades[i]}")