Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("------------------------------\n        Main Menu\n--------------------------------")
... a = "Sign In"
... b = "Log In to List"
... c = "List of Students"
... d = "Edit Information"
... e = "Sign In New Student"
... f = "Delete"
... g = "Exit"
... print(f"1.{a}\n2.{b}\n3.{c}\n4.{d}\n5.{e}\n6.{f}\n7.{g}")
... 
... my_dic = {1: a, 2: b, 3: c, 4: d, 5: e, 6: f, 7: g}
... 
... admin_entreee = False
... student_dict = {
...    "name": ["mohamad", "baran"],
...    "family": ["nori", "hojati"],
...    "number": [20010, 20011],
...    "class_name": ["A1", "B3"]
... }
... 
... def menu():
...     while True:
...         h = input("Enter your choice (1-7): ")
...         if h.isdigit():
...             h = int(h)
...             if h == 1:
...                 sign_in()
...             elif h == 2:
...                 admin_entree()
...             elif h == 3:
...                 show_dict()
...             elif h == 4:
...                 register_std()
...             elif h == 5:
...                 edite_inf_std()
...             elif h == 6:
                delete_std()
            elif h == 7:
                exit_system()
            else:
                print("Wrong choice, Please try again.")
        else:
            print("Wrong choice, Please try again.")

def sign_in():
    global phone_num, password, name, family
    name = input("Enter your name: ")
    family = input("Enter your family name: ")
    while True:
        phone_num = input("Enter your phone number: ")
        if len(phone_num) == 11 and phone_num[0] == "0" and phone_num.isdigit():
            print("Phone number is valid.")
            break
        else:
            print("Wrong phone number.")
    password = input("Enter your password: ")
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    if has_letter and has_digit:
        print("Password is valid.")
    else:
        print("Password must include at least one letter and one digit.")

def admin_entree():
    global admin_entreee
    for _ in range(3):
        au = input("Enter your admin username: ")
        ap = input("Enter your admin password: ")
        if au == phone_num and ap == password:
            admin_entreee = True
            print("Welcome admin!")
            return
    print("Too many failed attempts. Access denied.")

def show_dict():
    if admin_entreee:
        print(student_dict)
    else:
        print("You are not admin.")

def register_std():
    if admin_entreee:
        name = input("Enter student name: ")
        family = input("Enter student family: ")
        number = input("Enter student number: ")
        class_name = input("Enter student class name: ")
        student_dict["name"].append(name)
        student_dict["family"].append(family)
        student_dict["number"].append(int(number))
        student_dict["class_name"].append(class_name)
    else:
        print("You are not admin.")

def edite_inf_std():
    if admin_entreee:
        std_num = int(input("Enter student number: "))
        if std_num in student_dict["number"]:
            idx = student_dict["number"].index(std_num)
            student_dict["name"][idx] = input("Enter new name: ")
            student_dict["family"][idx] = input("Enter new family: ")
            student_dict["class_name"][idx] = input("Enter new class name: ")
        else:
            print("Student not found.")
    else:
        print("Access denied.")

def delete_std():
    if admin_entreee:
        std_num = int(input("Enter student number: "))
        if std_num in student_dict["number"]:
            idx = student_dict["number"].index(std_num)
            del student_dict["name"][idx]
            del student_dict["family"][idx]
            del student_dict["number"][idx]
            del student_dict["class_name"][idx]
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    else:
        print("Access denied.")

def exit_system():
    global admin_entreee
    admin_entreee = False
    print("You have been logged out.")

menu()
