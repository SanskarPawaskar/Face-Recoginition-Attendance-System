import imp
from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x780+0+0")
        self.root.title("Facial Recognization")

            # ===================Variable==================================================

        self.var_dep= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_sem= StringVar()
        self.var_id= StringVar()
        self.var_name= StringVar()
        self.var_div= StringVar()
        self.var_roll= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_contact= StringVar()
        self.var_address= StringVar()
        self.var_teacher= StringVar()
        self.var_radio1 = StringVar()


        #==============Placing Background Image=======================
        img = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/student_registration_frame.png"))
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0,width=1440,height=780)

        #============== Course Details Left Frame =================
        current_course_frame=LabelFrame(bg_img,bd=10,relief=RIDGE,bg="white",text="Course Information",font=("times new roman",14,"bold"))
        current_course_frame.place(x=40,y=225,width=609,height=95)

        # Department Section
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo= ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",15,"bold"),state="read only",width=18)
        dep_combo["values"]=("Select Department","Computer","IT","Mechanical","Civil","EXTC","Automobile")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)


        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=25,sticky=W)

        course_combo= ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",15,"bold"),state="read only",width=18)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=2,sticky=W)


        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo= ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",15,"bold"),state="read only",width=18)
        year_combo["values"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=12,sticky=W)


        # Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=25,sticky=W)

        sem_combo= ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",15,"bold"),state="read only",width=18)
        sem_combo["values"]=("Select Semester","Semester 1" ,"Semester 2","Semester 3","Semester 4","Semester 5","Semester 6","Semester 7","Semester 8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=5,pady=12,sticky=W)

        #==================Student Class Information Frame================
        Student_class_frame=LabelFrame(bg_img,bd=10,relief=RIDGE,bg="white",text="Class Student Information",font=("times new roman",14,"bold"))
        Student_class_frame.place(x=40,y=325,width=609,height=380)

        # Students ID
        studentId_label=Label(Student_class_frame,text="Student ID:",font=("times new roman",15,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_id,font=("times new roman",15,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        # Student name
        studentName_label=Label(Student_class_frame,text="Student Name:",font=("times new roman",15,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_name,font=("times new roman",15,"bold"))
        studentName_entry.grid(row=0,column=3,padx=0,pady=8,sticky=W)


        # Class Division
        class_div_label=Label(Student_class_frame,text="Division:",font=("times new roman",15,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)

        # class_div_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_div,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=5,pady=8,sticky=W)

        div_combo= ttk.Combobox(Student_class_frame,textvariable=self.var_div,font=("times new roman",15,"bold"),state="read only",width=18)
        div_combo["values"]=("Select Division","Div A","Div B","Div C","Div D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=8,sticky=W)

        # Roll No
        roll_no_label=Label(Student_class_frame,text="Roll No:",font=("times new roman",15,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_no_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_roll,font=("times new roman",15,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=0,pady=8,sticky=W)

        # Gender
        gender_label=Label(Student_class_frame,text="Gender:",font=("times new roman",15,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        # gender_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=5,pady=8,sticky=W)
        gender_combo= ttk.Combobox(Student_class_frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),state="read only",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=8,sticky=W)

        # DOB
        dob_label=Label(Student_class_frame,text="D.O.B:",font=("times new roman",15,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_dob,font=("times new roman",15,"bold"))
        dob_entry.grid(row=2,column=3,padx=0,pady=8,sticky=W)


        # Email
        email_label=Label(Student_class_frame,text="Email:",font=("times new roman",15,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=8,sticky=W)


        # Contact Number
        contact_label=Label(Student_class_frame,text="Contact No:",font=("times new roman",15,"bold"),bg="white")
        contact_label.grid(row=3,column=2,padx=10,sticky=W)

        contact_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.grid(row=3,column=3,padx=0,pady=8,sticky=W)


        # Address
        address_label=Label(Student_class_frame,text="Address:",font=("times new roman",15,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,sticky=W)

        address_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_address,font=("times new roman",15,"bold"))
        address_entry.grid(row=4,column=1,padx=5,pady=8,sticky=W)
        

         # Teacher name
        teacher_label=Label(Student_class_frame,text="Teacher Name:",font=("times new roman",15,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(Student_class_frame,width=20,textvariable=self.var_teacher,font=("times new roman",15,"bold"))
        teacher_entry.grid(row=4,column=3,padx=0,pady=8,sticky=W)


        #Radio Buttons
        radiobtn1=ttk.Radiobutton(Student_class_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=1,pady=4)

        radiobtn2=ttk.Radiobutton(Student_class_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=5,column=3,pady=4)

        #Buttons Frame
        btn_frame =Frame(Student_class_frame,bd=3,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=250,width=582,height=100)

        #=============== Save Button =====================
        save_btn = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/save_btn.png"))
        self.photoimg4=ImageTk.PhotoImage(save_btn)
        b1=Button(btn_frame,command=self.add_data,image=self.photoimg4,cursor="hand2")
        b1.place(x=8,y=12,width=128,height=22)

       #=============== Update Button =====================
        update_btn = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/update_btn.png"))
        self.photoimg5=ImageTk.PhotoImage(update_btn)
        b1=Button(btn_frame,command=self.update_data,image=self.photoimg5,cursor="hand2")
        b1.place(x=152,y=12,width=128,height=22)

        #=============== Delete Button =====================
        delete_btn = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/delete_btn.png"))
        self.photoimg6=ImageTk.PhotoImage(delete_btn)
        b1=Button(btn_frame,command=self.delete_data,image=self.photoimg6,cursor="hand2")
        b1.place(x=296,y=12,width=128,height=22)

        #=============== Reset Button =====================
        reset_btn = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/reset_btn.png"))
        self.photoimg7=ImageTk.PhotoImage(reset_btn)
        b1=Button(btn_frame,command=self.reset_data,image=self.photoimg7,cursor="hand2")
        b1.place(x=440,y=12,width=128,height=22)

         #=============== Take Photo Sample =====================
        take_photp_btn = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/take_photo_sample_btn.png"))
        self.photoimg8=ImageTk.PhotoImage(take_photp_btn)
        b1=Button(btn_frame,command=self.generate_dataset,image=self.photoimg8,cursor="hand2")
        b1.place(x=11,y=44,width=560,height=38)

         #=============== Update Photo Button =====================
        #update_photo_btn = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/update_photo_sample_btn.png"))
        #self.photoimg9=ImageTk.PhotoImage(update_photo_btn)
        #b1=Button(btn_frame,image=self.photoimg9,cursor="hand2")
        #b1.place(x=8,y=66,width=560,height=22)

        #================ Student Details Right Frame==================
        Right_frame=LabelFrame(bg_img,bd=10,relief=GROOVE,bg="white",text="Student Details",font=("times new roman",14,"bold"))
        Right_frame.place(x=700,y=225,width=700,height=480)

        #Search System Frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=0,width=670,height=75)

        # #Serach Option
        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        self.var_search_combo=StringVar()
        search_combo= ttk.Combobox(search_frame,textvariable=self.var_search_combo,font=("times new roman",13,"bold"),state="read only",width=18)
        search_combo["values"]=("Select","Roll_No","Contact","Student_Id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=1,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=1,sticky=W)

        # #Search Button
        #search_btn = Button(search_frame,text="Search",width=11,font=("times new roman",13,"bold"),bg="red",fg="white")
        #search_btn.grid(row=0,column=3,padx=2)

        # #Show All
        #show_all_btn = Button(search_frame,text="Show All",width=11,font=("times new roman",15,"bold"),bg="red",fg="white")
        #show_all_btn.grid(row=0,column=4,padx=2)

        #=============== Search Button =====================
        search_btn = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/search_btn.png"))
        self.photoimg10=ImageTk.PhotoImage(search_btn)
        b1=Button(search_frame,image=self.photoimg10,cursor="hand2",command=self.search_data)
        b1.place(x=411,y=9,width=111,height=22)


         #=============== Show All Button =====================
        show_all_btn = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/show_all_btn.png"))
        self.photoimg11=ImageTk.PhotoImage(show_all_btn)
        b1=Button(search_frame,image=self.photoimg11,cursor="hand2",command=self.fetch_data)
        b1.place(x=540,y=9,width=111,height=22)

        #Table Frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=80,width=670,height=365)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table =ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","contact","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]= "headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
    
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #======================function declaration============================================

        # add dataset 
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sanskar21",database="MyData")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_contact.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                    ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

            #============== Fetch Data =====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sanskar21",database="MyData")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_table")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

         #============ Get cursor================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data =content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_contact.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

#==============Upadate Function ======================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update Student Details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sanskar21",database="Mydata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_table set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,Dob=%s,Email=%s,Contact=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_Id=%s",(
                    # my_cursor.execute("update student_table set Department=%s,Course=%s,Year=%s,Semester=%s,Student_Id=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,Dob=%s,Email=%s,Contact=%s,Address=%s,Teacher=%s,PhotoSample=%s",(
                                                                            self.var_dep.get(),
                                                                            self.var_course.get(),
                                                                            self.var_year.get(),
                                                                            self.var_sem.get(), 
                                                                            self.var_name.get(),
                                                                            self.var_div.get(),
                                                                            self.var_roll.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_dob.get(),
                                                                            self.var_email.get(),
                                                                            self.var_contact.get(),
                                                                            self.var_address.get(),
                                                                            self.var_teacher.get(),
                                                                            self.var_radio1.get(),
                                                                            self.var_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Updated Successfully")
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}")


    
        #===================Delete function =====================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sanskar21",database="MyData")
                    my_cursor=conn.cursor()
                    sql="delete from student_table where Student_id=%s"
                    val=self.var_id.get(),
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details deleted successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#========================= Reset Function =================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#=================== Search Function ========================

    def search_data(self):
        if self.var_search_combo.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option or Enter Data")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sanskar21",database="MyData")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_table where " +str(self.var_search_combo.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)

                    conn.commit()
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




#==================== Generate Dataset or Take Photo Samaple=====================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="" :
            messagebox.showerror("Error","All fields are requried",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sanskar21",database="MyData")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_table")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                        id+=1
                my_cursor.execute("update student_table set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_No=%s,Gender=%s,Dob=%s,Email=%s,Contact=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_Id=%s" ,(

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_sem.get(),                                                                                                                                                       
                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_contact.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_id.get()==id+1
                ))


  
                                                                                                                                                                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()   

    #=============load predefined data on face from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Mininum neighbour=3

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)  #BREAKDOWN: cv2.putText(face,str(img_id),cv2.FONT_FONT NAME,(COLOR VALUE),THICKNESS) 
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==300: #300 samples will be taken
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset generated sucessfully!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                



if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()