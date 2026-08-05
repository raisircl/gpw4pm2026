import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Example")
root.geometry("420x260")

text = tk.Text(root, height=6, wrap="word")
text.pack(fill="both", expand=True, padx=20, pady=20)
text.insert("1.0", "Text widgets can hold multiple lines.")

root.mainloop()
