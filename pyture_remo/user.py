# -*- coding: utf-8 -*-


class User:
    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __init__(self, **kwargs):
        self.id: str = kwargs.get("id")
        self.name: str = kwargs.get("name")
        self.superuser: bool = kwargs.get("superuser")
