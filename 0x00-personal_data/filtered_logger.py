#!/usr/bin/env python3

"""
Module containing the filter_datum function
"""

import re


def filter_datum(fields: list[str],
                 redaction: str, message: str, separator: str) -> str:
    """Function performing the redaction on the message"""
    for field in fields:
        pat = r'({}=)([^{}]+{})'.format(field, separator, separator)
        message = re.sub(pat, r'\1{}{}'.format(redaction, separator), message)
    return message
