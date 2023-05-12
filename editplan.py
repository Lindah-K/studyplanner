import tkinter as tk
import subprocess

# Create a tkinter window
root = tk.Tk()
root.title("StudyPlan Editor")
# root.geometry("500x380")
root.resizable(False, False)
# root.configure(bg="teal")

label = tk.Label(root, text="Delete done tasks and save changes:", font=("Arial",14,"bold"), fg="#f1f1f1", bg="teal",padx=175)
label.pack(pady=10)

# Create a text widget for displaying the file content
text_widget = tk.Text(root)
text_widget.pack()

# Create a scrollbar for the text widget
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

# Open the file and read its content
filename = "subjects.txt"
with open(filename, "r") as file:
    file_content = file.read()

# Insert the file content into the text widget
text_widget.insert(tk.END, file_content)

# Create a delete button for each entry
delete_buttons = []
lines = file_content.split("\n")
for i, line in enumerate(lines):
    button = tk.Button(root, text="Delete", command=lambda i=i: delete_line(i))
    button.pack(pady=5)
    delete_buttons.append(button)

def delete_line(line_index):
    # Delete the line from the text widget
    text_widget.delete(f"{line_index+1}.0", f"{line_index+2}.0")
    
    # Delete the corresponding delete button
    delete_buttons[line_index].pack_forget()
    del delete_buttons[line_index]
    
    # Update the line indices of the remaining delete buttons
    for i in range(line_index, len(delete_buttons)):
        delete_buttons[i]["command"] = lambda i=i: delete_line(i)

# Create a save button to save changes to the file
# save_button = tk.Button(root, text="Save", command=save_changes)
# save_button.pack()

def save_changes():
    # Get the updated file content from the text widget
    updated_content = text_widget.get("1.0", tk.END)
    
    # Write the updated content to the file
    with open(filename, "w") as file:
        file.write(updated_content)

    root.after(500, root.destroy)
    subprocess.Popen(["python","myplan.py"])
        
save_button = tk.Button(root, text="Save", command=save_changes,bg="teal", fg="#f1f1f1")
save_button.pack(pady=10)
# Start the tkinter event loop
root.mainloop()
