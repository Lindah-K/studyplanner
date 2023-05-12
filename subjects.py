import tkinter as tk
import subprocess

def open_myplan():
        window.after(500, window.destroy)
        subprocess.Popen(["python","myplan.py"])
    
def exit_myplan():
        window.after(500, window.destroy)
        subprocess.Popen(["python","welcome.py"])

window = tk.Tk()
window.title("StudySmart Study Planner")
window.geometry("500x450")
window.resizable(False, False)
    # window.configure(bg="teal")

label = tk.Label(window, text="My SubjectPlan:", font=("Arial",18,"bold"), fg="#f1f1f1", bg="teal",padx=175)
label.pack(pady=20)

frame1 = tk.Frame(window, padx=10, pady=10)
frame2 = tk.Frame(window, padx=10, pady=10)
frame3 = tk.Frame(window, padx=10, pady=10)


sub1_label = tk.Label(frame1, text="Subject 1:")
sub1_label.pack(side=tk.LEFT)
sub1_entry = tk.Entry(frame1)
sub1_entry.pack(side=tk.LEFT)

task1_label = tk.Label(frame1, text="   Task:")
task1_label.pack(side=tk.LEFT)
task1_entry = tk.Entry(frame1)
task1_entry.pack(side=tk.LEFT)

time1_label = tk.Label(frame1, text="   DueDate:")
time1_label.pack(side=tk.LEFT)
time1_entry = tk.Entry(frame1)
time1_entry.pack(side=tk.LEFT)

sub2_label = tk.Label(frame2, text="Subject 2:")
sub2_label.pack(side=tk.LEFT)
sub2_entry = tk.Entry(frame2)
sub2_entry.pack(side=tk.LEFT)

task2_label = tk.Label(frame2, text="   Task:")
task2_label.pack(side=tk.LEFT)
task2_entry = tk.Entry(frame2)
task2_entry.pack(side=tk.LEFT)

time2_label = tk.Label(frame2, text="   DueDate:")
time2_label.pack(side=tk.LEFT)
time2_entry = tk.Entry(frame2)
time2_entry.pack(side=tk.LEFT)

sub3_label = tk.Label(frame3, text="Subject 3:")
sub3_label.pack(side=tk.LEFT)
sub3_entry = tk.Entry(frame3)
sub3_entry.pack(side=tk.LEFT)

task3_label = tk.Label(frame3, text="   Task:")
task3_label.pack(side=tk.LEFT)
task3_entry = tk.Entry(frame3)
task3_entry.pack(side=tk.LEFT)

time3_label = tk.Label(frame3, text="   DueDate:")
time3_label.pack(side=tk.LEFT)
time3_entry = tk.Entry(frame3)
time3_entry.pack(side=tk.LEFT)

frame1.pack()
frame2.pack()
frame3.pack()

def save_planner():
        subject1 = sub1_entry.get()
        subject2 = sub2_entry.get()
        subject3 = sub3_entry.get()

        task1 = task1_entry.get()
        task2 = task2_entry.get()
        task3 = task3_entry.get()
        
        time1 = time1_entry.get()
        time2 = time2_entry.get()
        time3 = time3_entry.get()

        if not subject1 and not subject2 and not subject3:
            success_label.config(text="Add atleast one subjects!", fg="red", font="10")

        elif subject1 or not task1 or not time1:
            success_label.config(text="Fill in task and due date for the subjects added", fg="red", font="10")

            if subject1 and task1 and time1:
                success_label.config(text="StudyPlan Successfully Saved", fg="teal")
                
                with open("subjects.txt", "a") as f:
                #     f.write(f"{subject1}, {task1}, {time1} \n")
                    f.write(f"{subject1}, {task1}, {time1} \n")
                sub1_entry.delete(0, tk.END)
                task1_entry.delete(0, tk.END)
                time1_entry.delete(0, tk.END)

                if subject2 or not task2 or not time2:
                    success_label.config(text="Fill in task and due date for the subjects added", fg="red")

                    if subject2 and task2 and time2:
                        success_label.config(text="StudyPlan Successfully Saved", fg="teal")
                        with open("subjects.txt", "a") as f:
                        #     f.write(f"{subject2}, {task2}, {time2} \n")
                            f.write(f"{subject2}, {task2}, {time2} \n")
                        sub2_entry.delete(0, tk.END)
                        task2_entry.delete(0, tk.END)
                        time2_entry.delete(0, tk.END)
                        
                        if subject3 or not task3 or not time3:
                            success_label.config(text="Fill in task and due date for the subjects added", fg="red")

                            if subject3 and task3 and time3:
                                success_label.config(text="StudyPlan Successfully Saved", fg="teal")
                                with open("subjects.txt", "a") as f:        
                                    f.write(f"{subject1}, {task1}, {time1} \n")
                                    f.write(f"{subject2}, {task2}, {time2} \n")
                                    f.write(f"{subject3}, {task3}, {time3} \n")
                                sub1_entry.delete(0, tk.END)
                                sub2_entry.delete(0, tk.END)
                                sub3_entry.delete(0, tk.END)
                                task1_entry.delete(0, tk.END)
                                task2_entry.delete(0, tk.END)
                                task3_entry.delete(0, tk.END)
                                time1_entry.delete(0, tk.END)
                                time2_entry.delete(0, tk.END)
                                time3_entry.delete(0, tk.END)

        
        else:
            success_label.config(text="StudyPlan Successfully Saved", fg="teal")

            with open("subjects.txt", "a") as f:
                f.write(f"{subject1}, {subject2}, {subject3} \n")

            success_label.config(text="StudyPlan Successfully Saved", fg="teal")
            
   
save_button = tk.Button(window, text="Save Planner", command=save_planner, padx=22, bg="teal", fg="#f1f1f1", font="bold")
save_button.pack(pady=10)
    
save_button = tk.Button(window, text="View SubjectPlan", command=open_myplan, padx=6, bg="teal", fg="#f1f1f1", font="bold")
save_button.pack(pady=10)

save_button = tk.Button(window, text="Exit", command=exit_myplan, padx=67, bg="teal", fg="#f1f1f1", font="bold")
save_button.pack(pady=10)

text_label = tk.Label(window, text="working hard is hard, but not impossible", font=("Arial",8,"italic"), fg="teal", pady=5)

success_label = tk.Label(window, text="")
success_label.pack(pady=5)

window.mainloop()