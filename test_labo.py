# -*- coding: utf-8 -*-

from labo import labo_vide 
from labo import enregistrer_arrive 
from labo import enregistrer_depart 
from labo import changer_bureau 
from labo import PresentException 

def test_labo_vide():
    labo = labo_vide()
    assert len(labo) == 0

def test_enregistrer_arrive():
    labo = labo_vide()
    enregistrer_arrive(labo, "Xavier", "F305")
    assert labo["Xavier"] == "F305"


def test_enregistrer_arrive_fail():
    labo = labo_vide()
    enregistrer_arrive(labo, "Xavier", "F305")
    assert labo["Xavier"] == "F305"
    try:
        enregistrer_arrive(labo, "Xavier", "F355")
        assert False
    except PresentException as e:
        assert True

def test_enregistrer_depart():
    labo = labo_vide()
    pass

def test_changer_bureau():
    labo = labo_vide()
    pass

print("ok")