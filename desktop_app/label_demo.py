import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Example")
root.geometry("420x260")

message = tk.StringVar(value="Hello from Label")
ttk.Label(root, textvariable=message, font=("Segoe UI", 14, "bold")).pack(pady=20)
ttk.Button(root, text="Change", command=lambda: message.set("Label updated")).pack()


root.mainloop()
