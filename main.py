#By Kaelatt Version 1.0

import tkinter
from tkinter.filedialog import *
import numpy as np
from PIL import Image

def openfile():
    IMGs=askopenfilenames (title="Choisi tes images",
                      filetypes=[('jpg files', '.jpg'), ('png files', '.png'),
                                 ('all files', '.*')])
    path.set(IMGs)
    fenetre_accueil.after (1, getfile)

def getfile():
    x=0
    for i in path.get() :
        liste_file.insert(x+1,i)
        print(i)
    liste_file.pack()

def openfolder():
    ouput=askdirectory (title="Ton Dossier")
    folder.set(ouput)
    fenetre_accueil.after (1, getfolder)

def getfolder():
    liste_folder.insert(1,folder.get())
    liste_folder.pack()


def create():
    x=0
    try :
        output = folder.get() + "/output.jpg"
        list = [Image.open(i) for i in path.get()]
        imgs_comb=np.vstack ((list))
        imgs_comb=Image.fromarray (imgs_comb)
        imgs_comb.save (output)
        tkinter.Label(canvas, text='Fusion Ok - '+output).pack ()
    except E:
        tkinter.Label (canvas, text='Fusion Fail contact Kaelatt').pack ()
if __name__ == '__main__':
    fenetre_accueil=Tk ()  # création fenetre accueil
    fenetre_accueil.title ("All for One by Kaelatt - V1.0")  # titre de la fenetre
    fenetre_accueil.geometry ("800x600+350+100")  # taille de la fenetre definie
    fenetre_accueil.iconbitmap ("../all-star_emote.ico")
    path=Variable()
    folder = Variable()

    canvas=Canvas (fenetre_accueil, width=800, height=600, bd=0, highlightthickness=0)
    tkinter.Button (canvas, text="Choisis tes img", bg='#ECA612', command=openfile) \
        .pack (fill='x', expand=False, pady=10, padx=0)

    tkinter.Button (canvas, text="Choisis ton dossier de sortie", bg='#ECA612', command=openfolder) \
        .pack (fill='x', expand=False, pady=10, padx=0)

    liste_file=Listbox (canvas, height = 10 ,width = 50)
    liste_folder= Listbox (canvas, height = 10 ,width = 50)
    tkinter.Label (canvas)

    tkinter.Button (canvas, text="Transforme", bg='#ECA612', command=create) \
            .pack (fill='x', expand=False, pady=10, padx=0)

    canvas.pack ()
    fenetre_accueil.mainloop ()