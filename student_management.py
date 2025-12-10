import mysql.connector

# ---------- DATABASE CONNECTION ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="studentdb"
)

cursor = db.cursor()

# ---------- CREATE TABLE IF NOT EXISTS ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    course VARCHAR(255),
    city VARCHAR(255)
)
""")

# ---------- INSERT ----------
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    city = input("Enter City: ")

    query = "INSERT INTO students(name, age, course, city) VALUES (%s,%s,%s,%s)"
    values = (name, age, course, city)
    cursor.execute(query, values)
    db.commit()

    print("Student Added Successfully")

# ---------- VIEW ----------
def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    print("--- All Students ---")
    for row in result:
        print(row)
    print()

# ---------- UPDATE ----------
def update_student():
    view_students()
    sid = int(input("Enter Student ID To Update: "))

    name = input("New Name: ")
    age = int(input("New Age: "))
    course = input("New Course: ")
    city = input("New City: ")

    query = "UPDATE students SET name=%s, age=%s, course=%s, city=%s WHERE id=%s"
    values = (name, age, course, city, sid)

    cursor.execute(query, values)
    db.commit()

    print("Student Updated Successfully")

# ---------- DELETE ----------
def delete_student():
    view_students()
    sid = int(input("Enter Student ID To Delete: "))

    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (sid,))
    db.commit()

    print("Student Deleted Successfully")

# ---------- SEARCH ----------
def search_student():
    name = input("Enter Name To Search: ")
    query = "SELECT * FROM students WHERE name LIKE %s"
    cursor.execute(query, ("%"+name+"%",))

    result = cursor.fetchall()

    if result:
        print("--- Search Result ---")
        for row in result:
            print(row)
    else:
        print("No Student Found")


# ---------- MENU ----------
while True:
    print("""
========= Student Management System =========
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit
""")

    choice = int(input("ENTER CHOICE: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        search_student()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")
