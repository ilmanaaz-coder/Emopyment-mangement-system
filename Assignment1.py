empolye= {101:                               # sample empolyee dictionary
             {"Name":"Amit",
              "Age":23,
              "Department":"IT",
              "Salary":50000}
         }
# Dictionary to store employees
empolye = {}

def add_employee():   #  Unique Employee ID
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in empolye:
                print("ID already exists. Enter another ID.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    #  Employee name
    name = input("Enter Employee name: ")

    #  Employee age
    while True:
        try:
            age = int(input("Enter Employee age: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    #  Employee department
    department = input("Enter Employee department: ")

    #  Employee salary
    while True:
        try:
            salary = float(input("Enter Employee salary: "))
            break
        except ValueError:
            print("Please enter a valid digit.")

    # Store in dictionary
    empolye[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print(f"Employee {name} added successfully!")



add_employee()

print(empolye)



#view empolyee
def view_employee():
    if not empolye:
        print('No Employee Data available')
        return

    # Header
    print(f"{'ID':<6}{'Name':<20}{'Age':<4}{'Department':<16}{'Salary':<10}")
    print('-'*60)

    # Employee details
    for emp_id, details in empolye.items():
        print(f"{emp_id:<6}{details['name']:<20}{details['age']:<4}{details['department']:<16}{details['salary']:<10}")

view_employee()


#search empolyee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    if emp_id in empolye:
        details = empolye[emp_id]
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    else:
        print("Employee not found.")
search_employee()

#menu driven
def menu_driven():
    while True:
        print("1. Add employee")
        print("2. view all empolyee")
        print("3. search empolyee")
        print("4. Exit")

        choice=int(input( "Enter any number :" ))

        if choice == 1:
            add_empolyee()
        elif choice ==2:
            view_employee()
        elif choice == 3:
            search_employee()
        elif choice ==4:
            print("Thank you for using EMS ")
        else:
            print(" Invalid choice ,try again ")
menu_driven()