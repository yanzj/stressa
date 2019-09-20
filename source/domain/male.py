# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.domain.person import Person


class Male(Person):
    """
    Male class, i.e. first of only two gender classes

    """

    def __init__(self, age=0, kinder_garden='0', sfo='0'):
        """
        Constructor / Instantiate the class

        Parameters
        ----------
        age             : int, float, str
                          age of person
        kinder_garden   : str
                          kids in kinder garden, '1' true or '0' false
        sfo             : str
                          After school programme, '1' true or '0' false

        """
        super().__init__(sex='m', age=age, kinder_garden=kinder_garden, sfo=sfo)
