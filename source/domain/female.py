# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.domain.person import Person
from source.util.evaluator import Evaluator


class Female(Person):
    """
    Male class, i.e. second of only two gender classes

    """

    def __init__(self, age=0, income=0, kinder_garden='0', sfo='0', pregnant='0'):
        """
        Constructor / Instantiate the class

        Parameters
        ----------
        age             : int, float, str
                          age of person
        income          : int, float
                          gross yearly income
        kinder_garden   : str
                          kids in kinder garden, '1' true or '0' false
        sfo             : str
                          After school programme, '1' true or '0' false
        pregnant        : str
                          Pregnant female, '1' true or '0' false

        """
        Evaluator.evaluate_data_type({pregnant: str})

        Evaluator.evaluate_possible_arguments({pregnant: ['pregnant', ('0', '1')]})

        Evaluator.evaluate_two_boolean(self.set_age(age) not in ('19', '50'), pregnant == '1',
                                       "pregnancy at this age not possible")

        super().__init__(sex='f', age=age, income=income, kinder_garden=kinder_garden, sfo=sfo)

        self.age = self.set_age(age)
        self.income = str(income)
        self.kinder_garden = kinder_garden
        self.sfo = sfo
        self.pregnant = pregnant
