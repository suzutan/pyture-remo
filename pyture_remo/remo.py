# -*- coding: utf-8 -*-

from .device import Device
from .api import Api
from typing import List, NoReturn
from .appliance import Appliance


class Remo:

    def __init__(self, token: str):
        self._id: str = None
        self._nickname: str = None
        self._devices:  List[Device] = []
        self._appliances:  List[Appliance] = []
        self._api: Api = Api()
        self._api.init(token=token)
        self.sync()

    def sync(self) -> NoReturn:
        self._devices = \
            [Device(data=device) for device in self._api.get(path="/1/devices")]
        self._appliances = \
            [Appliance(data=appliance) for appliance in self._api.get(path="/1/appliances")]

    def devices(self) -> List[Device]:
        return self._devices

    def device(self, name: str) -> Device:
        result = list(filter(lambda x: name == x.name, self._devices))

        if not len(result):
            raise ValueError(name)

        return result[0]

    def appliances(self) -> List[Appliance]:
        return self._appliances

    def appliance(self, name: str) -> Appliance:
        result = list(filter(lambda x: name == x.nickname,self._appliances))

        if not len(result):
            raise ValueError(name)

        return result[0]
