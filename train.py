from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
import os
from tkinter import messagebox
from cv2 import split
import mysql.connector
import cv2
import numpy as np
import glob



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x780+0+0")
        self.root.title("Train")

        #==============Placing Background Image=======================
        img = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/tr_ds_frame.png"))
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0,width=1440,height=780)


        #=============== Train Dataset Button =====================
        img1 = Image.open(os.path.join("/Users/sanskar/Desktop/College/MiniProject Sem-6/Face Recognition /Images/tr_ds_btn.png"))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(bg_img,command=self.train_classifier,image=self.photoimg1,cursor="hand2")
        b1.place(x=569,y=633,width=328,height=100)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        imagePaths = [f for f in glob.glob(data_dir+'*.jpg')]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')#Converting Image to Greyscale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #================= Train Classifier and Save ==================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed")





        




        


if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()