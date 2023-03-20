from logging import root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os, sys, subprocess
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x780+0+0")
        self.root.title("Facial Recognization")

#==============Placing Background Image=======================
        img = Image.open(os.path.join("Images/student_mgm_frame.png"))
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0,width=1440,height=780)

#=============== Student Registration Button =====================
        img1 = Image.open(os.path.join("Images/std_reg_btn.png"))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=46,y=462,width=216,height=53)

#=============== Attendance Button =====================
        img2 = Image.open(os.path.join("Images/attendance_btn.png"))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(bg_img,command=self.attendance_data,image=self.photoimg2,cursor="hand2")
        b1.place(x=326,y=462,width=216,height=53)

#=============== Photos Button =====================
        img3 = Image.open(os.path.join("Images/photos_btn.png"))
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(bg_img,command=self.open_img,image=self.photoimg3,cursor="hand2")
        b1.place(x=609,y=462,width=216,height=53)

#=============== Train Dataset Button =====================
        img4 = Image.open(os.path.join("Images/train_dataset_btn.png"))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,command=self.train_data,image=self.photoimg4,cursor="hand2")
        b1.place(x=894,y=462,width=216,height=53)

#=============== Mark Attendance Button =====================
        img5 = Image.open(os.path.join("Images/mark_attendance_btn.png"))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,command=self.face_data,image=self.photoimg5,cursor="hand2")
        b1.place(x=1169,y=462,width=216,height=53)

#=============== Exit Button =====================
        img6 = Image.open(os.path.join("Images/exit_btn.png"))
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,command=self.root.destroy,image=self.photoimg6,cursor="hand2")
        b1.place(x=595,y=636,width=245,height=60)


#================== Functions =====================

    def open_img(self):
        subprocess.Popen(["open", 'data'])
    


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)




    

















if __name__== "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()