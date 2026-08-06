import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


DB_NAME = "company.db"


class CompanyApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Department and Employee Management")
        self.geometry("1050x650")
        self.minsize(950, 580)

        # Open database connection
        self.conn = sqlite3.connect(DB_NAME)

        # Enable SQLite foreign-key constraints
        self.conn.execute("PRAGMA foreign_keys = ON")

        self.create_tables()

        # Store selected record IDs
        self.selected_dept_id = None
        self.selected_emp_id = None

        # Department dropdown mappings
        self.dept_label_to_id = {}
        self.dept_id_to_label = {}

        self.create_styles()
        self.create_widgets()

        self.load_departments()
        self.refresh_department_dropdown()
        self.load_employees()

        self.protocol("WM_DELETE_WINDOW", self.close_app)

    # =====================================================
    # DATABASE TABLE CREATION
    # =====================================================

    def create_tables(self):

        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tblDept
            (
                DeptId INTEGER PRIMARY KEY AUTOINCREMENT,
                DeptName TEXT NOT NULL UNIQUE
            )
            """
        )

        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tblEmp
            (
                EmpId INTEGER PRIMARY KEY AUTOINCREMENT,
                EmpName TEXT NOT NULL,
                Email TEXT,
                Salary REAL NOT NULL DEFAULT 0
                    CHECK (Salary >= 0),

                DeptId INTEGER NOT NULL,

                FOREIGN KEY (DeptId)
                    REFERENCES tblDept(DeptId)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT
            )
            """
        )

        self.conn.commit()

    # =====================================================
    # APPLICATION DESIGN
    # =====================================================

    def create_styles(self):

        style = ttk.Style(self)

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 18, "bold")
        )

        style.configure(
            "TButton",
            padding=7
        )

        style.configure(
            "Treeview",
            rowheight=28
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

    def create_widgets(self):

        title = ttk.Label(
            self,
            text="Department and Employee CRUD Application",
            style="Title.TLabel"
        )

        title.pack(pady=(14, 8))

        notebook = ttk.Notebook(self)
        notebook.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        self.dept_tab = ttk.Frame(
            notebook,
            padding=15
        )

        self.emp_tab = ttk.Frame(
            notebook,
            padding=15
        )

        notebook.add(
            self.dept_tab,
            text="Department Management"
        )

        notebook.add(
            self.emp_tab,
            text="Employee Management"
        )

        self.build_department_tab()
        self.build_employee_tab()

    # =====================================================
    # DEPARTMENT FORM DESIGN
    # =====================================================

    def build_department_tab(self):

        form = ttk.LabelFrame(
            self.dept_tab,
            text="Department Form",
            padding=15
        )

        form.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            form,
            text="Department Name:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.dept_name_var = tk.StringVar()

        self.dept_name_entry = ttk.Entry(
            form,
            textvariable=self.dept_name_var,
            width=35
        )

        self.dept_name_entry.grid(
            row=0,
            column=1,
            padx=8,
            pady=8,
            sticky="w"
        )

        button_frame = ttk.Frame(form)

        button_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(10, 0),
            sticky="w"
        )

        ttk.Button(
            button_frame,
            text="Add",
            command=self.add_department
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Update",
            command=self.update_department
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Delete",
            command=self.delete_department
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_department_form
        ).pack(side="left", padx=4)

        list_frame = ttk.LabelFrame(
            self.dept_tab,
            text="Department Records",
            padding=10
        )

        list_frame.pack(
            fill="both",
            expand=True
        )

        self.dept_tree = ttk.Treeview(
            list_frame,
            columns=("DeptId", "DeptName"),
            show="headings",
            selectmode="browse"
        )

        self.dept_tree.heading(
            "DeptId",
            text="Department ID"
        )

        self.dept_tree.heading(
            "DeptName",
            text="Department Name"
        )

        self.dept_tree.column(
            "DeptId",
            width=150,
            anchor="center"
        )

        self.dept_tree.column(
            "DeptName",
            width=500
        )

        self.dept_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.dept_tree.bind(
            "<<TreeviewSelect>>",
            self.on_department_select
        )

        scrollbar = ttk.Scrollbar(
            list_frame,
            orient="vertical",
            command=self.dept_tree.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.dept_tree.configure(
            yscrollcommand=scrollbar.set
        )

    # =====================================================
    # EMPLOYEE FORM DESIGN
    # =====================================================

    def build_employee_tab(self):

        form = ttk.LabelFrame(
            self.emp_tab,
            text="Employee Form",
            padding=15
        )

        form.pack(
            fill="x",
            pady=(0, 15)
        )

        self.emp_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.salary_var = tk.StringVar()
        self.department_var = tk.StringVar()

        # Employee name

        ttk.Label(
            form,
            text="Employee Name:"
        ).grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        ttk.Entry(
            form,
            textvariable=self.emp_name_var,
            width=32
        ).grid(
            row=0,
            column=1,
            padx=8,
            pady=8,
            sticky="w"
        )

        # Email

        ttk.Label(
            form,
            text="Email:"
        ).grid(
            row=0,
            column=2,
            padx=8,
            pady=8,
            sticky="w"
        )

        ttk.Entry(
            form,
            textvariable=self.email_var,
            width=32
        ).grid(
            row=0,
            column=3,
            padx=8,
            pady=8,
            sticky="w"
        )

        # Salary

        ttk.Label(
            form,
            text="Salary:"
        ).grid(
            row=1,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        ttk.Entry(
            form,
            textvariable=self.salary_var,
            width=32
        ).grid(
            row=1,
            column=1,
            padx=8,
            pady=8,
            sticky="w"
        )

        # Department dropdown

        ttk.Label(
            form,
            text="Department:"
        ).grid(
            row=1,
            column=2,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.department_combo = ttk.Combobox(
            form,
            textvariable=self.department_var,
            width=29,
            state="readonly"
        )

        self.department_combo.grid(
            row=1,
            column=3,
            padx=8,
            pady=8,
            sticky="w"
        )

        button_frame = ttk.Frame(form)

        button_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            pady=(12, 0),
            sticky="w"
        )

        ttk.Button(
            button_frame,
            text="Add",
            command=self.add_employee
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Update",
            command=self.update_employee
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Delete",
            command=self.delete_employee
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_employee_form
        ).pack(side="left", padx=4)

        ttk.Button(
            button_frame,
            text="Refresh",
            command=self.load_employees
        ).pack(side="left", padx=4)

        # Employee Treeview

        list_frame = ttk.LabelFrame(
            self.emp_tab,
            text="Employee Records",
            padding=10
        )

        list_frame.pack(
            fill="both",
            expand=True
        )

        columns = (
            "EmpId",
            "EmpName",
            "Email",
            "Salary",
            "DeptName"
        )

        self.emp_tree = ttk.Treeview(
            list_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        headings = {
            "EmpId": "Employee ID",
            "EmpName": "Employee Name",
            "Email": "Email",
            "Salary": "Salary",
            "DeptName": "Department"
        }

        widths = {
            "EmpId": 110,
            "EmpName": 180,
            "Email": 240,
            "Salary": 120,
            "DeptName": 180
        }

        for column in columns:

            self.emp_tree.heading(
                column,
                text=headings[column]
            )

            anchor_value = "center" if column in (
                "EmpId",
                "Salary"
            ) else "w"

            self.emp_tree.column(
                column,
                width=widths[column],
                anchor=anchor_value
            )

        self.emp_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.emp_tree.bind(
            "<<TreeviewSelect>>",
            self.on_employee_select
        )

        scrollbar = ttk.Scrollbar(
            list_frame,
            orient="vertical",
            command=self.emp_tree.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.emp_tree.configure(
            yscrollcommand=scrollbar.set
        )

    # =====================================================
    # DEPARTMENT: CREATE
    # =====================================================

    def add_department(self):

        dept_name = self.dept_name_var.get().strip()

        if not dept_name:

            messagebox.showwarning(
                "Validation",
                "Enter a department name."
            )

            return

        try:

            self.conn.execute(
                """
                INSERT INTO tblDept (DeptName)
                VALUES (?)
                """,
                (dept_name,)
            )

            self.conn.commit()

            messagebox.showinfo(
                "Success",
                "Department added successfully."
            )

            self.clear_department_form()
            self.load_departments()
            self.refresh_department_dropdown()
            self.load_employees()

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Duplicate",
                "This department already exists."
            )

    # =====================================================
    # DEPARTMENT: READ
    # =====================================================

    def load_departments(self):

        # Remove old rows
        for item in self.dept_tree.get_children():
            self.dept_tree.delete(item)

        rows = self.conn.execute(
            """
            SELECT DeptId, DeptName
            FROM tblDept
            ORDER BY DeptName
            """
        ).fetchall()

        for dept_id, dept_name in rows:

            self.dept_tree.insert(
                "",
                "end",
                values=(
                    dept_id,
                    dept_name
                )
            )

    def on_department_select(self, event=None):

        selected = self.dept_tree.selection()

        if not selected:
            return

        values = self.dept_tree.item(
            selected[0],
            "values"
        )

        self.selected_dept_id = int(values[0])
        self.dept_name_var.set(values[1])

    # =====================================================
    # DEPARTMENT: UPDATE
    # =====================================================

    def update_department(self):

        if self.selected_dept_id is None:

            messagebox.showwarning(
                "Selection",
                "Select a department to update."
            )

            return

        dept_name = self.dept_name_var.get().strip()

        if not dept_name:

            messagebox.showwarning(
                "Validation",
                "Enter a department name."
            )

            return

        try:

            self.conn.execute(
                """
                UPDATE tblDept
                SET DeptName = ?
                WHERE DeptId = ?
                """,
                (
                    dept_name,
                    self.selected_dept_id
                )
            )

            self.conn.commit()

            messagebox.showinfo(
                "Success",
                "Department updated successfully."
            )

            self.clear_department_form()
            self.load_departments()
            self.refresh_department_dropdown()
            self.load_employees()

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Duplicate",
                "This department already exists."
            )

    # =====================================================
    # DEPARTMENT: DELETE
    # =====================================================

    def delete_department(self):

        if self.selected_dept_id is None:

            messagebox.showwarning(
                "Selection",
                "Select a department to delete."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Delete the selected department?\n\n"
            "A department containing employees cannot be deleted."
        )

        if not confirm:
            return

        try:

            self.conn.execute(
                """
                DELETE FROM tblDept
                WHERE DeptId = ?
                """,
                (self.selected_dept_id,)
            )

            self.conn.commit()

            messagebox.showinfo(
                "Success",
                "Department deleted successfully."
            )

            self.clear_department_form()
            self.load_departments()
            self.refresh_department_dropdown()

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Cannot Delete",
                "This department is assigned to one or more employees.\n\n"
                "Delete or reassign those employees first."
            )

    def clear_department_form(self):

        self.selected_dept_id = None
        self.dept_name_var.set("")

        for selected in self.dept_tree.selection():
            self.dept_tree.selection_remove(selected)

        self.dept_name_entry.focus_set()

    # =====================================================
    # DEPARTMENT DROPDOWN
    # =====================================================

    def refresh_department_dropdown(self):

        rows = self.conn.execute(
            """
            SELECT DeptId, DeptName
            FROM tblDept
            ORDER BY DeptName
            """
        ).fetchall()

        self.dept_label_to_id.clear()
        self.dept_id_to_label.clear()

        labels = []

        for dept_id, dept_name in rows:

            label = f"{dept_id} - {dept_name}"

            labels.append(label)

            self.dept_label_to_id[label] = dept_id
            self.dept_id_to_label[dept_id] = label

        self.department_combo["values"] = labels

        if self.department_var.get() not in labels:
            self.department_var.set("")

    # =====================================================
    # EMPLOYEE VALIDATION
    # =====================================================

    def validate_employee_form(self):

        emp_name = self.emp_name_var.get().strip()
        email = self.email_var.get().strip()
        salary_text = self.salary_var.get().strip()
        department_label = self.department_var.get().strip()

        if not emp_name:

            messagebox.showwarning(
                "Validation",
                "Enter the employee name."
            )

            return None

        if not salary_text:

            messagebox.showwarning(
                "Validation",
                "Enter the salary."
            )

            return None

        try:

            salary = float(salary_text)

            if salary < 0:
                raise ValueError

        except ValueError:

            messagebox.showwarning(
                "Validation",
                "Salary must be a valid non-negative number."
            )

            return None

        dept_id = self.dept_label_to_id.get(
            department_label
        )

        if dept_id is None:

            messagebox.showwarning(
                "Validation",
                "Select a department."
            )

            return None

        return emp_name, email, salary, dept_id

    # =====================================================
    # EMPLOYEE: CREATE
    # =====================================================

    def add_employee(self):

        data = self.validate_employee_form()

        if data is None:
            return

        emp_name, email, salary, dept_id = data

        self.conn.execute(
            """
            INSERT INTO tblEmp
            (
                EmpName,
                Email,
                Salary,
                DeptId
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                emp_name,
                email,
                salary,
                dept_id
            )
        )

        self.conn.commit()

        messagebox.showinfo(
            "Success",
            "Employee added successfully."
        )

        self.clear_employee_form()
        self.load_employees()

    # =====================================================
    # EMPLOYEE: READ
    # =====================================================

    def load_employees(self):

        for item in self.emp_tree.get_children():
            self.emp_tree.delete(item)

        rows = self.conn.execute(
            """
            SELECT
                e.EmpId,
                e.EmpName,
                COALESCE(e.Email, ''),
                e.Salary,
                d.DeptName
            FROM tblEmp AS e
            INNER JOIN tblDept AS d
                ON d.DeptId = e.DeptId
            ORDER BY e.EmpId DESC
            """
        ).fetchall()

        for row in rows:

            emp_id = row[0]
            emp_name = row[1]
            email = row[2]
            salary = row[3]
            dept_name = row[4]

            self.emp_tree.insert(
                "",
                "end",
                iid=str(emp_id),
                values=(
                    emp_id,
                    emp_name,
                    email,
                    f"{salary:.2f}",
                    dept_name
                )
            )

    def on_employee_select(self, event=None):

        selected = self.emp_tree.selection()

        if not selected:
            return

        emp_id = int(selected[0])

        row = self.conn.execute(
            """
            SELECT
                EmpId,
                EmpName,
                COALESCE(Email, ''),
                Salary,
                DeptId
            FROM tblEmp
            WHERE EmpId = ?
            """,
            (emp_id,)
        ).fetchone()

        if row is None:
            return

        self.selected_emp_id = row[0]
        self.emp_name_var.set(row[1])
        self.email_var.set(row[2])
        self.salary_var.set(str(row[3]))

        dept_id = row[4]

        self.department_var.set(
            self.dept_id_to_label.get(
                dept_id,
                ""
            )
        )

    # =====================================================
    # EMPLOYEE: UPDATE
    # =====================================================

    def update_employee(self):

        if self.selected_emp_id is None:

            messagebox.showwarning(
                "Selection",
                "Select an employee to update."
            )

            return

        data = self.validate_employee_form()

        if data is None:
            return

        emp_name, email, salary, dept_id = data

        self.conn.execute(
            """
            UPDATE tblEmp
            SET
                EmpName = ?,
                Email = ?,
                Salary = ?,
                DeptId = ?
            WHERE EmpId = ?
            """,
            (
                emp_name,
                email,
                salary,
                dept_id,
                self.selected_emp_id
            )
        )

        self.conn.commit()

        messagebox.showinfo(
            "Success",
            "Employee updated successfully."
        )

        self.clear_employee_form()
        self.load_employees()

    # =====================================================
    # EMPLOYEE: DELETE
    # =====================================================

    def delete_employee(self):

        if self.selected_emp_id is None:

            messagebox.showwarning(
                "Selection",
                "Select an employee to delete."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Delete the selected employee record?"
        )

        if not confirm:
            return

        self.conn.execute(
            """
            DELETE FROM tblEmp
            WHERE EmpId = ?
            """,
            (self.selected_emp_id,)
        )

        self.conn.commit()

        messagebox.showinfo(
            "Success",
            "Employee deleted successfully."
        )

        self.clear_employee_form()
        self.load_employees()

    def clear_employee_form(self):

        self.selected_emp_id = None

        self.emp_name_var.set("")
        self.email_var.set("")
        self.salary_var.set("")
        self.department_var.set("")

        for selected in self.emp_tree.selection():
            self.emp_tree.selection_remove(selected)

    # =====================================================
    # CLOSE APPLICATION
    # =====================================================

    def close_app(self):

        self.conn.close()
        self.destroy()


if __name__ == "__main__":

    app = CompanyApp()
    app.mainloop()