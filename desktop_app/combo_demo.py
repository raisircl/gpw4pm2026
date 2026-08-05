import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox Example")
root.geometry("420x260")

course = tk.StringVar()
combo = ttk.Combobox(root, textvariable=course, values=["Python", "Tkinter", "SQLite"], state="readonly")
combo.pack(padx=20, pady=20)
combo.set("Tkinter")

root.mainloop()
