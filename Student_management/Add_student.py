import csv
import os
csv_path = os.path.join("Student_management", "student.csv")
os.makedirs("Student_management", exist_ok=True)  # Ensure folder exists
is_file_exists = os.path.isfile(csv_path)
is_empty = not is_file_exists or os.path.getsize(csv_path) == 0

def add_student():
   

    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_age = input("Enter student age: ")
    student_sem = input("Enter student semester: ")

    # ✅ Only check for existing student if file is not empty
    student_exists = False
    if not is_empty:
        with open(csv_path, "r", newline="") as read_file:
            csv_reader = csv.DictReader(read_file)
            for row in csv_reader:
                if row["ID"] == student_id:
                    student_exists = True
                    break

    if student_exists:
        print(f"Student with ID {student_id} is already registered.")
    else:
        with open(csv_path, "a", newline="") as write_file:
            csv_writer = csv.DictWriter(write_file, fieldnames=["ID", "Name", "Age", "Semester"])
            if is_empty:
                csv_writer.writeheader()
            csv_writer.writerow({
                "ID": student_id,
                "Name": student_name,
                "Age": student_age,
                "Semester": student_sem
            })
            print(f"Student with ID {student_id} has been added successfully.")




 
def update_student():
    csv_path = os.path.join("Student_management", "student.csv")
    
    student_id = input("Enter student ID to update: ")
    
    updated = False
    updated_rows = []

    # Read all data
    with open(csv_path, "r", newline="") as read_file:
        csv_reader = csv.DictReader(read_file)
        for row in csv_reader:
            if row["ID"] == student_id:
                print(f"Current Name: {row['Name']} Age: {row['Age']} Semester: {row['Semester']}")
                new_name = input("Enter new name (Leave blank if no change): ")
                new_age = input("Enter new age (Leave blank if no change): ")
                new_sem = input("Enter new semester (Leave blank if no change): ")

                if new_name:
                    row["Name"] = new_name
                if new_age:
                    row["Age"] = new_age
                if new_sem:
                    row["Semester"] = new_sem

                updated = True
            updated_rows.append(row)

    # Write all rows back to the file
    if updated:
        with open(csv_path, "w", newline="") as write_file:
            fieldnames = ["ID", "Name", "Age", "Semester"]
            csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(updated_rows)
        print(f"Student with ID {student_id} has been updated successfully.")
    else:
        print("Student not found.")
