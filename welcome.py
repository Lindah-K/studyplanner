from tkinter import *
import tkinter as tk
import subprocess

root = tk.Tk()
root.title ("Student Study Planner App")
root.geometry("385x420")
root.resizable(False, False)

welcome_label = tk.Label(root, text="Welcome to StudySmart!", font=("Arial",20,"bold"), fg="#f1f1f1", bg="teal",padx=120)
welcome_label.pack(pady=20)

def exit():
    root.after(500, root.destroy)

def welcome():
    root.after(500, root.destroy)
    subprocess.Popen(["python","welcome.py"])

def open_plan():
    root.after(500, root.destroy)
    subprocess.Popen(["python","subjects.py"])

def login():
    username = username_entry.get()
    password = password_entry.get()
    login_success = False
    user_exists = False

    with open ('user_data.txt', 'r') as f:
        for line in f:
            line = line.strip().split(',')
            if line[0] == username:
                user_exists = True

                if line[0] == username and line[1] == password:

                    # if username == "lin" and password == "123":
                    login_success = True
                    username_entry.delete(0, tk.END)
                    password_entry.delete(0, tk.END)
                    root.after(500, open_plan)
                    root.after(500, root.destroy)

    if not user_exists:
        error_label.config(text="User not registered!", fg="red", font=("Arial", 10, "bold"))
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        error_label.after(2000,error_label.destroy)
    elif login_success:
            success_label.config(text="Login Successful",fg="teal", font=("Arial", 12,"bold"))
    else:
            error_label.config(text="Incorrecct username or password!", fg="red", font=("Arial", 10, "bold"))
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            error_label.after(1000,welcome)
            error_label.after(1000,error_label.destroy)

def register():
    root.after(500, root.destroy)
    subprocess.Popen(["python","register.py"])

frame1 = tk.Frame(root, padx=10, pady=10)
frame2 = tk.Frame(root, padx=10, pady=10)

username_label = tk.Label(frame1, text="Username: ")
username_label.pack(side=tk.LEFT)
username_entry = tk.Entry(frame1,highlightcolor="teal", borderwidth=3)
username_entry.pack(side=tk.LEFT)

password_label = tk.Label(frame2, text="Password: ")
password_label.pack(side=tk.LEFT)
password_entry = tk.Entry(frame2, show="*", highlightcolor="teal", borderwidth=3)
password_entry.pack(side=tk.LEFT)

frame1.pack()
frame2.pack()

def show_password():
    if password_entry["show"] == "*":
        password_entry["show"] = ""
    else:
        password_entry["show"]="*"

show_password_checkbox = tk.Checkbutton(root, text="Show Password", command=show_password)
show_password_checkbox.pack(pady=10)
login_button = tk.Button(root, text="Login", command=login, bg="teal", fg="#f1f1f1",font="bold", padx=15)
login_button.pack(pady=5)

register_button = tk.Button(root, text="Register", command=register, bg="teal", fg="#f1f1f1", font="bold", padx=5)
register_button.pack(pady=5)

save_button = tk.Button(root, text="LOG OUT", command=exit, bg="teal", fg="#f1f1f1", font="bold")
save_button.pack(pady=5)

success_label = tk.Label(root, text="")
success_label.pack(pady=5)

error_label = tk.Label(root, text="")
error_label.pack()

root.mainloop()
