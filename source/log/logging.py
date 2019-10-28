# -*- coding: utf-8 -*-

"""
Implementation of logging functionality for the application

"""

__author__ = 'Samir Adrik'
__email__ = 'samir.adrik@gmail.com'

import os

from loguru import logger as log

from source.util import Assertor


def logging(file_path=None, file_name="application.log"):
    """
    loguru logger method that produces one logger per. call to method

    Parameters
    ----------
    file_path    : str
                   file path to store all .log files, default is __file__, i.e.
                   directory  from which the call to the method was invoked
    file_name    : str
                   name of log file

    Returns
    -------
    out     : loguru._logger.Logger

    """
    try:
        Assertor.assert_data_types([file_path, file_name], [(type(None), str), str])
        file = __file__ if not file_path else file_path
        log_dir = os.path.dirname(file) + "/logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log.add(log_dir + "/application.log")
        return log
    except Exception as log_exception:
        raise OSError("an error occurred with: {}".format(log_exception))


LOGGER = logging()
