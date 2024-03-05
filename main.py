import tkinter as tk
from tkinter import messagebox

tasks = []

screen = tk.Tk()
screen.title('TO DO LIST')
screen.geometry("600x400")

def addTask():
    selectTask = taskEntry.get()
    if selectTask:
        tasks.append(selectTask)
        tasklist.insert(tk.END, selectTask)
        taskEntry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning!", "Enter a task.")

def deleteTask():
    try:
        chosentask = tasklist.curselection()[0]
        tasklist.delete(chosentask)
        del tasks[chosentask]
    except IndexError:
        messagebox.showwarning("Warning!", "Select the task you wish to delete.")

def deleteAll():
    tasklist.delete(0, tk.END)
    tasks.clear()

taskEntry = tk.Entry(screen, width=40)
taskEntry.grid()    

add = tk.Button(screen, text="Add", command = addTask, bg= "green")
add.grid()

delete = tk.Button(screen, text="Delete", command= deleteTask, bg= "red")
delete.grid()

deleteAll = tk.Button(screen, text = "Clear", command = deleteAll, bg = "grey")
deleteAll.grid()

tasklist = tk.Listbox(screen, width=50)
tasklist.grid()

screen.mainloop()
