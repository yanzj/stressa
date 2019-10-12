# -*- coding: utf-8 -*-

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from source.exception import BaseClassCannotBeInstantiated
from source.log import logger
from uuid import uuid4
from abc import ABC


class Entity(ABC):
    """
    abstract base entity class

    """

    def __init__(self):
        """
        Constructor / Instantiate the class. Only one property, i.e. id given by uuid4

        """
        logger.info(
            "trying to create entity: '{}'".format(self.__class__.__name__))

        if type(self) == Entity:
            try:
                raise BaseClassCannotBeInstantiated(
                    "abstract base class '{}' cannot be instantiated".format(
                        self.__class__.__name__))
            except Exception as exp:
                logger.exception(exp)
                raise exp

        self._id = str(uuid4())

    @property
    def id(self):
        """
        Id getter

        """
        return self._id
