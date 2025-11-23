def calculate_grade(percentage):
    if percentage >= 90:
        return "S"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
    
print("Student Grade Calculator")

n = int(input("Enter number of subjects: "))
marks = [ ]
for i in range(n):
    m = float(input(f"Enter marks for subject{i+1}: "))
    marks.append(m)
    
total = sum(marks)
percentage = (total / (n*100))*100
grade = calculate_grade(percentage)

print("\n-RESULT-")
print(f"Total Marks : {total}/{n*100}")
print(f"Percentage : {percentage: .2f}%")
print(f"Grade : {grade}")