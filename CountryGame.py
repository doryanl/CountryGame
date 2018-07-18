#!/usr/bin/Python3.5
# -*- coding: utf-8 -*-
#Lievre Doryan TS1

from tkinter import *
from Class import *

#France = Pays()
Allemagne = Pays()
Espagne = Pays()
Portugal = Pays()
Suede = Pays()
Chine = Pays()
Japon = Pays()
CoréeDuSud = Pays()
Inde = Pays()
Thailande = Pays()
Russie = Pays()
Vietnam = Pays()
Taiwan = Pays()
Singapour = Pays()
kazakhstan = Pays()
USA = Pays()
Canada = Pays()
Australie = Pays()
Brésil = Pays()
RoyaumeUni = Pays()
Argentine = Pays()
Egypte = Pays()
Pérou = Pays()
AffriqueDuSud = Pays()
Ukraine = Pays()
EmirasArabesUnis = Pays()
Danemark = Pays()
Norvège = Pays()
Islande = Pays()
Chili = Pays()

France.Def('FRANCE',['Le pays inventeur du systeme metrique','Un polygone a 6 côtés','Louis XIV était son roi'],'Drapeaux/France.gif')
Allemagne.Def('ALLEMAGNE',["L'un de ses châteaux a inspiré celui de Disneyland","Le pays le plus peuplé de l'U.E",'A été divisé en deux durant la Guerre Froide'],'Drapeaux/Allemagne.gif')
Espagne.Def('ESPAGNE',["A éte envahie par l'empire arabe dans le passé","L'une des dernières monarchies en Europe ",'On y danse le flamenco'],'Drapeaux/Espagne.gif')
Portugal.Def('PORTUGAL',["Macao fut l'une de ses colonies","La plus ancienne ville d'Europe de l'Ouest s'y trouve",'Le football y est le sport le plus populaire'],'Drapeaux/Portugal.gif')
Suede.Def('SUEDE',['Le premier pays à accorder le suffrage aux femmes',"L'une des terres des Vikings","Une marque de magasin d'ameublement très connu y a son siège social"],'Drapeaux/Suede.gif')
Japon.Def('JAPON',['Pays soumis a de nombreux séïsme','Le paradis des Otaku','Le pays du soleil levant'],'')
          
Europe = set()
EurAsie = set()
Monde = set()

Europe = {France,Allemagne,Espagne,Portugal,Suede}
EurAsie = Europe | {Japon}
Monde = EurAsie | {USA}

CountryGame = Win()
CountryGame.Zones = {"Europe":Europe, "EurAsie":EurAsie, "Monde":Monde}
CountryGame.ini()
