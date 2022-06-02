from cgitb import text
from ensurepip import bootstrap
from posixpath import split
from re import L
from sqlite3 import Row
from tkinter import *
import tkinter as tk
from tkinter.tix import COLUMN
import PIL.Image, PIL.ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class App(tk.Tk):
    # incantation

    def __init__(self, *args, **kwargs):
        # initialisation des données
        self.t = []
        self.nt = []
        self.t1 = []
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("TKINTER PROJECT")
        self.geometry("800x600")
        # Rendre la grille de fenêtre 1x1
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # -----------------------------------main_frame-----------------------------
        # Créer un cadre de page principal

        self.main_frame = tk.Frame()

        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Création d'étiquettes de titre
        self.titleLabel = tk.Label(self.main_frame, text="WELCOME TO MY APPLICATION: ", font=('georgia', '20', 'bold'))
        self.titleLabel.pack(anchor='center', ipadx=60, ipady=60, expand=True)
        self.titleLabel = tk.Label(self.main_frame, text="EDITED BY :", font=('georgia', '15'))
        self.titleLabel.pack(anchor='w')
        self.titleLabel = tk.Label(self.main_frame, text="Bahry Adem ", font=('georgia', '18'))
        self.titleLabel.pack(anchor='w', ipadx=50, ipady=50, expand=True)

        # Bouton pour passer pour frame 1
        self.changePageButton = ttk.Button(self.main_frame, text="START ", command=lambda: self.changePage(self.frame1),
                                           bootstyle=("dark", OUTLINE))
        self.changePageButton.pack(ipadx=30, ipady=30, expand=True)

        # -------------------------------------------------------------------------
        # -----------------------------------frame1---------------------------------
        # Créer une image de destination
        self.frame1 = ttk.Frame()
        style = ttk.Style("litera")
        self.frame1.grid(row=0, column=0, sticky="nsew")

        # Création d'étiquettes de titre
        self.titleLabel = ttk.Label(self.frame1, text="TRI PAR INSERTION", font=('Georgia', '20', 'bold'),
                                    bootstyle="info")
        self.titleLabel.pack(anchor='n', expand=True, pady=30)

        self.titleLabel1 = ttk.Label(self.frame1, text="Insérer des entiers avec espace : ", font=('Georgia', '20')
                                     )
        self.titleLabel1.pack(anchor='nw', expand=True, padx=50)

        self.entre = ttk.Entry(self.frame1, text="frame1", font=('Helvetica', '30'), bootstyle="primary")
        self.entre.pack(pady=50)
        # Bouton pour revenir de l'image 1 à l'image principale
        self.entre2 = ttk.Entry(self.frame1, text="frame 9", font=('Helvetica', '30'), bootstyle="primary")
        self.entre2.pack()

        self.back_button = ttk.Button(self.frame1, text="Back", command=lambda: self.changePage(self.main_frame),
                                      bootstyle=(SUCCESS, OUTLINE))
        self.back_button.pack(anchor='n', ipadx=30, ipady=10, expand=True)

        self.bbutton = ttk.Button(self.frame1, text="sup", command=lambda: self.sup(self.titleLabel5),
                                  bootstyle=(SUCCESS, OUTLINE))
        self.bbutton.pack(anchor='n', ipadx=30, ipady=10, expand=True)

        self.titleLabel5 = ttk.Label(self.frame1, text="", font=('Helvetica', '20'), bootstyle="info")
        self.titleLabel5.pack(anchor='center', expand=True)

        self.titleLabel7 = ttk.Label(self.frame1, text='', font=('Helvetica', '20'), bootstyle="danger")
        self.titleLabel7.pack(anchor='center', expand=True)

        self.entre.bind("<KeyPress>", lambda e: self.on_key_pressing(e, self.entre, self.titleLabel7))
        self.entre2.bind("<KeyPress>", lambda m: self.on_key_pressing2(m, self.entre2))
        self.entre.bind("<space>", lambda r: self.on_key_tri(r, self.entre, self.entre2))
        self.entre.bind("<BackSpace>", lambda s: self.on_key_del(s, self.entre, self.entre2))

        # BOUTON VERS LE PAGE 3
        self.changePageButton = ttk.Button(self.frame1, text="CHANGER LE TYPE DE TRI ",
                                           command=lambda: self.changePage(self.frame2), bootstyle="success")
        self.changePageButton.pack(anchor='n', expand=True, padx=20, pady=40, fill=Y)
        # -------------------------------------------------------------------------
        # -----------------------------------frame2---------------------------------
        # Créer une image de destination
        self.frame2 = tk.Frame()
        self.frame2.grid(row=0, column=0, sticky="nsew")
        # Création d'étiquettes de titre
        self.titleLabel3 = ttk.Label(self.frame2, text="TRI PAR BULLE", font=('georgia', '20', 'bold'),
                                     bootstyle="info")
        self.titleLabel3.pack(anchor='n', expand=True, pady=30)

        self.titleLabel4 = tk.Label(self.frame2, text="Insérer Des Entiers (avec espace) : ",
                                    font=('Copperplate Gothic Bold', '20'))
        self.titleLabel4.pack(anchor='nw', expand=True, padx=50)

        self.entre1 = ttk.Entry(self.frame2, text="Frame 2", font=('Helvetica', '30'), bootstyle="info")
        self.entre1.pack(pady=50)

        self.entre3 = ttk.Entry(self.frame2, text="frame 5", font=('Helvetica', '30'), bootstyle="info")
        self.entre3.pack()

        self.back_button = ttk.Button(self.frame2, text="Back", command=lambda: self.changePage(self.frame1),
                                      bootstyle=(SUCCESS, OUTLINE))
        self.back_button.pack(anchor='n', expand=True)

        self.titleLabel6 = ttk.Label(self.frame2, text="", font=('Helvetica', '20'), bootstyle="info")
        self.titleLabel6.pack(anchor='center', expand=True)

        self.titleLabel8 = ttk.Label(self.frame2, text='', font=('Helvetica', '20'), bootstyle="danger")
        self.titleLabel8.pack(anchor='center', expand=True)

        self.entre1.bind("<KeyPress>", lambda e: self.on_key_pressing(e, self.entre1, self.titleLabel8))
        self.entre3.bind("<KeyPress>", lambda m: self.on_key_pressing2(m, self.entre3))
        self.entre1.bind("<space>", lambda r: self.on_key_tri(r, self.entre1, self.entre3))
        self.entre1.bind("<BackSpace>", lambda s: self.on_key_del(s, self.entre1, self.titleLabel8))

        # Bouton pour revenir main frame

        # --------------------------------------------------------------------------
        # main_Cadre d'affichage en haut
        self.main_frame.tkraise()

    def changePage(self, page):
        '''
Fonction de transition d'écran
        '''
        page.tkraise()

    def sup(self, label):
        nb = 0
        for i in range(len(self.t)):
            if (self.t[i] >= 3):
                nb = nb + 1
        label.config(text=str(nb))

    def on_key_pressing(self, event, entry, label):
        try:
            if (event.char[-1] != " "):
                int(event.char[-1])
                label.config(text="")
        except:

            return "break"

    def on_key_pressing2(self, event, entry):
        return "break"

    def on_key_tri(self, event, entry, entry1):

        i = len(entry.get())
        ch = ""
        while (entry.get()[i - 1] != " " and i >= 1):
            ch = entry.get()[i - 1] + ch
            i = i - 1
        self.nt.append(int(ch))
        self.t = self.nt[:]
        self.trinsertion(self.t)
        y = self.t
        y = " ".join(map(str, y)) + "  "
        entry1.delete(0, END)
        entry1.insert(0, y)

    def on_key_del(self, event, entry, label):
        if (entry.get()[-1] != " " and len(self.nt) != 0):
            self.nt.pop(-1)
            x = self.nt[:]
            y = self.nt[:]
            self.trinsertion(x)
            label.delete(0, END)
            label.insert(0, x)

            y = " ".join(map(str, y)) + "  "
            entry.delete(0, END)
            entry.insert(0, y)

    def trinsertion(self, t):
        n = len(t)
        for i in range(1, n):
            val = t[i]
            j = i - 1
            while (j >= 0) and (t[j] > val):
                t[j + 1] = t[j]
                j = j - 1
            t[j + 1] = val

    def tri_bulle(self, t):
        n = len(t)
        # Traverser tous les éléments du tableau
        for i in range(n):
            for j in range(0, n - i - 1):
                # échanger si l'élément trouvé est plus grand que le suivant
                if t[j] > t[j + 1]:
                    t[j], t[j + 1] = t[j + 1], t[j]


if __name__ == "__main__":
    app = App()
    app.mainloop()