
from os import close, path
from logging import root
from os import SEEK_CUR, close
from tkinter import*
from tkinter import ttk
from typing import Any
from attendance import Attendance
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor, CMySQLConnection, MySQLConnection
from main import Face_Recognition_System
from student import Student
from train import Train
from face_recognition import Face_Recognition


import cv2
import datetime
from time import strptime
import re
import pyttsx3
from mysql.connector import cursor

from os import close


# mera
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice




def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1800x800+0+0")



        # background img
        # self.bg = ImageTk.PhotoImage(
        #     file=r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\background.PNG")
        # self.bg = ImageTk.PhotoImage(
        #     file = r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\9.jpg")
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\admin\PycharmProjects\pythonProject1 face recognition.py\back.PNG")
        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0, relwidth=1,relheight=1)

        # img1 = Image.open(
        #     r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\2.jpg")
        img1 = Image.open(r"C:\Users\admin\OneDrive\Pictures\login.PNG")
        # img1 = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\2.jpg")

        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)
        frame = Frame(self.root, bg="white")
        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), bg="white", fg="Red")
        get_str.place(x=100, y=100)

        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=550)

        # img1 = Image.open(
        #     r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\2.jpg")
        img1 = Image.open(r"C:\Users\admin\OneDrive\Pictures\loging.PNG ")
        # img1 = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\2.jpg")

        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20,"italic" ,"bold"), bg="white", fg="black")
        get_str.place(x=100, y=100)

        # labels
        username_lbl = Label(frame, text="Email ID", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        username_lbl.place(x=65, y=152)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 12  ))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        password_lbl.place(x=65, y=225)

        self.txtpass = ttk.Entry(frame, show="*", font=("times new roman", 12 ))
        self.txtpass.place(x=40, y=250, width=270)

        # icon.............
        # img2 = Image.open(
        #     r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\2.jpg")
        img2 = Image.open(r"C:\Users\admin\OneDrive\Pictures\LOO.PNG")
        # img2 = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\2.jpg")

        img2 = img2.resize((20, 20), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="white", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        # img3 = Image.open(
        #     r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\img\3.jpg")
        img3 = Image.open(r"C:\Users\admin\OneDrive\Pictures\pass.PNG")
        # img3 = Image.open(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\img\3.jpg")

        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="white", borderwidth=0)
        lblimg3.place(x=650, y=397, width=25, height=25)

        # loginBuutton
        loginbtn = Button(frame,  command=self.login,  text="Login", font=(
            "times new roman", 15, "bold"), bd=3, relief=RIDGE, bg="blue", fg="orange")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # registrationButton
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=(
            "times new roman", 14,"italic", "bold"), borderwidth=0, bg="white", fg="black", activebackground="white")
        registerbtn.place(x=25, y=350, width=160)

        # forgetpasswordButton
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,
                           font=("times new roman", 14,"italic", "bold"), borderwidth=0, bg="white", fg="black",
                           activebackground="white")
        forgetbtn.place(x=15, y=390, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app =Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "khom37" or "Khom" and self.txtpass.get() == "khom@123":
            speak_va("Welcome to Face Recognition World")
            messagebox.showinfo("success", "welcome to Face Recognition World")
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_System(self.new_window)
        else:
            conn = mysql.connector.connect(host='localhost', user='root', passwd='vanshika@08102001', database='data')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from  students where email=%s and pass=%s", (
                self.txtuser.get(),
                self.txtpass.get()

            ))
            row = my_cursor.fetchone()
            if row == None:
                speak_va("Invalid username and password!")
                messagebox.showerror("Error", "Invalid username and password")
            else:
                open_main = messagebox.askyesno("YesNo", "Acess only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


        # ************************************Reset password button ko lagi*******************

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "select the security question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "select your answer", parent=self.root2)
        elif self.txt_newpassword.get() == "":
            messagebox.showerror("Error", "please enter your new password", parent=self.root2)
        else:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Keshav@123", database="mydata")
            conn = mysql.connector.connect(host='localhost', user='root', passwd='vanshika@08102001',database='data')
            my_cursor = conn.cursor()
            query = ("select * from  students where email = %s and securityQ=%s and securityA=%s ")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
            my_cursor.execute(query, value)
            # my_cursor.execute("select * from register where email=%s and securityQ=%s and securityA=%s "(
            # self.txtuser.get(),
            # self.combo_security_Q.get(),
            # self.txt_security.get()

            #          ))
            row = my_cursor.fetchone()
            if row == None:
                speak_va("Wrong Security Answer")
                messagebox.showerror("Error", "Invalid security answer")
            else:
                query = ("update  students set pass=%s where email=%s")
                value = (self.txt_newpassword.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                speak_va("Your password has been reset successfully.")
                messagebox.showinfo("Info", "your password has been reset , please login new password",
                                    parent=self.root2)
            conn.commit()
            conn.close()
            self.root2.destroy()

        #   ************************forget password ko lagi****************

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', passwd='vanshika@08102001',database='data')
            my_cursor = conn.cursor()
            query = (
                "select *from  students where email=%s")  ##### <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< see thissssssss
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            #print(row)
            if row == None:
                messagebox.showerror("Error", "Please enter the valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 15, "bold"), bg="white",
                          fg="red")
                l.place(x=0, y=0, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"),
                                   bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth place", "your dad name", "your mother name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=70, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=70, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"),
                             bg="blue", fg="black")
                btn.place(x=100, y=300)
#--------------------Register ko class__________________________
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

    def return_login(self):
        self.root.destroy()


# defining object

if __name__ == "__main__":
     main()
     root= Tk()
     app=login_window(root)
     root.mainloop()

