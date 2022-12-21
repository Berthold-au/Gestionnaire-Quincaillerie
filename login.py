from cProfile import label
from textwrap import fill
from tkinter import *
from tkinter import messagebox
import sqlite3

def center(app, larg, long):
    screen_x = int(app.winfo_screenwidth())
    screen_y = int(app.winfo_screenheight())

    window_x = larg 
    window_y = long 

    posX = (screen_x // 2) - (window_x // 2)
    posY = (screen_y // 2) - (window_y // 2)

    geo = f"{window_x}x{window_y}+{posX}+{posY}"
    app.geometry(geo)

USER_NAME = "admin"
PASS_WORD = "admin"

mainapp = Tk()
mainapp.resizable(width=False, height=False)

center(mainapp,452, 250)

mainapp.title("Login")
from subprocess import call

def verified():
    if var_username.get().lower() == USER_NAME and var_password.get().lower() == PASS_WORD:
        messagebox.showinfo("Admin", "Heureux de vous revoire!")
        mainapp.destroy()
        call(["python", "app.py"])
    else:
        messagebox.showerror("Invalid", "Nom d'utilisateur ou mot de passe invalide!")
        return False
    pass
zone_block = LabelFrame(mainapp,text="Connexion a l'appli", font=("Century Gothic", 20), fg='#000')

lb_username = Label(zone_block, text="Nom d'utilisateur: ", font=("Century Gothic", 10), fg='#000')
var_username = StringVar()
username = Entry(zone_block, textvariable=var_username, font=("Century Gothic", 10), fg='#000')

lb_password = Label(zone_block, text="Mot de passe: ", font=("Century Gothic", 10), fg='#000')
var_password = StringVar()
password = Entry(zone_block, show='*', textvariable=var_password, font=("Century Gothic", 10), fg='#000')

btn_valid = Button(zone_block, text="Se connecter", width=18, font=("Century Gothic", 10), fg='#000', command=verified)

lb_username.grid(row=0, column=0)
username.grid(row=0, column=1)

lb_password.grid(row=1, column=0)
password.grid(row=1, column=1)

btn_valid.grid(row=2, column=1)

zone_block.pack(expand=YES, ipadx=5, ipady=8)

mainapp.mainloop()