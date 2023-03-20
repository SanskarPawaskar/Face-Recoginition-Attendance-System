from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import mysql.connector
from main import Face_Recognization_System

def main():
    win=Tk()
    app=Login_Page(win)
    win.mainloop()



class Login_Page:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1440x780+0+0")

       #============== Placing Background Image===============

        img = Image.open(os.path.join("Images/login_page_frame.png"))
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0,width=1440,height=780)

        #============= Username Entrybox ===============

        self.username=ttk.Entry(bg_img,font=("times new roman",20,"bold"))
        self.username.place(x=292,y=256,width=427,height=55)

         #============= Password Entrybox ===============

        self.password=ttk.Entry(bg_img,font=("times new roman",20,"bold"),show="*")
        self.password.place(x=292,y=374,width=427,height=55)

        #================= Login Button ===================
        img1 = Image.open(os.path.join("Images/login_btn.png"))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(bg_img,image=self.photoimg1,command=lambda:[self.login(),self.clear_text_1(),self.clear_text_2()],cursor="hand2")
        b1.place(x=398,y=474,width=216,height=67)

        #================= New User Button ===================
        img2 = Image.open(os.path.join("Images/new_user_btn.png"))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(bg_img,command=self.register_window,image=self.photoimg2,cursor="hand2")
        b1.place(x=218,y=586,width=287,height=77.5)

        #================= Forgot Password Button ===================
        img3 = Image.open(os.path.join("Images/forgot_password_btn.png"))
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(bg_img,command=self.forgot_password,image=self.photoimg3,cursor="hand2")
        b1.place(x=523,y=586,width=287,height=77.5)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Registration(self.new_window)
    
    def clear_text_1(self):
        self.username.delete(0, 'end')

    def clear_text_2(self):
        self.password.delete(0, 'end')


    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields Required")
        elif self.username.get()=="sanskar" and self.password.get()=="pawaskar":
            messagebox.showinfo("Success","You have successfully Logged In")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanskar21",database="MyData")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                            self.username.get(),
                                            self.password.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("Verification","Access only Admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognization_System(self.new_window)
                        
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

#================== Reset Password Function =========================
    def reset_password(self):
        if self.security_question.get()=="Select a Question":
            messagebox.showerror("Error","Select a Question",parent=self.root2)
        elif self.security_answer.get()=="":
            messagebox.showerror("Error","Enter an Answer",parent=self.root2)
        elif self.new_password.get()=="":
            messagebox.showerror("Error","Enter new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanskar21",database="MyData")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityquestion=%s and securityanswer=%s")
            value=(self.username.get(),self.security_question.get(),self.security_answer.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_password.get(),self.username.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your Password has been Reset Please login with new Password",parent=self.root2)
                self.root2.destroy()






#================= Forgot Password Window ============================
    def forgot_password(self):
        if self.username.get()=="":
            messagebox.showerror("Error","Please Enter Username to reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanskar21",database="MyData")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Enter a Valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("643x633+186+105")
                fp_img = Image.open(os.path.join("Images/forgot_password_frame.png"))
                self.photoimg_fp=ImageTk.PhotoImage(fp_img)
                fp_img=Label(self.root2,image=self.photoimg_fp)
                fp_img.place(x=0,y=0,width=643,height=633)

                #============= Security Question Combo Box ===============

                self.security_question=ttk.Combobox(fp_img,font=("times new roman",20,"bold"),state="readonly")
                self.security_question.place(x=106,y=177,width=427,height=55)
                self.security_question["values"]=("Select a Question","Your Grandfathers Name","Your Favourite Sport","Your Birth Place")
                self.security_question.current(0)

                #============= Security Answer Entrybox ===============

                self.security_answer=ttk.Entry(fp_img,font=("times new roman",20,"bold"))
                self.security_answer.place(x=106,y=295,width=427,height=55)

                #============= New Password Entrybox ===============

                self.new_password=ttk.Entry(fp_img,font=("times new roman",20,"bold"))
                self.new_password.place(x=106,y=413,width=427,height=55)

                #================== Reset Password Button ===================

                reset_pass_btn = Image.open(os.path.join("Images/reset_password_btn.png"))
                self.photoimg_reset=ImageTk.PhotoImage(reset_pass_btn)
                b1=Button(fp_img,command=self.reset_password,image=self.photoimg_reset,cursor="hand2")
                b1.place(x=121,y=511,width=411,height=75)







                
                             


#================== Register Class=========================
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
        b1=Button(bg_img,command=self.login_return,image=self.photoimg2,cursor="hand2",fg="white")
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
    
    def login_return(self):
        self.root.destroy()



if __name__ =="__main__":
    main()
  

