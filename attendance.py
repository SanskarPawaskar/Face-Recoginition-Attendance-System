from logging import root
import re
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x780+0+0")
        self.root.title("Attendance")

#============== Variables ===============================
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_status=StringVar()

    
#=============== Placing Background Frame =======================
        img = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/attendance_management_frame.png"))
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0,width=1440,height=780)

#============== Student Id Entry Box ======================
        self.student_id=ttk.Entry(bg_img,textvariable=self.var_attend_id,font=("times new roman",20,"bold"))
        self.student_id.place(x=175,y=306,width=154,height=25)

#============== Roll No Entry Box ======================
        self.roll_no=ttk.Entry(bg_img,textvariable=self.var_attend_roll,font=("times new roman",20,"bold"))
        self.roll_no.place(x=443,y=306,width=154,height=25)

#============== Student Name Entry Box ======================
        self.student_name=ttk.Entry(bg_img,textvariable=self.var_attend_name,font=("times new roman",20,"bold"))
        self.student_name.place(x=175,y=358,width=154,height=25)

#============== Student Department Entry Box ======================
        self.department=ttk.Entry(bg_img,textvariable=self.var_attend_dep,font=("times new roman",20,"bold"))
        self.department.place(x=443,y=360,width=154,height=25)

#============== Time Entry Box ======================
        self.time=ttk.Entry(bg_img,textvariable=self.var_attend_time,font=("times new roman",20,"bold"))
        self.time.place(x=175,y=413,width=154,height=25)

#============== Date Entry Box ======================
        self.date=ttk.Entry(bg_img,textvariable=self.var_attend_date,font=("times new roman",20,"bold"))
        self.date.place(x=443,y=413,width=154,height=25)

#============== Status Entry Box ======================

        self.status=ttk.Combobox(bg_img,textvariable=self.var_attend_status,font=("times new roman",20,"bold"),state="readonly")
        self.status.place(x=336,y=476,width=154,height=25)
        self.status["values"]=("Select Status","Present","Absent")
        self.status.current(0)
        
#================ Import Csv Button =========================
        img1 = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/import_csv_btn.png"))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(bg_img,command=self.import_csv,image=self.photoimg1,cursor="hand2")
        b1.place(x=89,y=564,width=492,height=38)

#================ Export Csv Button =========================
        img2 = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/export_csv_btn.png"))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(bg_img,command=self.export_csv,image=self.photoimg2,cursor="hand2")
        b1.place(x=89,y=615,width=492,height=38)

#================ Update Button =========================
        #img3 = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/update_btn_2.png"))
       # self.photoimg3=ImageTk.PhotoImage(img3)
      #  b1=Button(bg_img,image=self.photoimg3,cursor="hand2")
        #b1.place(x=70,y=653,width=240,height=38)

#================ Reset Button =========================
        img4 = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/reset_btn_2.png"))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,command=self.reset_data,image=self.photoimg4,cursor="hand2")
        b1.place(x=89,y=672,width=492,height=38)

#================ Student Details Frame ===========================
        student_details_frame =LabelFrame(bg_img,bd=3,relief=RIDGE,bg="white")
        student_details_frame.place(x=675,y=264,width=688,height=435)

#================== Scroll Bar===============================
        scroll_x=ttk.Scrollbar(student_details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(student_details_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(student_details_frame,columns=("id","roll","name","department","time","date","status"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("status",text="Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("status",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

#================ Fetch Data / Import CSV Function ================================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSC",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

#================ Export Function ===================================

    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSC",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data has been exported to "+os.path.basename(fln)+"Successfully")
                file_csv = open("attendance.csv", "w")
                file_csv.truncate()
                file_csv.close()
        except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)    

    def get_cursor(self,event=""):
        cursor_row= self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_status.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_status.set("Select Status")





if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()