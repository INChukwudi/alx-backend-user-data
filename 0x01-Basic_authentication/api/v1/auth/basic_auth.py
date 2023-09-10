#!/usr/bin/env python3
"""
Basic Auth Module
"""

import base64
from typing import TypeVar

from .auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class
    Inherits from the Auth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        extract_base64_authorization_header

        Return:
          - str
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        needle = "Basic "
        try:
            if authorization_header.index(needle) != 0:
                return None
        except ValueError:
            return None

        return authorization_header[len(needle):]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        decode_base64_authorization_header

        Return:
          - str
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        if not self.__is_base64_string(base64_authorization_header):
            return None

        return base64.b64decode(base64_authorization_header).decode("utf-8")

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        extract_user_credentials

        Return:
          - (str, str)
        """
        return (None, None)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        user_object_from_credentials

        Return:
          - str
        """
        return None

    def __is_base64_string(self, prob_str: str) -> bool:
        """
        __is_base64_string

        Return:
            - bool
        """
        try:
            if isinstance(prob_str, str):
                sb_bytes = bytes(prob_str, 'ascii')
            elif isinstance(prob_str, bytes):
                sb_bytes = sb
            else:
                return False
            return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
        except Exception:
            return False
