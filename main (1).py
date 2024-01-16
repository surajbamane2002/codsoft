import tkinter as tk

window = tk.Tk()
window.title("To-Do List")

tasks = []


def add_task():
  task = task_entry.get()
  tasks.append(task)
  task_list.insert(tk.END, task)
  task_entry.delete(0, tk.END)


def delete_task():
  if task_list.curselection():
    task = task_list.get(task_list.curselection())
    if task in tasks:
      tasks.remove(task)
      task_list.delete(0)


def complete_task():
  task = task_list.get(task_list.curselection())
  tasks.remove(task)
  task_list.delete(tk.NW)
  task_list.insert(tk.END, task, "completed")


task_entry = tk.Entry(window)
task_entry.pack(side=tk.TOP)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(window)
task_list.pack()

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

complete_button = tk.Button(window,
                            text="Complete Task",
                            command=complete_task)
complete_button.pack()

window.mainloop()
