from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime  #pip install datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        # variable
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # ===================title=============
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("arial", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =======================logo=============
        img2 = Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # ==============label frame============
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details",
                                    font=("arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ================label and entry==================
        # cust ref
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        ent_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))

        ent_contact.grid(row=0, column=1, sticky=W)

        # fetch data butto
        btnfetchData = Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"),bg="black",fg="gold", width=8)
        btnfetchData.place(x=347, y=4)

        # =============check in date==========
        check_in_date = Label(labelframeleft, text="Check_in Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, width=29,
                                     font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)

        # =============check out date==========
        check_in_out = Label(labelframeleft, text="Check_out Date:", font=("arial", 12, "bold"), padx=2,pady=6)
        check_in_out.grid(row=2, column=0)

        txtcheck_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, width=29, font=("arial", 13, "bold"))
        txtcheck_out.grid(row=2, column=1)

        # ========Room Type==========
        label_RoomType = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="managemant")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=27,state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # =====available room===========
        lblRoomAvilable = Label(labelframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblRoomAvilable.grid(row=4, column=0, sticky=W)

       # txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, width=29,font=("arial", 13, "bold"))
        #txtRoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="managemant")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"),
                                      width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)


        # meal
        lblMeal = Label(labelframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, width=29, font=("arial", 13, "bold"))
        txtMeal.grid(row=5, column=1)

        # no of days
        lblNoOfDays = Label(labelframeleft, text="No of Days:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, width=29, font=("arial", 13, "bold"))

        txtNoOfDays.grid(row=6, column=1)

        # paid Tax
        lblNoOfDays = Label(labelframeleft, text="Paid Tax:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, width=29, font=("arial", 13, "bold"))
        txtNoOfDays.grid(row=7, column=1)

        # sub total
        lblNoOfDays = Label(labelframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, width=29, font=("arial", 13, "bold"))
        txtNoOfDays.grid(row=8, column=1)

        # total cost
        lblIdNumber = Label(labelframeleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_total, width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # bill button
        btnBill = Button(labelframeleft, text="Bill", command=self.total,font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # button
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data,font=("arial", 12, "bold"), bg="black",fg="gold", width=8)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpadate = Button(btn_frame, text="Update", command=self.update,font=("arial", 12, "bold"), bg="black", fg="gold",width=10)
        btnUpadate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete,font=("arial", 12, "bold"), bg="black", fg="gold",width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset,font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # right images
        img3 = Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\Room111.jpg")
        img3 = img3.resize((520, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

        # table fram search
        Tabel_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                 font=("arial", 12, "bold"), padx=2)
        Tabel_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Tabel_Frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=00, column=0, sticky=W)

        self.search_var = StringVar()
        combo_Serach = ttk.Combobox(Tabel_Frame, textvariable = self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")

        combo_Serach["value"] = ("Contact", "Room")
        combo_Serach.current(0)
        combo_Serach.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        txtSearch = ttk.Entry(Tabel_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Tabel_Frame, command=self.search,text="Search", font=("arial", 12, "bold"), bg="black", fg="gold", width=8)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Tabel_Frame,command=self.fetch_data, text="Show All", font=("arial", 12, "bold"), bg="black", fg="gold", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)

        # show data table
        deatils_table = Frame(Tabel_Frame, bd=2, relief=RIDGE)
        deatils_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(deatils_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(deatils_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(deatils_table, columns=(
            "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)

        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
                messagebox.showerror("Error", "All fields are requaired", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="4744",
                                               database="managemant")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"some thing went wrong:{str(es)}", parent=self.root)
#fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="managemant")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cuersor(self, event=""):
        cusrsor_row = self.room_table.focus()
        content = self.room_table.item(cusrsor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

        #updates
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="4744",
                                               database="managemant")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,room=%s,meal=%s,noOfdays=%s where Contact=%s",
                    (
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get(),
                        self.var_contact.get()

                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room Details has been updated successfully", parent=self.root)


        #delet
    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want delete this customer",
                                          parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="4744",
                                               database="managemant")
            my_cursor = conn.cursor()
            query = "delete from room where Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

        #reset
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        #self.var_roomtype.set("")
        self.var_roomavailable.set('')
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

        # function
        # all data fetch
    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please Enter Contact Number")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="managemant")
            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                conn = mysql.connector.connect(host="localhost", username="root", password="4744",
                                               database="managemant")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                #======email=====
                conn = mysql.connector.connect(host="localhost", username="root", password="4744",
                                               database="managemant")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=60)

                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=60)

                #=====NAtionality===
                conn = mysql.connector.connect(host="localhost", username="root", password="4744",
                                               database="managemant")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=90)

                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=90)

                #============Address
                conn = mysql.connector.connect(host="localhost", username="root", password="4744",
                                               database="managemant")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=120)

                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=120)

    #search system
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="managemant")
        my_cursor = conn.cursor()

        search_value = '%' + str(self.txt_search.get()) + '%'
        query = "SELECT * FROM room WHERE {} LIKE %s".format(self.search_var.get())
        my_cursor.execute(query, (search_value,))
        # my_cursor.execute("select * from room where"+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="laxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif  (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(100)
            q2=float(300)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.9))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "laxary"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Duplex"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.9)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)








if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
