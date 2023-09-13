#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from os import getenv
from typing import List, TypeVar


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
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for i in range(0, len(excluded_paths)):
            try:
                if path.index(excluded_paths[i][:-1]) == 0:
                    return False
            except ValueError:
                continue

        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization header method

        Return:
          - str
        """
        if request is None:
            return None

        if request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user method

        Return:
          - User object
        """
        return None

    def session_cookie(self, request=None):
        """
        session_cookie
        """
        if request is None:
            return None

        if getenv("SESSION_NAME") in request.cookies:
            return request.cookies.get(getenv("SESSION_NAME"))

        return None
