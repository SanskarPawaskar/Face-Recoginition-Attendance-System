from email.mime import image
from logging import root
import re
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
import os
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX, split
import mysql.connector
import cv2
import numpy as np
import glob
from time import strftime
from datetime import datetime
import csv


 
class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x780+0+0")
        self.root.title("Mark Attendance")

#==============Placing Background Image=======================
        img = Image.open(os.path.join("Images/mark_attendance_frame.png"))
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0,width=1440,height=780)


        #=============== Mark Attendance Button =====================
        img1 = Image.open(os.path.join("Images/mark_attendance_btn2.png"))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(bg_img,command=self.face_recog,image=self.photoimg1,cursor="hand2")
        b1.place(x=518,y=649,width=400,height=100)

#=================== Mark Attendance==================================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d  not in name_list)): #for not taking attendance twice
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

        #conn=mysql.connector.connect(host="localhost",username="root",password="sanskar21",database="Mydata")
        

        #with open('attendance.csv') as csv_file:
            #csvfile=csv.reader(csv_file, delimiter=',')
           # all_value =[]
           # for row in csvfile:
               # value=(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                #all_value.append(value)

       # query="insert into 'atten_dance' ('Stu_id', 'Roll_No', 'Name', 'Department', 'Time', 'Date', 'Status') values(%s,%s,%s,%s,%s,%s,%s)"

        #my_cursor=conn.cursor()
        #my_cursor.execute(query, all_value)
        #my_cursor.execute("insert into atten_dance values(%s,%s,%s,%s,%s,%s,%s)",(i, r, n, d, dtString, d1, "Present"))
#
        #conn.commit()
        #conn.close()




#=================== Face Recognition Function==========================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors )
            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict= clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host="localhost",username="root",password="sanskar21",database="Mydata")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student_table where Student_Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll_No from student_table where Student_Id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Department from student_table where Student_Id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_Id from student_table where Student_Id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>85:
                    cv2.putText(img,f"Student Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll_No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCasade):
            coord=draw_boundary(img,faceCasade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            #ret=np.array(img)
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



 



if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()