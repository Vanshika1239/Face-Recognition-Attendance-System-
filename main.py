import tkinter
from tkinter import *
from PIL import Image, ImageTk
from PIL import Image
from student import student
import os
import time
from time import strftime
from datetime import datetime
import sys
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpdeck import Helpdeck
from logging import root


from exit import Exit

class Face_Recognition_System:
    def __init__(self, root):
         self.root = root
         self.root.geometry("1450x820+0+0")
         self.root.title("Face Recognition System")


    # first image
         #img1 = Image.open("clg1.PNG")
         #img1 = img1.resize((775, 120), Image.ANTIALIAS)
         #self.photoimg1 = ImageTk.PhotoImage(img1)

         #f_lbl = Label(self.root, image=self.photoimg1)
         #f_lbl.place(x=0, y=0, width=450, height=120)

         # second image
         img2 = Image.open(r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\eye.PNG")
         img2 = img2.resize((775, 120), Image.ANTIALIAS)
         self.photoimg2 = ImageTk.PhotoImage(img2)

         f_lbl = Label(self.root, image=self.photoimg2)
         f_lbl.place(x=450, y=0, width=450, height=120)

        # third image
         # img3 = Image.open("clg2.PNG")
         # img3 = img3.resize((775, 120), Image.ANTIALIAS)
         #  self.photoimg3 = ImageTk.PhotoImage(img3)

         # f_lbl = Label(self.root, image=self.photoimg3)
         # f_lbl.place(x=900, y=0, width=450, height=120)

         # background image
         img4 = Image.open("background.PNG")
         img4 = Image.open("background.PNG")
         img4 = img4.resize((1350, 580), Image.ANTIALIAS)
         img4 = img4.resize((1550, 780), Image.ANTIALIAS)
         self.photoimg4 = ImageTk.PhotoImage(img4)

         bg_img = Label(self.root, image=self.photoimg4)
         bg_img.place(x=0, y=120, width=1350, height=580)
         bg_img.place(x=0, y=120, width=1550, height=780)

         title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM ",
                           font=("Algerian", 35, "bold"), bg="white", fg="darkblue")
         title_lbl.place(x=0, y=0, width=1550, height=45)  # using .place u can place things at any part of the window
#-----------------time--------------------------
         def time():
              string = strftime('%H:%M:%S %p')
              lbl.config(text = string)

              lbl.after(1000,time)

         lbl = Label(title_lbl,font = ('timme new ramon',14,'bold'),background='white',foreground = 'blue')
         lbl.place(x=0,y=0,width=110,height=50)
         time()
         #    different buttons with images
         # student button
         img5 = Image.open("student.PNG")
         img5 = img5.resize((195, 195), Image.ANTIALIAS)
         self.photoimg5 = ImageTk.PhotoImage(img5)

         btn1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
         btn1.place(x=100, y=80, width=195, height=195)

         btn1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                         font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
         btn1_1.place(x=100, y=245, width=195, height=40)

         # Face Detection button
         img6 = Image.open("faceDetector.PNG")
         img6 = img6.resize((195, 195), Image.ANTIALIAS)
         self.photoimg6 = ImageTk.PhotoImage(img6)

         btn2 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.face_recognition)
         btn2.place(x=400, y=80, width=195, height=195)

         btn2_2 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white", command=self.face_recognition)
         btn2_2.place(x=400, y=245, width=195, height=40)

         # attendance button
         img7 = Image.open("attendes.PNG")
         img7 = img7.resize((195, 195), Image.ANTIALIAS)
         self.photoimg7 = ImageTk.PhotoImage(img7)

         btn3 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.attendance_data)
         btn3.place(x=700, y=80, width=195, height=195)

         btn3_3 = Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2",
                         font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn3_3.place(x=700, y=245, width=195, height=40)

         # Help Desk button
         img8 = Image.open("help deck.PNG")
         img8 = img8.resize((195, 195), Image.ANTIALIAS)
         self.photoimg8 = ImageTk.PhotoImage(img8)

         btn4 = Button(bg_img, image=self.photoimg8,command=self.helpdeck, cursor="hand2")
         btn4.place(x=1000, y=80, width=195, height=195)

         btn4_4 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.helpdeck, font=("times new roman", 15, "bold"),
                         bg="darkblue",  fg="white")
         btn4_4.place(x=1000, y=245, width=195, height=40)

         # train data button
         img9 = Image.open("trainFace-khom.PNG")
         img9 = img9.resize((195, 195), Image.ANTIALIAS)
         self.photoimg9 = ImageTk.PhotoImage(img9)

         btn5 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.train_data)
         btn5.place(x=100, y=350, width=195, height=195)

         btn5_5 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,
                         font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
         btn5_5.place(x=100, y=525, width=195, height=40)

         # Photos button
         img10 = Image.open("photo.PNG")
         img10 = img10.resize((195, 195), Image.ANTIALIAS)
         self.photoimg10 = ImageTk.PhotoImage(img10)

         btn6 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img)
         btn6.place(x=400, y=350, width=195, height=195)

         btn6_6 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white", command=self.open_img)
         btn6_6.place(x=400, y=525, width=195, height=40)

         # Developer button
         img11 = Image.open("developer.PNG ")
         img11 = img11.resize((195, 195), Image.ANTIALIAS)
         self.photoimg11 = ImageTk.PhotoImage(img11)

         btn7 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.developer)
         btn7.place(x=700, y=350, width=195, height=195)

         btn7_7 = Button(bg_img, text="Developer", command=self.developer,cursor="hand2", font=("times new roman", 15, "bold"),
                          bg="darkblue", fg="white")
         btn7_7.place(x=700, y=525, width=195, height=40)

         # Exit button
         img12 = Image.open(r"exit.PNG")
         img12 = img12.resize((195, 195), Image.ANTIALIAS)
         self.photoimg12 = ImageTk.PhotoImage(img12)

         btn8 = Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.iExit)
         btn8.place(x=1000, y=350, width=195, height=195)

         btn8_8 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"),
                          bg="darkblue", fg="white")
         btn8_8.place(x=1000, y=525, width=195, height=40)

    def open_img(self):
         os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure Exit This Project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    #     # =================================== Functions buttons =========================================

    def student_details(self):
       self.new_window = Toplevel(self.root)
       self.app = student(self.new_window)


    def train_data(self):
     self.new_window = Toplevel(self.root)
     self.app = Train(self.new_window)


    def face_recognition(self):
     self.new_window = Toplevel(self.root)
     self.app = Face_Recognition(self.new_window)


    def attendance_data(self):
     self.new_window = Toplevel(self.root)
     self.app = Attendance(self.new_window)


    def developer(self):
         self.new_window = Toplevel(self.root)
         self.app = Developer(self.new_window)

    def  helpdeck(self):
          self.new_window = Toplevel(self.root)
          self.app = Helpdeck(self.new_window)


    def exit(self):
     self.new_window = Toplevel(self.root)
     self.app = Exit(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
