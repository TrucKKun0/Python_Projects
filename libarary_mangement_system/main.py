import csv
import os

file_path = os.path.join("library_management_system","student.csv")
os.makedirs("student.csv",exist_ok=True)
is_file_exist = os.path.isfile("student.csv")
is_empty = os.path.getsize == 0 or not is_file_exist 

get_role = input("Enter your role(student/admin):")
get_role = get_role.lower()
print(get_role)

if(get_role == 'student'):
    print("1. View details")
    print("2. Book Details")
    print("3. Change username or password")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit program")
    while True:
        input_choice  = input("Please select form option (1-7):")
        if(int(input_choice)==1):
            pass
        if(int(input_choice)==2):
            pass
        if(int(input_choice)==3):
            pass
        if(int(input_choice)==4):
            pass
        if(int(input_choice)==5):
            pass
        if(int(input_choice)==6):
            pass
        if(int(input_choice)==7):
            pass
       
if(get_role == 'admin'):
    print("1. Add book")
    print("2. Add student")
    print("3. Remove student")
    print("4. Remove book")
    print("5. View student")
    print("6. View book")
    print("7. Checks Login")
    while True:
        input_choice  = input("Please select form option (1-7):")
        if(int(input_choice)==1):
            pass
        if(int(input_choice)==2):
            pass
        if(int(input_choice)==3):
            pass
        if(int(input_choice)==4):
            pass
        if(int(input_choice)==5):
            pass
        if(int(input_choice)==6):
            pass
        if(int(input_choice)==7):
            pass