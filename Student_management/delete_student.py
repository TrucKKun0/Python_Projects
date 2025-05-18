import os 
import csv

csv_path = os.path.join("Student_management","student.csv")
os.makedirs("Student_management",exist_ok = True)
is_file_exist = os.path.isfile("student.csv")
is_empty = not is_file_exist or os.path.getsize(csv_path) == 0

def delete_student():
    input_id = input("Enter the student ID to delete: ")
    student_found = False
    updated_rows = []
    with open(csv_path, "r", newline="") as read_file:
        csv_reader = csv.DictReader(read_file)
        for row in csv_reader:
            if row["ID"] == input_id:
                student_found = True
                print(f"Student with ID {input_id} has been deleted.")
            else:
                updated_rows.append(row)
    if not student_found:
            print(f"No student found with ID {input_id}.")
    with open(csv_path, "w", newline="") as write_file:
        csv_writer = csv.DictWriter(write_file, fieldnames=["ID", "Name", "Semester"])
        csv_writer.writeheader()
        csv_writer.writerows(updated_rows)