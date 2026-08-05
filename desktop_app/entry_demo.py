import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry Example")
root.geometry("420x260")

name = tk.StringVar()
ttk.Entry(root, textvariable=name).pack(fill="x", padx=24, pady=16)
ttk.Label(root, textvariable=name).pack(pady=8)

root.mainloop()
