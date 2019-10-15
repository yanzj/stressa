# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.domain import Family, Female, Entity, Male
from source.exception import DomainError
from uuid import UUID
from abc import ABC
import pytest as pt


class TestFamily:

    @classmethod
    def setup(cls):
        """
        Executed before all tests

        """
        cls.family_members = [Male(age=39), Female(age=40)]
        cls.family = Family(cls.family_members)

    @classmethod
    def teardown(cls):
        """
        Executed after all tests

        """
        cls.family = None

    def test_family_object_is_instance_of_family(self):
        """
        Test that all family objects are instances of Family class

        """
        for parents in [Entity, ABC]:
            isinstance(self.family, parents)
            issubclass(self.family.__class__, parents)

    @pt.mark.parametrize('invalid_arg', [True, 'test', 90210, 90210.0, ('test', 'test'), {}])
    def test_family_members_type_are_list(self, invalid_arg):
        """
        Test that Family object raises TypeError if family_members argument are invalid

        """
        with pt.raises(TypeError):
            self.family.family_members = invalid_arg

    def test_family_cannot_be_empty(self):
        """
        Test that family_members cannot be empty

        """
        with pt.raises(ValueError):
            self.family.family_members = []

    @pt.mark.parametrize('invalid_arg', [(), {}])
    def test_income_and_cars_type_error_for_invalid_arguments(self, invalid_arg):
        """
        TypeError raised when invalid income and cars argument types passed into Family class
        through constructor or setter

        """
        with pt.raises(TypeError):
            self.family.inntekt = invalid_arg
        with pt.raises(TypeError):
            self.family.antall_biler = invalid_arg

    @pt.mark.parametrize('negative_income', [-1094400, -1094400.0, '-1094400', '-1094400.0'])
    @pt.mark.parametrize('negative_cars', [-1, '-1'])
    def test_income_and_cars_cannot_be_negative(self, negative_income, negative_cars):
        """
        Test that ValueError is raised if negative values for income and cars are passed into
        Family class through constructor or setter

        """
        with pt.raises(ValueError):
            self.family.inntekt = negative_income
        with pt.raises(ValueError):
            self.family.antall_biler = negative_cars

    @pt.mark.parametrize('inntekt', [594400, 594400, '594400', '594400'])
    @pt.mark.parametrize('antall_biler', [0, '0'])
    def test_arguments_gets_set_in_family_object(self, inntekt, antall_biler):
        """
        Test that valid arguments gets set into object

        """
        family = self.family
        new_family = [Male(25), Female(24)]

        family.family_members = new_family
        family.inntekt = inntekt
        family.antall_biler = antall_biler

        assert family.family_members == new_family
        assert family.inntekt == str(inntekt)
        assert family.antall_biler == str(antall_biler)

    @pt.mark.parametrize('invalid_family', [Male(17), Female(17), [Male(17), Female(17)]])
    def test_family_cannot_exist_without_guardianship(self, invalid_family):
        """
        Test that Family object cannot exist without guardianship, i.e. must have atleast one
        person over 18 years.

        """
        with pt.raises(DomainError):
            Family(invalid_family) if isinstance(invalid_family, list) else Family([invalid_family])

    def test_add_family_members_method(self):
        """
        Test the add_family_members method in Family class

        """
        family = self.family
        children = [Male(age=12), Female(age=10)]
        family.add_family_members(children)
        assert len(family.family_members) == 4

        child = Male(age=5)
        family.add_family_members(child)
        assert len(family.family_members) == 5

    def test_get_properties_method(self):
        """
        Test get properties method in Family class

        """
        family = [Male(age=48), Female(age=45, pregnant='1'), Female(age=17), Male(age=13, sfo='1'),
                  Female(age=5, kinder_garden='1')]
        properties = {'inntekt': '1489000', 'antall_biler': '2'}
        for i, member in enumerate(family):
            for key, value in member.__dict__.items():
                if "id" not in key:
                    properties.update({key[1:] + str(i): value})

        fam = Family(family, income=1489000, cars=2)
        assert fam.sifo_properties() == properties

    def test_that_id_not_in_sifo_properties(self):
        """
        Test that sifo_properties() does not include entity id's

        """
        prop = self.family.sifo_properties()
        assert 'id' not in prop.keys()

    def test_family_object_id_are_uuid4(self):
        """
        Test that all entity ids are uuid4 compatible

        """
        assert UUID(str(self.family.id))
