import os 
import csv

csv_path = os.path.join("Student_management","student.csv")
os.makedirs("Student_management",exist_ok = True)
is_file_exist = os.path.isfile("student.csv")
is_empty = not is_file_exist or os.path.getsize(csv_path) == 0

def search_student():
    search_item = input("Enter the regstration no. of the student:")
    with open (csv_path,"r") as read_file:
        csv_reader = csv.DictReader(read_file)
        for line in csv_reader:
            if(line["ID"] == search_item ):
                print(f"Name={line['Name']} Registraion N0.={line['ID']} Semester ={line['Semester']}")
                break
            else:
                print("No Student is found")