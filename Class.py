#!/usr/bin/Python3.5
# -*- coding: utf-8 -*-
#Lievre Doryan TS1

from tkinter import *
from random import *
from time import time

class Pays:

    def __init__(self):
        self.nom = ''
        self.indices = ['','','']
        self.drapeau = ''

    def Def(self,nom,indices,drapeau):
        self.nom = nom
        self.indices = indices
        self.drapeau = drapeau

    def OpDrap(self,fen):
        photo = PhotoImage(file = self.drapeau)
        Drap = Canvas(fen,width = 600,height = 400)
        Drap.create_image(10,10,anchor = NW,image=photo)
        Drap.pack()
        Drap.place(relx=0.5,rely=0.7,anchor="c")
        i = time()
        e = time()+3
        while i < e:
            i = time() 
            fen.update_idletasks()
            fen.update()
        Drap.destroy()
        fen.update_idletasks()
        fen.update()
        
        
class Win:

    def __init__(self):
        self.game = Tk()
        self.elmt = []
        self.Zones = set()
        self.mot = ""
        self.pays = Pays()
        self.point = 0
        self.turn = 0
        self.loop = True
        self.nom = ""
        l = self.game.winfo_screenwidth()*8//10
        h = self.game.winfo_screenheight()*8//10
        Abscisse = (self.game.winfo_screenwidth()-l)//2
        Ordonné = (self.game.winfo_screenheight()-h)//2
        self.game.title("Countrygame")
        self.game.geometry("%dx%d%+d%+d" % (l,h,Abscisse,Ordonné))

    def finish(self):
        self.game.destroy()

    def ini(self):
        fen = self.game
        l = self.game.winfo_screenwidth()*8//10
        h = self.game.winfo_screenheight()*8//10
        intro = 'Bienvenue dans notre jeu, nous vous laissons choisir le mode difficulté :'
        MonTexte=Label(fen, text=intro, font=('calibri',int(-1.9*l/73),'bold'),fg='red')
        MonTexte.place(relx=.5, rely=0, anchor="n")
        Choix1=Button(text="Europe", font=('calibri','30','bold'),fg='green',command = self.Europe)
        Choix1.place(relx=0.5,rely=0.25,anchor="c")
        Choix2=Button(text="Eurasie", font=('calibri','30','bold'),fg='red',command = self.EurAsie)
        Choix2.place(relx=0.5,rely=0.5,anchor="c")
        Choix3=Button(text="Monde", font=('calibri','30','bold'),fg='black',command = self.Monde)
        Choix3.place(relx=0.5,rely=0.75,anchor="c")
        self.elmt = [Choix1, Choix2, Choix3, MonTexte]

    def Clean(self):
        for i in self.elmt:
            i.destroy()
        self.elmt = []

    def Ask(self):
        Nom = self.nom
        if self.turn == 0:
            pays = sample(self.Zones[Nom],1)[0]
            self.Zones[Nom] = self.Zones[Nom] - {pays}
            self.pays = pays

    def Answer(self):
        if self.loop:
            if self.pays.nom == self.mot:
                self.loop = False
                self.point += 3-self.turn
                self.pays.OpDrap(self.game)
                self.turn = 0
            else:
                self.turn = (1+self.turn)%3
            self.Game()

    def Europe(self):
        self.nom = "Europe"
        self.Game()

    def EurAsie(self):
        self.nom = "EurAsie"
        self.Game()

    def Monde(self):
        self.nom = "Monde"
        self.Game()

    def Entry(self, evt):
        if evt.keysym == "Return":
            self.mot = self.elmt[1].get()
            self.mot = self.mot.replace(' ','') #remplace le premier élement entre parenthèse par le deuxiéme
            self.mot = self.mot.upper()         #met le mot en majuscule
            self.Answer()

    def Game(self):
        self.loop = True
        self.Clean()
        if len(self.Zones[self.nom]) >= 1:
            self.Ask()
            MonTexte = Label(text = str('indice %d: ' + self.pays.indices[self.turn]) % (self.turn+1), font=('calibri','20','bold'),fg='red')
            MonTexte.place(x=0, y=0)
            point = Label( text = "point: " + str(self.point), font=('calibri','20','bold'), fg='red')
            point.place(relx=0.9, rely=0)
            var_texte = StringVar()
            ligne_texte = Entry(self.game, textvariable=StringVar(), width=30)
            ligne_texte.place(relx = .1, rely = .1 ,anchor="c")
            self.elmt = [MonTexte, ligne_texte, point]
            self.game.bind('<Key>',self.Entry)
        else:
            self.Clean()
            self.Score()
        

    def Score(self):
        self.Clean()
        l = self.game.winfo_screenwidth()*8//10
        h = self.game.winfo_screenheight()*8//10
        MonTexte=Label(self.game, text="Bravo vous avez fini le jeu avec un score de %d point(s)" % (self.point), font=('calibri',int(-1.9*l/73),'bold'),fg='red')
        MonTexte.place(relx=.5, rely=0, anchor="n")

class Score:
    
    def __init__(self):
        self.lecture = open("score.scg", "r").read()
        self.ecriture = open("score.scg", "w")
        self.list = []

    def save(self):    
        self.ecriture.close()

    def NewScore(self,Ns,Ctg):
        self.List()
        self.Put(self,Ns,Ctg)
        
    def List(self):
        a = self.lecture
        b = 0
        for i in range(len(a)):
            if a[i] == "\n":
                self.list.append(a[b:i])
                b = i+1
        self.list.append(a[b:])

    def Put(self,Ns,Ctg):
        a = 0
        b = {"Europe" : 1,"EurAsie" : 2, "Monde" : 3}
        c = []
        d = 0
        for i in range(len(self.list)):
            if self.list[i][-1] == ":":
                a += 1
            if a == b[Ctg]:
                for j in range(len(i)):
                    if i[-j] == " ":
                        c.append(j-1)
            d += 1
