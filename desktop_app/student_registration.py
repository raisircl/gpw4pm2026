import tkinter as tk
from tkinter import messagebox
def say_hello():
    name = name_entry.get()
    course = course_entry.get()
    messagebox.showinfo("Information", f"Hello {name}, you have registered for the course: {course}")


root = tk.Tk()
root.geometry("500x300")

title = tk.Label(root, text="Student Registration", font=("Arial", 18, "bold"))
title.pack(pady=20)

tk.Label(root, text="Enter Student Name").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=10)

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack(pady=30)


root.mainloop()
