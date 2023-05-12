from tkinter import *
import tkinter as tk
import subprocess

app = tk.Tk()
app.title ("Student Study Planner App")
app.geometry("360x320")
app.resizable(False, False)

welcome_label = tk.Label(app, text="My Plan:", font=("Arial",18,"bold"), fg="#f1f1f1", bg="teal", padx=130)
welcome_label.pack()

text_label = tk.Label(app, text="")

    # Open the text file and read its contents
with open("subjects.txt", "r") as file:
    for line in file:
        line = line.strip().split(',')
        file_contents = file.read()

    # Set the label's text to the contents of the text file
    text_label.config(text=file_contents)

    # Pack the label into the window
    text_label.pack()

def edit_plan():
    app.after(500, app.destroy)
    subprocess.Popen(["python","editplan.py"])

def edit_flashcards():
    app.after(500, app.destroy)
    subprocess.Popen(["python","flashcards.py"])

def exit_plan():
    app.after(500, app.destroy)
    subprocess.Popen(["python","subjects.py"])


save_button = tk.Button(app, text="Edit Plan", command=edit_plan, bg="teal", fg="#f1f1f1",font="10", padx=25)
save_button.pack(pady=5)

save_button = tk.Button(app, text="My Flashcards", command=edit_flashcards, bg="teal", fg="#f1f1f1",font="10", padx=5)
save_button.pack(pady=5)

save_button = tk.Button(app, text="Exit Plan", command=exit_plan, bg="teal", fg="#f1f1f1",font="10", padx=25)
save_button.pack(pady=5)

app.mainloop()