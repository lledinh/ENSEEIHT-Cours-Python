# -*- coding: utf-8 -*-

''' R0 Gérer l'occupation des bureaux dans un labo '''
'''
Exemple:
Arrivé de xavier dans le bureau F305 
Arrivé de aurélie dans le bureau F307 
Arrivé de marc dans le bureau F305
'''

# R1 Comment gérer l'occupation des bureaux dans un labo 
# quitter: False
# Initialiser le labo                   labo: out
# while not quitter:
#   Afficher le menu
#   Demander le choix
#   Traiter le choix

# R2 Comment traiter le choix
# if choix == 1:
#   Gérer l'arrivée d'une personne
# OU
#   Demander le nom de la personne      nom: out
#   Demander le numéro du bureau        bureau: out
#   Enregistrer la personne             nom: in bureau: in labo: inout
#                                       try except personne déjà enregistrée
# elif: ...

# Module labo
# Labo_Vide()
# Enregistrer_arrive(labo, nom, bureau)
# Enregistrer_depart(labo, nom)
# Changer_Bureau(labo, nom, bureau)

# Module ihm                            utilise module labo optionnel module menu textuel
# Gerer_arrive
# Afficher_menu

# Optionel module menu textuel

# Module test labo                      utilise module labo

# Module scenario mixte ihm / test      utilise module labo

def labo_vide():
    labo = {}
    return labo

def enregistrer_arrive(labo, nom, bureau):
    if nom in labo:
        raise PresentException

    labo[nom] = bureau

def enregistrer_depart(labo, nom):
    if nom not in labo:
        raise AbsentException

    del labo[nom]

def changer_bureau(labo, nom, bureau):
    labo[nom] = bureau

class LaboException(Exception):
    """ Généralise les exceptions du laboratoire."""
    pass

class AbsentException(LaboException):
    pass


class PresentException(LaboException):
    pass