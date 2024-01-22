from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Feedback:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("850x300+380+290")



        # Create frames for grid and pack layout managers
        frame_grid = ttk.Frame(root)
        frame_grid.pack()

        frame_pack = ttk.Frame(root)
        frame_pack.pack()

        # variable
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_comment = StringVar()

        # header
        headerlabel = ttk.Label(frame_grid, text='CUSTOMER FEEDBACK', foreground='orange',
                                font=('Arial', 24))
        headerlabel.grid(row=0, column=0, columnspan=2, pady=10)  # Added pady to create space

        messagelabel = ttk.Label(frame_grid,
                                 text='PLEASE TELL US WHAT YOU THINK',
                                 foreground='purple', font=('Arial', 10))
        messagelabel.grid(row=1, column=0, columnspan=2)

        # labels
        namelabel = ttk.Label(frame_grid, text='Name')
        namelabel.grid(row=2, column=0, padx=5, sticky='sw')
        entry_name = ttk.Entry(frame_grid, width=18, font=('Arial', 14), textvariable=self.var_name)
        entry_name.grid(row=3, column=0)

        emaillabel = ttk.Label(frame_grid, text='Email')
        emaillabel.grid(row=2, column=1, sticky='sw')
        entry_email = ttk.Entry(frame_grid, width=18, font=('Arial', 14), textvariable=self.var_email)
        entry_email.grid(row=3, column=1)

        commentlabel = ttk.Label(frame_pack, text='Comment', font=('Arial', 10))
        commentlabel.grid(row=0, column=0, sticky='w', padx=5, pady=5)  # Added padx and pady

        textcomment = ttk.Entry(frame_pack, width=55, textvariable=self.var_comment)
        textcomment.grid(row=1, column=0, padx=5, pady=5)  # Added padx and pady

        submitframe = ttk.Frame(frame_pack)
        submitframe.grid(row=2, column=0, padx=5, pady=5)  # Added padx and pady

        submitbutton = ttk.Button(submitframe, text='Submit', command=self.submit)
        submitbutton.pack(side='left', padx=10)  # Adjusted button layout
        clearbutton = ttk.Button(submitframe, text='Clear', command=self.clear)
        clearbutton.pack(side='left', padx=10)  # Adjusted button layout

    def clear(self):
        self.var_name.set("")
        self.var_email.set("")
        self.var_comment.set("")

    def submit(self):
        if self.var_name.get() == "" or self.var_email.get() == "" or self.var_comment.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="4744",
                                               database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into feedback values(%s,%s,%s)", (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_comment.get(),
                ))
                conn.commit()
                conn.close()

                messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submitted',parent=self.root)
                self.clear()

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Feedback(root)
    root.mainloop()
