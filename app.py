from tkinter import *
import tkinter 
from tkinter import messagebox
import time

root = Tk()
root.title("Gestionnaire d'une quincaillerie")
# center(root, 580, 380)
root.resizable(width=False, height=False)

    # Observateur
def update_label(*args):
    if len(var_client_name.get()) <= 12:
        nameVar.set(var_client_name.get().lower().title())
    if len(var_client_name.get()) > 13:
        messagebox.showwarning("Attention", "Le nom du client ne doit pas depasser plus de 13 caracteres espace y compris.")
    quantiterVar.set(var_quantiter_prod.get())
    # productVar.set(var_product.get())
    priceVar.set(var_quantiter_prod.get() * 2)

def update_payement(*ars):
    payementVar.set("Aucune")
    if var_type_payement.get() == 1:
        payementVar.set("Cheque")
    elif var_type_payement.get() == 2:
        payementVar.set("Virement")
    elif var_type_payement.get() == 0:
        payementVar.set("Espece")

import sqlite3
def createDatabase():
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        tClient = """
        CREATE TABLE Clients(
            id INTEGER,
            nom TEXT,
            produit TEXT,
            quantiter INTEGER,
            payement TEXT
        )
        """
        tProduit = """
        CREATE TABLE Produits(
            id INTEGER,
            nom TEXT,
            prix INTEGER
        )
        """
        cur.execute(tClient)
        cur.execute(tProduit)

        for k,v in enumerate(products):
            d = {
                "id" : f"{k}",
                "nom" : f"{v}",
                "prix": "100"
            }

            cur.execute("""
                INSERT INTO Produits 
                VALUES(:id, :nom, :prix)
            """, d)
            
        messagebox.showinfo("Success", "Base de donnees creer avec success. Vous pouvez commencer a travailler.")
    except sqlite3.OperationalError:
        messagebox.showwarning("Rappel", "La base de donnees existe deja. Fecturer vos operations!")
    finally:
        con.commit()
        con.close()

def validerCommande():
    pass

from fpdf import FPDF
def genererFacture():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "N", 16)
    pdf.write(10, f"Nom du client: {nameVar.get()}")
    pdf.write(15, f"Quantiter: {quantiterVar.get()}")
    pdf.write(10, f"Type de payement: {int(payementVar.get())}")
    pdf.write(10, f"Prix total: {priceVar.get()}")
    pdf.output("facture.pdf")

# ------------------------------------------------------------------------------------------------------------------------------------------
zone_block_left = LabelFrame(root, fg='#f50606', text="Enregistrement du client", font=("Century Gothic", 10))

lb_client_name = Label(zone_block_left, text="Nom et prenom du client: ", font=("Century Gothic", 8))
var_client_name = StringVar()
var_client_name.trace('w', update_label)
client_entry = Entry(zone_block_left, textvariable=var_client_name, font=("Century Gothic", 8))
lb_client_name.grid(row=0, column=0)
client_entry.grid(row=0, column=1)

lb_products = Label(zone_block_left, text="Nom du produit: ", font=("Century Gothic", 8))
var_product = StringVar()
# var_product.trace('w', update_label)
product_list = Listbox(zone_block_left, listvariable=var_product, font=("Century Gothic", 8))
products = ["Couteau", "Seaux", "Marteau", "Peinture", "Gaz", "Sacs", "Machette", "Bourhoutte", "Peinture", "Plaque a gaz", "Pince","", "Autres"]
for k,v in enumerate(products):
    product_list.insert(k, f"{v}")
lb_products.grid(row=1, column=0)
product_list.grid(row=1, column=1)

lb_quantiter_prod = Label(zone_block_left, text="Quantiter: ", font=("Century Gothic", 8))
var_quantiter_prod = IntVar()
var_quantiter_prod.trace('w', update_label)
quantiter_prod = Spinbox(zone_block_left, from_=1, to=50, font=("Century Gothic", 8), textvariable=var_quantiter_prod)
lb_quantiter_prod.grid(row=2, column=0)
quantiter_prod.grid(row=3, column=1)

lb_payement = Label(zone_block_left, text="Mode de payement: ", font=("Century Gothic", 8))
var_type_payement = IntVar()
var_type_payement.trace('w', update_payement)
espece_payement = Radiobutton(zone_block_left, variable=var_type_payement, text="Espece", value=0, font=("Century Gothic", 8))
cheque_payement = Radiobutton(zone_block_left, variable=var_type_payement, text="Cheque", value=1, font=("Century Gothic", 8)) # check= 1
virement_payement = Radiobutton(zone_block_left, variable=var_type_payement, text="Virement", value=2, font=("Century Gothic", 8))

lb_payement.grid(row=4, column=0)
espece_payement.grid(row=4, column=1)
cheque_payement.grid(row=5, column=1)
virement_payement.grid(row=6, column=1)

validCommand = Button(zone_block_left, text="Valider la commande", font=("Century Gothic", 8), command=validerCommande)
validCommand.grid(row=7, column=1, padx=8, pady=12)

zone_block_left.pack(side="left", fill="y")

# ------------------------------------------------------------------------------------------------------------------------------------------
zone_block_top_right = LabelFrame(root, fg='#f50606', text="Fournisseur", font=("Century Gothic", 10))
lb_produit = Label(zone_block_top_right, text="Produit: ", font=("Century Gothic", 8))
produitVar = StringVar()
produit = Entry(zone_block_top_right, textvariable=produitVar)
lb_produit.grid(row=0, column=0)
produit.grid(row=0, column=1)

lb_qts = Label(zone_block_top_right, text="Quantiter: ", font=("Century Gothic", 8))
qtsVar = IntVar()
qts = Entry(zone_block_top_right, textvariable=qtsVar, font=("Century Gothic", 8))
lb_qts.grid(row=1, column=0)
qts.grid(row=1, column=1)

btn = Button(zone_block_top_right, text="Passer la commande", font=("Century Gothic", 8))
btn.grid(row=2, column=1, pady=5)

zone_block_top_right.pack(side="top", ipady=45, ipadx=40)
# ------------------------------------------------------------------------------------------------------------------------------------------

zone_block_right = LabelFrame(root, fg='#f50606', text="Information d'enregistrement", font=("Century Gothic", 10))
lb_client_name_new = Label(zone_block_right, text="Nom et prenom du client: ", font=("Century Gothic", 8))
nameVar = StringVar()
lb_n_client_name = Label(zone_block_right, textvariable=nameVar, font=("Century Gothic", 8))

lb_products = Label(zone_block_right, text="Nom du produit: ", font=("Century Gothic", 8))
productVar = StringVar()
lifeProduct = Label(zone_block_right, textvariable=productVar)

lb_quantiter_prod = Label(zone_block_right, text="Quantiter: ", font=("Century Gothic", 8))
quantiterVar = IntVar()
lb_n_quantiter_prod = Label(zone_block_right, textvariable=quantiterVar, font=("Century Gothic", 8))

lb_payement = Label(zone_block_right, text="Mode de payement: ", font=("Century Gothic", 8))
payementVar = IntVar()
lifePayemenet = Label(zone_block_right, textvariable=payementVar, font=("Century Gothic", 8))    

lb_n_price = Label(zone_block_right, text="Prix: ", font=("Century Gothic", 8))
priceVar = IntVar()
lifePrice = Label(zone_block_right, textvariable=priceVar, font=("Century Gothic", 8))

btn_facture = Button(zone_block_right, text="Generer facture", font=("Century Gothic", 8), command=genererFacture)

lb_client_name_new.grid(row=0, column=0)
lb_n_client_name.grid(row=0, column=1)

lb_products.grid(row=1, column=0)
lifeProduct.grid(row=1, column=1)

lb_quantiter_prod.grid(row=2, column=0)
lb_n_quantiter_prod.grid(row=2, column=1)

lb_payement.grid(row=3, column=0)
lifePayemenet.grid(row=3, column=1)

lb_n_price.grid(row=4, column=0)
lifePrice.grid(row=4, column=1)

btn_facture.grid(row=5, column=1, padx=12, pady=12)
zone_block_right.pack(side="bottom")

mainmenu = Menu(root)
first = Menu(mainmenu, tearoff=0)
first.add_command(label="Creer la base de donnees", command=createDatabase)
first.add_command(label="Quitter", command=root.quit)

mainmenu.add_cascade(menu=first, label="Fichier")

root.config(menu=mainmenu)
root.mainloop()