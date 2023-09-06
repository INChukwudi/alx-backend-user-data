#!/usr/bin/env python3
"""
Basic Auth Module
"""

from typing import TypeVar

from .auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class
    Inherits from the Auth class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        extract_base64_authorization_header

        Return:
          - str
        """
        return None

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        decode_base64_authorization_header

        Return:
          - str
        """
        return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        extract_user_credentials

        Return:
          - (str, str)
        """
        return (None, None)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        user_object_from_credentials

        Return:
          - str
        """
        return None
