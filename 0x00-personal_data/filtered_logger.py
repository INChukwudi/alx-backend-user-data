#!/usr/bin/env python3

"""
Module containing the filter_datum function
"""

import re


def filter_datum(fields, redaction, message, separator) -> str:
    for field in fields:
        pat = r'({}=)([^{}]+{})'.format(field, separator, separator)
        message = re.sub(pat, r'\1{}{}'.format(redaction, separator), message)
    return message
