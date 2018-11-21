"""
some module
"""

import logging
import os
from time import gmtime, strftime

log_filepath = './logs/'


def setup_logger(name, log_file, level=logging.INFO):
    """
    setup the logger

    Usage -
        ::project_code: python
            import logger

    :param str name: name of blah
    :param str log_file: flog file
    :param int level: logging level
    :return: logging object
    """
    '''
    level = logging.INFO
    try:
        os.makedirs(log_filepath)
    except Exception as e:
        pass

    handler = logging.FileHandler(log_filepath + log_file)
    formatter = logging.Formatter(
        '%(asctime)-8s | %(levelname)-6s | %(lineno)4s | %(filename)20s |%(funcName)15s() | %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
    '''
    logging.basicConfig(
    format='%(asctime)-8s | %(levelname)-6s | %(lineno)4s | %(filename)20s |%(funcName)15s() | %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
    )
    return logging

