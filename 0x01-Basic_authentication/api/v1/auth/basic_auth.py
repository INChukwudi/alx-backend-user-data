#!/usr/bin/env python3
"""
Basic Auth Module
"""

import base64
from typing import TypeVar

from .auth import Auth
from models.user import User


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

        try:
            return base64.b64decode(base64_authorization_header) \
              .decode("utf-8")
        except UnicodeDecodeError:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        extract_user_credentials

        Return:
          - (str, str)
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        try:
            first_index = decoded_base64_authorization_header.index(":")
            email = decoded_base64_authorization_header[:first_index]
            pwd = decoded_base64_authorization_header[first_index + 1:]
            return (email, pwd)
        except ValueError:
            return (None, None)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        user_object_from_credentials

        Return:
          - str
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        if User.count == 0:
            return None

        try:
            user_list = User.search({"email": user_email})
            if len(user_list) == 0:
                return None

            if not user_list[0].is_valid_password(user_pwd):
                return None

            return user_list[0]
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user

        Return:
           - User object
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_str = self.extract_base64_authorization_header(auth_header)
        if base64_str is None:
            return None

        dec_b64_str = self.decode_base64_authorization_header(base64_str)
        if dec_b64_str is None:
            return None

        user_cred = self.extract_user_credentials(dec_b64_str)
        if user_cred is (None, None):
            return None

        return self.user_object_from_credentials(user_cred[0], user_cred[1])

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
