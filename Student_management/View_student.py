import csv
import os
def view_students():
    
    csv_path = os.path.join("Student_management", "student.csv")
    os.makedirs("Student_management", exist_ok=True)  # Ensure folder exists
    is_file_exists = os.path.isfile(csv_path)
    is_empty = not is_file_exists or os.path.getsize(csv_path) == 0
    if is_empty:
        print("No student Found")
        
    else:
        with open(csv_path,'r') as view_file:
            csv_reader = csv.DictReader(view_file)
            for row in csv_reader:
                print(f"ID: {row['ID']}, Name: {row['Name']}, Age: {row['Age']}, Semester: {row['Semester']}")