#!/usr/bin/env python3
"""
Session Auth Module
"""

import uuid

from .auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth Class definition
    Inherits from Auth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        create_session

        Return:
            - str
        """
        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        s_id = str(uuid.uuid4())
        self.user_id_by_session_id[s_id] = user_id
        return s_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        user_id_for_session_id

        Return:
           - str
        """
        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
