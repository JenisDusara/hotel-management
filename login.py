from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from customer import Cust_Win
import mysql.connector
from room import Roombooking
from details import DetailsRoom
from hotel import HotelManagementSystem as hotel


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1552x800+0+0")

        # variable

        self.var_email = StringVar()
        self.var_pass = StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Jenish\Desktop\hotel-management\image\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Statrted",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtpass.place(x=40, y=250, width=270)


        # ==================Icon Images==

        img2 = Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)


        img3 = Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\lock-512.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        # ===login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register button
        registernbtn = Button(frame, command=self.register_window,text="New User register", font=("times new roman", 10, "bold"), borderwidth=0,fg="white",
                          bg="black", activeforeground="white", activebackground="black")
        registernbtn.place(x=15, y=350, width=160)

        # forgotpassword

        registerbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 10, "bold"),borderwidth=0, fg="white",
                          bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="jenis" and self.txtpass.get()=="1702":
            messagebox.showinfo("Success","Welcome ")
            self.new_window=Toplevel(self.root)
            self.app=hotel(self.new_window)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNO", "Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=hotel(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            # ================reset password==========
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","select the security Question ",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="mydata")
            my_cursor = conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset , please login new password",parent=self.root2)
                self.root2.destroy()



            # ==========forgot password

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="mydata")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error", "Please Enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",12,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("time new roman", 15, "bold"),
                                   bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=("time new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["value"] = ("select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("Contact No", 15,))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("Contact No", 15,))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("Contact No", 15,),fg="white",bg="green")
                btn.place(x=100,y=290)

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        # ================variable===
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=StringVar()



        #====================== bg image============
        self.bg=ImageTk.PhotoImage(file=r".\image\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #==================== left image=======
        self.bg1 = ImageTk.PhotoImage(
            file=r".\image\2525.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
        #======= main Frame======
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #==============labels and entry===========
        # =-=====================row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        #= =========================row2

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15,))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_email, font=("Contact No", 15,))
        self.txt_contact.place(x=370, y=200, width=250)

        #===========row 3

        security_Q=Label(frame,text="Select Security Question",font=("time new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("time new roman",15,"bold"),state="readonly")
        self.combo_security_Q["value"]=("select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA, font=("Contact No", 15,))
        self.txt_security.place(x=370, y=270, width=250)

        #=========rows4
        pswd=Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass,font=("Contact No", 15,))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("Contact No", 15,))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)


        #==================checkbutton-==========
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition", font=("Contact No", 12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # ===============button

        img=Image.open(r".\image\register-now-button1.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1 = Image.open(r".\image\loginpng.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)

        # ================function declaration===
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Conform Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="4744", database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exist , please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfull")

    def return_login(self):
        self.root.destroy()

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("150x880+0+0")

# ====================== first img=========
        img1=Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\hotel1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

# ===============logo ============
        img2 = Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\logohotel.png")
        img2=img2.resize((1550,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        img2=img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)


#===============title==============
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("title new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)


        #=================main fram==
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #=============menu==============
        lbl_menu = Label(main_frame,text="MENU", font=("title new roman", 20, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # =============btn fram==============
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("time new roman", 14, "bold"), bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking,width=22, font=("time new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0,pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22,command=self.detailsroom, font=("time new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0,pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("time new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("time new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0,pady=1)


        #=============right side imag=========
        img3 = Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\0002.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1310, height=590)

        #===========down images-===============
        img4 = Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\myh.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\Jenish\Desktop\hotel-management\image\khana.jpg           ")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def detailsroom(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)





if __name__=="__main__":
    main()
