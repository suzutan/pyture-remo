# -*- coding: utf-8 -*-

from .device import Device
from .api import Api
from typing import List
from .appliance import Appliance


class Remo:

    def __init__(self, token: str):
        self.devices: List[Device] = None
        self.appliances: List[Appliance] = None
        self.id: str = None
        self.nickname: str = None
        self.api: Api = Api()
        self.api.init(token=token)

    def devices(self) -> List[Device]:
        return [Device(data=device) for device in self.api.get(path="/1/devices")]

    def device(self, name: str) -> Device:
        result = list(filter(lambda x: name == x["name"], self.api.get(path="/1/devices")))

        if not len(result):
            raise ValueError(name)

        return Device(data=result[0])

    def appliances(self) -> List[Appliance]:
        return [Appliance(data=appliance) for appliance in self.api.get(path="/1/appliances")]

    def appliance(self, name: str) -> Appliance:
        result = list(filter(lambda x: name == x["nickname"], self.api.get(path="/1/appliances")))

        if not len(result):
            raise ValueError(name)

        return Appliance(data=result[0])
