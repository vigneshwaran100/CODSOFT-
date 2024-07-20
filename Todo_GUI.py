import tkinter as tk

class TodoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.todo_list = []

        # Create frames
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack()
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        # Create input fields
        self.task_entry = tk.Entry(self.input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT)
        self.add_button = tk.Button(self.input_frame, text="Add", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Create list box
        self.list_box = tk.Listbox(self.list_frame, width=40)
        self.list_box.pack(side=tk.LEFT)

        # Create buttons
        self.remove_button = tk.Button(self.button_frame, text="Remove", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT)
        self.replace_button = tk.Button(self.button_frame, text="Replace", command=self.replace_task)
        self.replace_button.pack(side=tk.LEFT)
        self.complete_button = tk.Button(self.button_frame, text="Complete", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT)
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack(side=tk.LEFT)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.append(task)
            self.list_box.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        try:
            index = self.list_box.curselection()[0]
            self.todo_list.pop(index)
            self.list_box.delete(index)
        except:
            pass

    def replace_task(self):
        try:
            index = self.list_box.curselection()[0]
            task = self.task_entry.get()
            if task:
                self.todo_list[index] = task
                self.list_box.delete(index)
                self.list_box.insert(index, task)
                self.task_entry.delete(0, tk.END)
        except:
            pass

    def complete_task(self):
        try:
            index = self.list_box.curselection()[0]
            self.todo_list.pop(index)
            self.list_box.delete(index)
        except:
            pass

root = tk.Tk()
gui = TodoListGUI(root)
root.mainloop()