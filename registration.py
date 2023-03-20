from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import mysql.connector

class Registration:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1440x780+0+0")

        #================= Variables=========================

        self.var_firstname=StringVar()
        self.var_lastname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_question=StringVar()
        self.var_security_answer=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()
        self.var_check_button=IntVar()
    
        #============ Place Background Image==================

        img = Image.open(os.path.join("Images/registration_frame.png"))
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0,width=1440,height=780)


        #============= First name Entrybox ===============

        self.firstname=ttk.Entry(bg_img,textvariable=self.var_firstname,font=("times new roman",20,"bold"))
        self.firstname.place(x=555,y=211,width=368,height=43)

        #============= Last name Entrybox ===============

        self.lastname=ttk.Entry(bg_img,textvariable=self.var_lastname,font=("times new roman",20,"bold"))
        self.lastname.place(x=980,y=211,width=368,height=43)

        #============= Contact No Entrybox ===============

        self.contact=ttk.Entry(bg_img,textvariable=self.var_contact,font=("times new roman",20,"bold"))
        self.contact.place(x=555,y=316,width=368,height=43)

        #============= Email Entrybox ===============

        self.email=ttk.Entry(bg_img,textvariable=self.var_email,font=("times new roman",20,"bold"))
        self.email.place(x=980,y=316,width=368,height=43)

        #============= Security Question Combo Box ===============

        self.security_question=ttk.Combobox(bg_img,textvariable=self.var_security_question,font=("times new roman",20,"bold"),state="readonly")
        self.security_question.place(x=555,y=420,width=368,height=43)
        self.security_question["values"]=("Select a Question","Your Grandfathers Name","Your Favourite Sport","Your Birth Place")
        self.security_question.current(0)

        #============= Security Answer Entrybox ===============

        self.security_answer=ttk.Entry(bg_img,textvariable=self.var_security_answer,font=("times new roman",20,"bold"))
        self.security_answer.place(x=980,y=420,width=368,height=43)

        #============= Password Entrybox ===============

        self.password=ttk.Entry(bg_img,textvariable=self.var_password,font=("times new roman",20,"bold"))
        self.password.place(x=555,y=525,width=368,height=43)

        #============= Confirm Password Entrybox ===============

        self.confirm_password=ttk.Entry(bg_img,textvariable=self.var_confirm_password,font=("times new roman",20,"bold"))
        self.confirm_password.place(x=980,y=525,width=368,height=43)

        #============== Check Button =================
        checkbtn=Checkbutton(bg_img,variable=self.var_check_button,text="I Agree to the terms and condition",font=("times new roman",20,"bold"),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=555,y=589)

        #================== Register Button ==============
        img1 = Image.open(os.path.join("Images/register_btn.png"))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(bg_img,image=self.photoimg1,command=self.register_data,cursor="hand2")
        b1.place(x=587,y=639,width=293,height=64)

        #================== Login Button ==============
        img2 = Image.open(os.path.join("Images/login_btn_2.png"))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(bg_img,image=self.photoimg2,cursor="hand2",fg="white")
        b1.place(x=1015,y=639,width=293,height=64)







#================= Function Declaration ======================
    def register_data(self):
        if self.var_firstname.get()=="" or self.var_lastname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_security_question.get()=="Select a Question" or self.var_security_answer.get()=="" or self.var_password.get()=="" or self.var_confirm_password.get()=="" :
            messagebox.showerror("Error","All Fields are Required")
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Password did not Match")
        elif self.var_check_button.get()==0:
            messagebox.showerror("Error","Terms and Condition not Agreed")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanskar21",database="MyData")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User alerady exists, use different email")
            else:
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_firstname.get(),
                    self.var_lastname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_question.get(),
                    self.var_security_answer.get(),
                    self.var_password.get(),
                
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registerd Successfully")
        







if __name__ == "__main__":
    root=Tk()
    app=Registration(root)
    root.mainloop()
