import tkinter
from tkinter import messagebox
import random
import pyperclip
from tkinter.messagebox import askokcancel, showinfo, WARNING

randomise = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ1234567890;:,.+-=~#'

class Window():
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.geometry('500x200')
        self.window.resizable(False, False)

        self.passwordLength = tkinter.IntVar()
        self.passwordLength.set(10)
        self.password = ""

        self.window.title(window_title)
        
        # configure the grid
        self.window.columnconfigure(0, weight=2)
        self.window.columnconfigure(1, weight=3)
        self.window.columnconfigure(2, weight=4)


        lbel = tkinter.Label(self.window, text='Python Password Generator')
        lbel.config(font=('helvetica', 30))
        lbel.grid(column=0, row=0, columnspan=4,  ipady=10)

        pwdLength_label = tkinter.Label(self.window, text="Password Length")
        pwdLength_label.grid(column=0, row=1, columnspan=1, sticky=tkinter.W,ipadx=10)

        password_entry = tkinter.Entry(self.window, textvariable=self.passwordLength)
        password_entry.grid(column=1, row=1, )
        password_entry['state'] = 'disabled'


        plus_button = tkinter.Button(
        self.window, 
        text="+", 
        command=self.up
        )
        plus_button.grid(column=2, row=1,sticky=tkinter.E)
        minus_button = tkinter.Button(
        self.window, 
        text="-", 
        command=self.down
        )
        minus_button.grid(column=3, row=1,sticky=tkinter.E)

        generate_button = tkinter.Button(self.window, text="Generate", command=self.generate)
        generate_button.grid( row=2, columnspan=4,sticky=tkinter.EW, ipadx=100, 
    ipady=5, rowspan=2)

        self.delay = 1
        self.update()

        self.window.mainloop()

    def update(self):
        self.window.after(self.delay, self.update)
    
    def up(self):
        self.passwordLength.set(self.passwordLength.get()+1)
    
    def down(self):
        passwordLength = self.passwordLength.get()
        if passwordLength > 0:
            self.passwordLength.set(passwordLength-1)
    
    def generate(self):
        global randomise
        password = "".join([random.choice(randomise) for x in range(self.passwordLength.get())])
        frame = tkinter.Toplevel(self.window)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=3)
        frame.columnconfigure(2, weight=3)

        frame.geometry('300x100')


        pwd_label = tkinter.Label(frame, text="Generated Password")
        pwd_label.config(font=('helvetica', 10))
        pwd_label.grid(column=0, row=0, columnspan=3)

        pwd_label = tkinter.Label(frame, text=password)
        pwd_label.config(font=('helvetica', 20))
        pwd_label.grid(column=0, row=1, columnspan=3)

        def copyPWD():
            pyperclip.copy(password)
            showinfo(
            title='Alert',
            message='Password Copied to Your Clipboard')  

        tkinter.Button(frame, text='Copy', command=copyPWD).grid(column=0, row=2)
        tkinter.Button(frame, text='Close', command= lambda: frame.destroy()).grid(column=2, row=2)

app = Window(tkinter.Tk(), "Random Password Generator")

randomise = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ1234567890;:,.+-=~#'
print("".join([random.choice(randomise) for x in range(10)]))