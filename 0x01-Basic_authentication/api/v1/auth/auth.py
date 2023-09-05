#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import TypeVar


class Auth():
    """
    Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth method

        Return:
          - bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header method

        Return:
          - str
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user method

        Return:
          - User object
        """
        return None