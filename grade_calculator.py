# Student Grade Calculator - Enhanced Version (Week 2 Project)
# Developed by: Priya Kumari
# Description:
# This program collects student marks, calculates grades & comments,
# shows class statistics, includes a search feature, saves results to file,
# and uses a simple menu-based system as required in the assignment.

def calculate_grade(average):
    """Calculate grade and give comment"""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'


def get_valid_number(prompt, min_val=0, max_val=100):
    """Get valid number between min and max"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")


def get_positive_int(prompt):
    """Accept only positive integers"""
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Please enter a positive number!")
        except ValueError:
            print("Invalid input! Enter a whole number.")


# =====================================================
# MAIN PROGRAM LOGIC
# =====================================================

def enter_student_data():
    """Collect data for all students"""
    student_names = []
    student_marks = []
    student_results = []

    num_students = get_positive_int("Enter number of students: ")

    for i in range(num_students):
        print(f"\n=== STUDENT {i+1} ===")

        # Name
        name = input("Student name: ").strip()
        while name == "":
            print("Name cannot be empty!")
            name = input("Student name: ").strip()
        student_names.append(name)

        # Marks
        print("Enter marks (0-100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        marks = [math, science, english]
        student_marks.append(marks)

        # Average, grade, comment
        avg = sum(marks) / 3
        grade, comment = calculate_grade(avg)

        student_results.append({
            "average": avg,
            "grade": grade,
            "comment": comment
        })

    return student_names, student_marks, student_results


def display_results(names, marks, results):
    """Shows formatted results + class statistics"""
    print("\n" + "=" * 50)
    print("               RESULTS SUMMARY")
    print("=" * 50)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 60)

    for i in range(len(names)):
        name = names[i]
        avg = results[i]["average"]
        grade = results[i]["grade"]
        comment = results[i]["comment"]

        print(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}")

    # Class Statistics
    averages = [res["average"] for res in results]
    class_avg = sum(averages) / len(averages)
    max_avg = max(averages)
    min_avg = min(averages)
    max_name = names[averages.index(max_avg)]
    min_name = names[averages.index(min_avg)]

    print("\n" + "=" * 50)
    print("              CLASS STATISTICS")
    print("=" * 50)
    print(f"Total Students: {len(names)}")
    print(f"Class Average: {class_avg:.1f}")
    print(f"Highest Average: {max_avg:.1f} ({max_name})")
    print(f"Lowest Average: {min_avg:.1f} ({min_name})")


def search_student(names, results):
    """Search student by name"""
    name = input("\nEnter student name to search: ").strip()

    for i in range(len(names)):
        if names[i].lower() == name.lower():
            print("\n✓ Student Found")
            print(f"Name: {names[i]}")
            print(f"Average: {results[i]['average']:.1f}")
            print(f"Grade: {results[i]['grade']}")
            print(f"Comment: {results[i]['comment']}")
            return
    print("✗ Student not found!")


def save_to_file(names, marks, results):
    """Save results to a text file"""
    with open("test_students.txt", "w") as f:
        f.write("STUDENT GRADE REPORT\n")
        f.write("=" * 40 + "\n\n")

        for i in range(len(names)):
            f.write(f"Name: {names[i]}\n")
            f.write(f"Marks: {marks[i]}\n")
            f.write(f"Average: {results[i]['average']:.1f}\n")
            f.write(f"Grade: {results[i]['grade']}\n")
            f.write(f"Comment: {results[i]['comment']}\n")
            f.write("-" * 30 + "\n")

    print("\n✓ Results saved to test_students.txt")


def menu():
    print("\n" + "=" * 50)
    print("               MAIN MENU")
    print("=" * 50)
    print("1. Enter Student Data")
    print("2. Display Results")
    print("3. Search Student")
    print("4. Save to File")
    print("5. Exit")
    print("=" * 50)


def main():
    student_names = []
    student_marks = []
    student_results = []

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            student_names, student_marks, student_results = enter_student_data()

        elif choice == "2":
            if student_names:
                display_results(student_names, student_marks, student_results)
            else:
                print("No data available! Please enter students first.")

        elif choice == "3":
            if student_names:
                search_student(student_names, student_results)
            else:
                print("No data available!")

        elif choice == "4":
            if student_names:
                save_to_file(student_names, student_marks, student_results)
            else:
                print("No data to save!")

        elif choice == "5":
            print("Thank you for using the Grade Calculator!")
            break

        else:
            print("Invalid option! Please choose again.")


if __name__ == "__main__":
    main()