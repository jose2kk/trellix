"""Rapository."""

from typing import Optional


class BaseRepository:
    
    def __init__(self) -> None:
        self.repository = dict()

    def get_element(self, password: str) -> Optional[str]:
        try:
            return self.repository[password]
        except KeyError:
            return None

    def create_element(self, password: str, password_hint: str) -> None:
        self.repository[password] = password_hint


repository = BaseRepository()
