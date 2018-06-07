from tkinter import *
import os
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.grid()
        self.location(600,10)
        self.place()
        self.create_widgets()

    def create_widgets(self):
        lbl_user = Label(window, text="User")
        lbl_user.place(x=10, y=10)
        lbl_passw = Label(window, text="Pass")
        lbl_passw.place(x=10, y=30)

        txt_user = Entry(window,width=10)
        txt_user.place(x=60, y=10)
        txt_passw = Entry(window,width=10)
        txt_passw.place(x=60, y=30)

        login = Button(window, text="Start Bot", fg="green", command=self.say_hi)
        login.place(x=60, y=60)

        quit = Button(window, text="Stop Bot", fg="red",command=window.destroy)
        quit.place(x=60, y=90)

    def say_hi(self):
        print("hi there, everyone!")

    def start_bot(self, user, passw):
        chrome_options = Options()
        # chrome_options.set_headless(headless=True)
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'/usr/bin/chromedriver')
        driver.get("https://github.com/login")

        username = driver.find_element_by_id("login_field")
        password = driver.find_element_by_id("password")

        username.send_keys(user)
        password.send_keys(passw)
        time.sleep(1)

        driver.find_element_by_name("commit").click()
        print ("Headless Chrome Initialized")


window =Tk()
window.geometry('180x130')
window.maxsize(180,130)
app = Application(window)
app.mainloop()