import tkinter as tk

root = tk.Tk()
root.title("Student App")
root.geometry("400x300")
root.configure(bg="#959CC0")
root.resizable(False, False)

label = tk.Label(root, text="Enter Your Name:", font=("Arial", 12), bg="#959CC0", fg="white")
label.pack()

entry = tk.Entry(root)
entry.pack()

def submit():   
    user_input = entry.get()
    print(f"User input: {user_input}")

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()

