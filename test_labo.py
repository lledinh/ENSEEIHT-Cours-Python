# -*- coding: utf-8 -*-

from labo import labo_vide 
from labo import enregistrer_arrive 
from labo import enregistrer_depart 
from labo import changer_bureau 
from labo import PresentException 
from labo import AbsentException 

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
    enregistrer_arrive(labo, "Xavier", "F305")
    assert labo["Xavier"] == "F305"

    enregistrer_depart(labo, "Xavier")
    assert "Xavier" not in labo
    

def test_enregistrer_depart_fail():
    labo = labo_vide()
    
    try:
        enregistrer_depart(labo, "Xavier")
        assert False
    except AbsentException as e:
        assert True
        
def test_changer_bureau():
    labo = labo_vide()
    enregistrer_arrive(labo, "Xavier", "F305")
    assert labo["Xavier"] == "F305"

    changer_bureau(labo, "Xavier", "F308")
    assert labo["Xavier"] == "F308"

print("ok")