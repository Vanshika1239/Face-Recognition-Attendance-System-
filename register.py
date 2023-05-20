from logging import root
from os import close, path

from logging import root
from os import SEEK_CUR, close
from tkinter import*
from tkinter import ttk
from typing import Any

from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor, CMySQLConnection, MySQLConnection

import cv2
import datetime
from time import strptime
import re
import pyttsx3
# mera
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()
    #end



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1900x700+0+0")

        # ***************variabler
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background img
        # self.bg = ImageTk.PhotoImage(
        #     file=r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\background.PNG")
        # self.bg = ImageTk.PhotoImage(
        #     file = r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\9.jpg")
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\background.PNG")
        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # #left image
        # self.bg1 = ImageTk.PhotoImage(
        #     file=r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\6.jpg")
        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\admin\OneDrive\Pictures\working.PNG")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=100, y=100, width=800, height=550)
        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=620, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE.......", font=(
            "times new roman", 22, "bold"), fg="Blue", bg="white")
        register_lbl.place(x=20, y=20)

        # ***lebal and entry
        # column 1
        fname = Label(frame, text="First Name", font=(
            "times new roman", 12, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 12))
        self.fname_entry.place(x=50, y=130, width=250)



        lname = Label(frame, text="Last Name", font=("times new roman", 12, "bold"), bg="white")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 12))
        self.txt_lname.place(x=370, y=130, width=250)

        # column 2
        contact = Label(frame, text="Contact No.", font=("times new roman", 12, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 12))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 12))
        self.txt_email.place(x=370, y=200, width=250)

        # ...........column3
        security_Q = Label(frame, text="Select Security Question", font=(
            "times new roman", 12, "bold"), bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 12,  ), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your  School Name", "Your Favourite Colour")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 12, "bold"), bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 12))
        self.txt_security.place(x=370, y=270, width=250)

        # ......colum 5
        pswd = Label(frame, text="Password", font=(
            "times new roman", 12, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 12))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 12, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 12))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ......check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I am Agreed with the terms and conditions", font=("times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # button

        # img = Image.open(
        #     r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\7.jpg")
        # img = ImageTk.PhotoImage(file = r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\7.jpg")
        # img = ImageTk.PhotoImage(file = r"img\7.jpg")
        img = Image.open(r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\reg.PNG")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=70, y=420, width=200)

        # img1 = Image.open(
        #     r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\Capture.PNG")
        # img1 = ImageTk.PhotoImage(file = r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\8.jpg")
        img1 = Image.open(r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\login.PNG")
        img1 = img1.resize((200,50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)

    def checkname(self, name):
        for char in name:
            if not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
                return False
        return True

    def checklname(self, name):
        for char in name:
            if not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
                return False
        return True

    def checkphone(self, phone):
        if len(phone) <= 10:
            if phone.isdigit():
                return True
            if len(str(phone)) == 0:
                return True
            else:
                messagebox.showerror('Invalid', 'Invalid entry. Please enter phone (example:9846200045)',
                                     parent=self.root)
                return False

        else:
            messagebox.showwarning('Alert', 'invalid phone. Please enter phone (example:9846200045)', parent=self.root)
            return False

    # ...............function...................

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            speak_va('All fills are required')
            messagebox.showerror("Error", "All fills are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password and confirm password must be same")
        elif self.var_check.get() == 0:

            messagebox.showerror(
                "Error", "Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', passwd='vanshika@08102001',database='data')
            # conn = mysql.connector.connect(host="localhost", user="root", password="Keshav@123", database="mydata")
            my_cursor = conn.cursor()
            query = ("select * from  students where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                speak_va('User already registered this email')
                messagebox.showerror("Error", "User already registered this email")
            else:
                my_cursor.execute("insert into students  values(%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),
                    self.var_confpass.get()

                ))
                speak_va('Registered Successfully')
                messagebox.showinfo("Success", "Registered Successfully")
        conn.commit()
        conn.close()

    # object ko open garna
if __name__ == "__main__":
        root = Tk()
        app = Register(root)
        root.mainloop()