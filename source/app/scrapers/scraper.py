# -*- coding: utf-8 -*-

"""
Implementation of base Scraper class

"""

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

from abc import ABC, abstractmethod
from uuid import uuid4
import datetime
import json
import os

from mechanize import Browser

from source.util import Assertor, LOGGER


class Scraper(ABC):
    """
    Scraper superclass

    """

    @staticmethod
    def save_json(file_dict: dict, file_dir: str = "report/json", file_prefix: str = "Info"):
        """
        save information in object to JSON file

        Parameters
        ----------
        file_dict   : dict
                      retrieve information from this object and save to file
        file_dir    : str
                      file directory to save JSON files
        file_prefix  : str
                      title of file

        """
        try:
            Assertor.assert_data_types([file_dir, file_prefix], [str, str])
            try:
                if not os.path.exists(file_dir):
                    os.makedirs(file_dir)
            except Exception as exception:
                raise OSError("creation of dir " + file_dir + " failed with: " + str(exception))
            _json = json.dumps(file_dict, indent=2, separators=(',', ': '),
                               ensure_ascii=False)
            local_time = datetime.datetime.now().isoformat().replace(":", "-").replace(".", "-")
            file = open(os.path.join(file_dir, file_prefix + local_time + ".json"), "w")
            file.write(_json)
            file.close()
        except Exception as json_exception:
            LOGGER.exception(json)
            raise json_exception

    @abstractmethod
    def __init__(self):
        """
        Abstract class, so class cannot be instantiated

        """
        try:
            LOGGER.info("trying to create '{}'".format(self.__class__.__name__))
            super().__init__()
            self._browser = Browser()
            self._browser.set_handle_robots(False)
            self._browser.set_handle_refresh(False)
            self._id_str = str(uuid4())
        except Exception as scraper_exception:
            LOGGER.exception(scraper_exception)
            raise scraper_exception

    @property
    def id_str(self):
        """
        Id getter

        """
        return self._id_str
