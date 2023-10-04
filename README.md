# Facial Recognition Attendance System 
## A Project made using Python language with tkinter used to build the front-end and MySQL database as the backend for storing student data along with Haar cascade classifier for face recognition. The motivation behind this project is to implement the facial recognition feature in a real-life scenario. This project is also a student database management system performing basic CRUD operations interacting with the database and also uses the Haar cascade classifier for facial recognition, marking attendance simultaneously and exporting it in a CSV format.



### Login Page
When you launch our project you are first greeted with the Admin login page where we also have the New user button for Registration and also the forgot Password button.

![image](https://github.com/SanskarPawaskar/Face-Recoginition-Attendance-System/assets/74868217/73ca3023-1545-4705-bcb0-03da24d6ba9b)

### Admin Registration Page
This is our AdminRegistration Page
We have kept the email as our primary key which will be used as username while logging in.You have to also select security question and answer for the same

![image](https://github.com/SanskarPawaskar/Face-Recoginition-Attendance-System/assets/74868217/98a7e680-55ff-418f-81d2-d775e14fd2f6)

### Student Management Page (Dashboard)
Once the user has logged in they will be greeted with the student management page this page there are five Major part
Student Registration

* Attendance

* Photos

* Train Dataset

* Mark Attendance


![image](https://github.com/SanskarPawaskar/Face-Recoginition-Attendance-System/assets/74868217/b61dd99a-0adb-4f10-b502-2ff5c01c3053)

### Photos

This button will redirect you to a directory on your computer where all the images of the students are stored which are taken during the student registration.

### Train Dataset

This section is used to train all the images taken during student registration and store all the data in an XML file for face recognition

### Student Registration Page
* This page is used for the Registration of new Students where they input their necessary information.
  
* We also take photo Samples of students here for facial recognition to mark their attendance here
  
* On the left side of the frame, we have a student details window that displays information of students that have already registered


![image](https://github.com/SanskarPawaskar/Face-Recoginition-Attendance-System/assets/74868217/0a96ebd6-6665-48ef-9f10-f4beef45d48e)


### Attendance Management

This section can be used to view and export the marked attendance into a csv file which can be viewed in excel.

![image](https://github.com/SanskarPawaskar/Face-Recoginition-Attendance-System/assets/74868217/c5a51029-3445-417e-8b90-395e7b69adc6)

### Mark Attendance

In this section, when a student clicks on the Mark attendance button the camera is turned on. If the Students details are stored in the database the system will display its information or else it will show Unknown face.


![image](https://github.com/SanskarPawaskar/Face-Recoginition-Attendance-System/assets/74868217/0bc50746-e935-4cff-9f68-97aa8c922074)

### Database


#### Admin Database

![image](https://github.com/SanskarPawaskar/Face-Recoginition-Attendance-System/assets/74868217/3a72c3a7-64fe-44b6-90fe-a550fb1b0095)

#### Student Database

![image](https://github.com/SanskarPawaskar/Face-Recoginition-Attendance-System/assets/74868217/5ece24ee-3406-4a81-9b8e-eef93b2da536)





