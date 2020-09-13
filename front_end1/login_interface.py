from tkinter import*
from front_end1.interface_window import*
from tkinter import ttk
from tkinter import messagebox
from back_end1.register_connection import*
class Login:
    def __init__(self,screen):
        self.wn=screen
        self.wn.geometry("1470x830+60+0")
        self.wn.title("Login window".center(400))
        self.wn.configure(background="#2C3E4C")
        self.wn.resizable(0,0)
        self.con_login=register_database()

        #======frame=====
        self.frame2 = Frame(self.wn, bg="#2C3E4C")
        self.frame2.place(x=10, y=50, width=530, height=440)
        #=======image=======
        self.canvas5 = Canvas(self.wn, width=1470, height=830)
        self.canvas5.place(x=544, y=70)
        self.photo = PhotoImage(file="C:\\Users\\user\\PycharmProjects\\final _database1_assignment\\images\\mcgill-university.png")
        self.canvas5.create_image(0, 0, image=self.photo, anchor=NW)
        self.uni=Label(self.wn,text="University",font=("times new roman",30,"bold"),bg="#2C3E4C",fg="yellow")
        self.uni.place(x=900,y=20)
        #=====label=====
        self.lbl1=Label(self.frame2,text="Login Here",font=("impact",35,"bold"),bg="#2C3E4C",fg="#d77337").place(x=40,y=10)
        self.lbl2 =Label(self.frame2, text="Admin Login Area", font=("Goudy old style", 15, "bold"), bg="#2C3E4C", fg="#d25d17").place(
            x=40, y=70)
        #=======username=====
        self.username1 = Label(self.frame2, text="Username", font=("Goudy old style", 20, "bold"), bg="#2C3E4C", fg="#d77337").place(
            x=210, y=110)
        self.ent_username1 = Entry(self.frame2, font=("times new roman", 15), bg="lightgray")
        self.ent_username1.place(x=180, y=150,width=200)


        #=======password=====
        self.password1 = Label(self.frame2, text="Password", font=("Goudy old style", 20, "bold"), bg="#2C3E4C",
                               fg="#d77337").place(
            x=210, y=200)
        self.ent_password1 = Entry(self.frame2, font=("times new roman", 15), bg="lightgray",show="*")
        self.ent_password1.place(x=180, y=240,width=200)
        #=====button========
        self.btn_login=Button(self.wn,text="Login",font=("times new roman",20),fg="white",bg="#d77337",bd=0,cursor="hand2",
                              command=self.login_click).place(x=220,y=320,width=150,height=40)
        #=====forget password====
        self.btn_forget = Button(self.frame2, text="Forget Password ?", font=("Goudy old style", 20, "bold"), fg="#d77337",
                                bg="#2C3E4C", bd=0, cursor="hand2",command=self.forget_window).place(x=190, y=350)

        #========forget window========
    def reset_password(self):
        if self.combox1.get()=="" or self.ent_answer1.get()=="" or self.ent_newpass.get()=="":
            messagebox.showerror("error","All fields are required ",parent=self.root)
        else:
            try:
                query5="select * from tbl_register where Username=%s and Security_question=%s and Answer=%s;"
                value=self.ent_username1.get(),self.combox1.get(),self.ent_answer1.get()
                row=self.con_login.select(query5,value)

                if row==None:
                    messagebox.showerror("error","please enter the correct security question and qnswer",parent=self.root)
                else:
                    query6="update tbl_register set Password=%s where Username=%s;"
                    value=self.ent_newpass.get(),self.ent_username1.get()
                    self.con_login.update(query6,value)
                    messagebox.showinfo("success","your password has been changed",parent=self.root)
                    self.root.withdraw()
            except Exception as es:
                messagebox.showerror("error",f"error due to {str(es)}")

    def forget_window(self):
        if self.ent_username1.get()=="":
            messagebox.showerror("Error","please enter the username to reset your password")

        else:
            username=self.ent_username1.get()
            query3="select * from tbl_register where Username=%s;"
            value=(username,)
            row=self.con_login.select(query3,value)
            if row==None:
                messagebox.showerror("Error", "please enter the valid username to reset your password")
            else:
                self.root=Toplevel()
                self.root.title("Password Reset window".center(70))
                self.root.geometry("400x400+100+400")
                self.root.focus_force()
                self.root.configure(background="teal")

                # ========security question======
                self.security1 = Label(self.root, text="Security Question", font=("times new roman", 18, "bold"), bg="teal",
                                      fg="black").place(x=110, y=30)

                self.combox1 = ttk.Combobox(self.root, font=("times new roman", 15))
                self.combox1['values'] = ("Select", "Your Favourite pet name", "Your birth place", "Your best friend name")
                self.combox1.place(x=110, y=70, width=170)

                # ==========Answer=======
                self.answer1 = Label(self.root, text="Answer", font=("times new roman", 18, "bold"),bg="teal",
                                    fg="black").place(x=140, y=175)
                self.ent_answer1 = Entry(self.root, font=("times new roman", 15), bg="lightgray")

                self.ent_answer1.place(x=110, y=205, width=170)
                # ==========new password=======
                self.newpass = Label(self.root, text="New Password", font=("times new roman", 18, "bold"), bg="teal",
                                     fg="black").place(x=120, y=250)
                self.ent_newpass = Entry(self.root, font=("times new roman", 15), bg="lightgray",show="*")
                self.ent_newpass.place(x=110, y=280,width=170)
                #========button of reset password==
                self.btn_resetpassword = Button(self.root, text="Reset Password", font=("times new roman", 20), fg="white", bg="#d77337",
                                        bd=5,cursor="hand2",command=self.reset_password).place(x=110, y=330, width=180, height=40)



    def login_click(self):


        if self.ent_username1.get()=="" or self.ent_password1.get()=="":
            messagebox.showerror("Error","please enter username and password",parent=self.wn)

        else:
            username=self.ent_username1.get()
            password=self.ent_password1.get()
            query='select * from tbl_register where Username=%s and Password=%s'
            values=(username,password)
            row=self.con_login.select(query,values)


            if row==None:
                messagebox.showerror("error","Invalid username and password",parent=self.wn)

            else:
                messagebox.showinfo("success","congrats login success")
                self.wn.withdraw()
                self.main_window()






    def main_window(self):

        new_window=Toplevel()
        Mainwindow(new_window)

# window=Tk()
# Login(window)
# window.mainloop()