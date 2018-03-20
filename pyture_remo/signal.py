# -*- coding: utf-8 -*-

from .api import Api


class Signal:

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __init__(self, id: str, name: str = None, image: str = None):
        self.id: str = id
        self.name: str = name
        self.image: str = image
        self.api: Api = Api.instance()

    def send(self) -> dict:
        return self.api.post(path=f"/1/signals/{self.id}/send")
