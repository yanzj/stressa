# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'


class Evaluator:
    """
    Class for evaluating Python objects

    """

    @staticmethod
    def evaluate_data_type(dtype_dict):
        """
        Method that evaluates the type of objects in dictionary of {object: type}. Raises
        TypeError if not match.

        Parameters
        ----------
        dtype_dict    : dictionary
                        dict of object: type(s) to be evaluated
        """
        for obj, t in dtype_dict.items():
            if not isinstance(obj, t):
                raise TypeError(
                    "expected type '{}', got '{}' instead".format(t, type(obj).__name__))

    @staticmethod
    def evaluate_possible_arguments(arg_list):
        """
        Method that evaluates the object in dictionary of {object: [name, possible]} to see if
        object is in possibility. Raises ValueError if not match.

        Parameters
        ----------
        arg_list    : dictionary
                      dict of {object: [name, possible]} to be evaluated

        """
        for arg, ls in arg_list.items():
            name, possible = ls[0], ls[1]
            if arg not in possible:
                raise ValueError(
                    "only possible values for '{}' are {}".format(name, possible))