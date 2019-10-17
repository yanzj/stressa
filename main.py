# -*- coding: windows-1252 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.infrastructure import Ssb, Posten, Sifo, Portalen
from source.domain import Female, Family, Male

father = Male(age=45)
mother = Female(age=40)
girl = Female(age=13, sfo='1')
boy = Male(age=10, sfo='1')

family_members = [father, mother, girl, boy]
family = Family(family_members, income=850000, cars=2)
family.sifo_properties()

sifo = Sifo(family)
sifo.sifo_expenses()

posten = Posten('1275')
posten.zip_code_info()

ssb = Ssb()
ssb.ssb_interest_rates()

portalen = Portalen()
portalen.mortgage_offers()
