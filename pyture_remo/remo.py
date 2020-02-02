# -*- coding: utf-8 -*-

from .device import Device
from .api import Api
from typing import List, NoReturn
from .appliance import Appliance


class Remo:

    def __init__(self, token: str):
        self.id: str = None
        self.nickname: str = None
        self.devices:  List[Device] = []
        self.appliances:  List[Appliance] = []
        self.api: Api = Api()
        self.api.init(token=token)
        self.sync()

    def sync(self) -> NoReturn:
        self.devices = \
            [Device(data=device)
             for device in self.api.get(path="/1/devices")]
        self.appliances = \
            [Appliance(data=appliance)
             for appliance in self.api.get(path="/1/appliances")]

    def device(self, name: str) -> Device:
        result = list(filter(lambda x: name == x.name, self.devices))

        if not len(result):
            raise ValueError(name)

        return result[0]

    def appliance(self, name: str) -> Appliance:
        result = list(filter(lambda x: name == x.nickname, self.appliances))
        if not len(result):
            raise ValueError(name)

        return result[0]
