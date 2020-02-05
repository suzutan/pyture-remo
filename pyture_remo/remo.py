# -*- coding: utf-8 -*-

from .device import Device
from .api import Api
from typing import List, NoReturn, Optional, overload
from .appliance import Appliance


class Remo:

    def __init__(self, token: str):
        self.id: str = None
        self.nickname: str = None
        self.devices: List[Device] = []
        self.appliances: List[Appliance] = []
        self.api: Api = Api().instance()
        self.api.init(token=token)
        self.sync()

    def sync(self) -> NoReturn:
        new_device_json: dict = self.api.get(path="/1/devices")
        new_devices: List[Device] = []
        for new_device in new_device_json:
            find, device_result = self.device(_id=new_device["id"])
            if find:
                device_result.update(new_device)
                new_devices.append(device_result)
            else:
                new_devices.append(Device(data=new_device))
        self.devices = new_devices

        new_appliance_json: dict = self.api.get(path="/1/appliances")
        new_appliances: List[Appliance] = []
        for new_appliance in new_appliance_json:
            find, appliance_result = self.appliance(_id=new_appliance["id"])
            if find:
                appliance_result.update(new_appliance)
                new_appliances.append(appliance_result)
            else:
                new_appliances.append(Appliance(data=new_appliance))
        self.appliances = new_appliances

    @overload
    def device(self, _id: str) -> (bool, Optional[Device]):
        result: Optional[Device] = next(filter(lambda x: _id == x.id, self.devices), None)

        return (result is not None), result

    def device(self, name: str) -> (bool, Optional[Device]):
        result: Optional[Device] = next(filter(lambda x: name == x.name, self.devices), None)

        return (result is not None), result

    @overload
    def appliance(self, _id: str) -> (bool, Optional[Appliance]):
        result: Optional[Appliance] = next(filter(lambda x: _id == x.nickname, self.appliances), None)

        return (result is not None), result

    def appliance(self, name: str) -> (bool, Optional[Appliance]):
        result: Optional[Appliance] = next(filter(lambda x: name == x.nickname, self.appliances), None)

        return (result is not None), result
