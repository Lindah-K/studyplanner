import tkinter as tk
from tkinter import *
import subprocess

# create window
window = tk.Tk()
window.title("Sign Up On StudySmart App")
window.geometry("380x400")
window.resizable(False, False)

welcome_label = tk.Label(window, text="Register with us!", font=("Arial",20,"bold"), fg="#f1f1f1", bg="teal",padx=120)
welcome_label.pack(pady=20)

def welcome():
    window.after(500, window.destroy)
    subprocess.Popen(["python","welcome.py"])

# create frames for labels and entry fields
# label_frame = tk.Frame(window)
# label_frame.pack(side="left", padx=10)
# entry_frame = tk.Frame(window)
# entry_frame.pack(side="right", padx=10)
frame1 = tk.Frame(window, padx=10, pady=10)
frame2 = tk.Frame(window, padx=10, pady=10)
frame3 = tk.Frame(window, padx=10, pady=10)

username_label = tk.Label(frame1, text="Username:   ")
username_label.pack(side=tk.LEFT)
username_entry = tk.Entry(frame1,highlightcolor="teal", borderwidth=3)
username_entry.pack(side=tk.LEFT)

password_label = tk.Label(frame2, text="Password:    ")
password_label.pack(side=tk.LEFT)
password_entry = tk.Entry(frame2, show="*", highlightcolor="teal", borderwidth=3)
password_entry.pack(side=tk.LEFT)

confirm_password_label = tk.Label(frame3, text="Confirm Password: ")
confirm_password_label.pack(side=tk.LEFT)
confirm_password_entry = tk.Entry(frame3, show="*", highlightcolor="teal", borderwidth=3)
confirm_password_entry.pack(side=tk.LEFT)

frame1.pack()
frame2.pack()
frame3.pack()

# create show/hide password checkbox
# show_password_var = tk.BooleanVar()
# show_password_checkbox = tk.Checkbutton(window, text="Show Password", variable=show_password_var)
# show_password_checkbox.pack(pady=10)
def show_password():
    if password_entry["show"] == "*":
        password_entry["show"] = ""

        if confirm_password_entry["show"] == "*":
            confirm_password_entry["show"] = ""
    else:
        password_entry["show"]="*"
        confirm_password_entry["show"]= ""

show_password_checkbox = tk.Checkbutton(window, text="Show Password", command=show_password)
show_password_checkbox.pack(pady=10)
# create submit button
def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        error_label.config(window, text="Passwords do not match!",fg="red", font=("Arial", 11, "bold"))
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)  

        return

    with open("user_data.txt", "a") as f:
        f.write(f"{username},{password}\n")
    success_label.config(text="Succeesfully registered! Log in!", fg="teal", font=("Arial", 11,"bold"))
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

submit_button = tk.Button(window, text="Register",command=register, bg="teal", fg="#f1f1f1", font="bold")
submit_button.pack(pady=10)

submit_button = tk.Button(window, text="Get Started",command=welcome, bg="teal", fg="#f1f1f1", font="bold")
submit_button.pack(pady=10)

# window.after(500, window.destroy)
# window.after(500, welcome)


success_label = tk.Label(window, text="")
success_label.pack(pady=5)

error_label = tk.Label(window, text="")
error_label.pack(pady=5)

window.mainloop()
