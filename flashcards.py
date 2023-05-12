import tkinter as tk
import random
import json
import subprocess

# set up the tkinter app
app = tk.Tk()
app.title ("Student Study Planner App")
app.geometry("440x480")
app.resizable(False, False)

welcome_label = tk.Label(app, text="My FlashCards:", font=("Arial",18,"bold"), fg="#f1f1f1", bg="teal", padx=130)
welcome_label.pack(pady=20)

# create the question and answer labels
question_label = tk.Label(app, text="")
question_label.pack(pady=5)

answer_label = tk.Label(app, text="")
answer_label.pack(pady=5)

def exit_plan():
    app.after(500, app.destroy)
    subprocess.Popen(["python","subjects.py"])
# create the buttons
def show_question():
    global current_question
    if len(flashcards) > 0:
        current_question = random.choice(list(flashcards.keys()))
        question_label.config(text=current_question)
        answer_label.config(text="")
    else:
        question_label.config(text="No flashcards found.")
        answer_label.config(text="")

show_question_button = tk.Button(app, text="Show Question", command=show_question, bg="teal", fg="#f1f1f1",font="bold")
show_question_button.pack(pady=10)

def show_answer():
    global current_question
    if current_question:
        answer = flashcards[current_question]
        answer_label.config(text=answer)
    else:
        answer_label.config(text="")

show_answer_button = tk.Button(app, text="Show Answer", command=show_answer, bg="teal", fg="#f1f1f1",font="bold", padx=6)
show_answer_button.pack(pady=10)

def add_flashcard():
    question = question_entry.get()
    answer = answer_entry.get()
    if question and answer:
        flashcards[question] = answer
        save_flashcards()
        question_entry.delete(0, tk.END)
        answer_entry.delete(0, tk.END)

add_flashcard_button = tk.Button(app, text="Add Flashcard", command=add_flashcard, bg="teal", fg="#f1f1f1",font="bold", padx=4)
add_flashcard_button.pack(pady=10)

# create the flashcard entry fields
question_entry = tk.Entry(app, highlightcolor="teal", borderwidth=3)
question_entry.pack(pady=5)

answer_entry = tk.Entry(app, highlightcolor="teal", borderwidth=3)
answer_entry.pack(pady=5)

save_button = tk.Button(app, text="Exit", command=exit_plan, padx=30, bg="teal",font="bold",fg="#f1f1f1")
save_button.pack(pady=10)

# load the flashcards from a file
def load_flashcards():
    try:
        with open("flashcards.json", "r") as f:
            flashcards.update(json.load(f))
    except FileNotFoundError:
        pass

# save the flashcards to a file
def save_flashcards():
    with open("flashcards.json", "w") as f:
        json.dump(flashcards, f)

# initialize the flashcards dictionary
flashcards = {}
current_question = None
load_flashcards()

# start the tkinter app
app.mainloop()
