def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Number of students
    num_students = int(input("Enter the number of students: "))
    
    # Iterating over the number of students
    for i in range(num_students):
        # Input marks for each student
        marks = float(input(f"Enter marks for student {i + 1}: "))
        
        # Calculate grade using selection (if-else)
        grade = calculate_grade(marks)
        
        # Display the grade
        print(f"Student {i + 1} scored {marks} and received grade {grade}\n")

if __name__ == "__main__":
    main()
