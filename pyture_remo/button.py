# -*- coding: utf-8 -*-

from .api import Api


class Button:

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __init__(self, appliance_id: str, appliance_type: str, name: str = None, image: str = None, label: str = None):
        self.appliance_id: str = appliance_id
        self.appliance_type: str = appliance_type
        self.name: str = name
        self.image: str = image
        self.label: str = label
        self.api: Api = Api.instance()

    def send(self):
        self.api.post(path=f"/1/appliances/{self.appliance_id}/{self.appliance_type}", data={"button": self.name})
