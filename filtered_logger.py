#!/usr/bin/env python3
"""
    filtered_logger mod
"""
from typing import List
import re
import logging
import mysql.connector
from os import getenv

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns the log message obfuscated """
    for field in fields:
        regex = r'{}=.*?{}'.format(field, separator)
        repl_str = '{}={}{}'.format(field, redaction, separator)
        message = re.sub(regex, repl_str, message)
    return message


