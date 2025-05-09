from Add_student import add_student

print("Welcome to the Student Management System")
print("1. Add Student")
print("2. View Students")
print("3. Update Student")
print("4. Search Student")
print("5. Delete Student")
print("6. Exit")

while True:
    input_choice = input("Please select an option (1-6): ")
    if input_choice == "1":
        add_student()
    elif input_choice == "2":
        pass  # Placeholder for view students
    elif input_choice == "3":
        pass  # Placeholder for update student
    elif input_choice == "4":
        pass  # Placeholder for search student
    elif input_choice == "5":
        pass  # Placeholder for delete student
    elif input_choice == "6":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
