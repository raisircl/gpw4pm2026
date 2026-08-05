import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    course = course_entry.get()
    if name == "":
        messagebox.showerror("Error", "Name is required")
        return
    
    if course == "":
        messagebox.showerror("Error", "Course is required")
        return

    messagebox.showinfo("Submission Data", f"Name: {name}\nCourse: {course}")

root = tk.Tk()
root.geometry("500x350")

tk.Label(root, text="Name", font=("Arial",12,"bold")).grid(row=1, column=1)
name_entry=tk.Entry(root, font=("Arial",12))
name_entry.grid(row=1, column=2)

tk.Label(root, text="Course", font=("Arial",12,"bold")).grid(row=2, column=1)
course_entry=tk.Entry(root, font=("Arial",12))
course_entry.grid(row=2, column=2)
tk.Button(root, text="Submit", bg="lightblue", fg="black", command=submit).grid(row=3,column=2)

root.mainloop()
