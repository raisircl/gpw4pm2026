import sqlite3
conn = sqlite3.connect('dbms_project/payroll.db')
cursor = conn.cursor()
# create dept table columns : dno primary key and auto generated, dname, dlocation
cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_dept (
    dno INTEGER PRIMARY KEY AUTOINCREMENT,
    dname TEXT NOT NULL,
    loc TEXT NOT NULL
)''')
conn.commit()
conn.close()

def create_dept(dname, loc):
    conn = sqlite3.connect('dbms_project/payroll.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tbl_dept (dname, loc) VALUES (?, ?)", (dname, loc))
    conn.commit()
    conn.close()

def read_dept():
    conn = sqlite3.connect('dbms_project/payroll.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tbl_dept")
    rows = cursor.fetchall()
    conn.close()
    return rows
def update_dept(dno, dname, loc):
    conn = sqlite3.connect('dbms_project/payroll.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tbl_dept SET dname = ?, loc = ? WHERE dno = ?", (dname, loc, dno))
    conn.commit()
    conn.close()
def delete_dept(dno):
    conn = sqlite3.connect('dbms_project/payroll.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tbl_dept WHERE dno = ?", (dno,))
    conn.commit()
    conn.close()


#create_dept("HR", "New York")
#alldepts = read_dept()
#for dept in alldepts:
#    print(dept)
#update_dept(2, 'SW', 'MHL')
#delete_dept(2)

while True:
    print("1. Create Department")
    print("2. Read Departments")
    print("3. Update Department")
    print("4. Delete Department")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        dname = input("Enter department name: ")
        loc = input("Enter department location: ")
        create_dept(dname, loc)
        print("Department created successfully.")
    elif choice == '2':
        alldepts = read_dept()
        for dept in alldepts:
            print(dept)
    elif choice == '3':
        dno = int(input("Enter department number to update: "))
        dname = input("Enter new department name: ")
        loc = input("Enter new department location: ")
        update_dept(dno, dname, loc)
        print("Department updated successfully.")
    elif choice == '4':
        dno = int(input("Enter department number to delete: "))
        delete_dept(dno)
        print("Department deleted successfully.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
