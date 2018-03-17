from .device import Device
from .api import Api
from typing import List
from .appliance import Appliance
from .base import Base


class Remo(Base):

    def __init__(self, token: str):
        self.devices: List[Device] = None
        self.appliances: List[Appliance] = None
        self.id: str = None
        self.nickname: str = None
        self.api: Api = Api(token=token)

        self.fetch_user()
        self.fetch_devices()
        self.fetch_appliances()

    def fetch_user(self) -> None:
        result: dict = self.api.get(path="/users/me")
        self.id = result["id"]
        self.nickname = result["nickname"]

    def fetch_devices(self) -> None:
        result: dict = self.api.get(path="/devices")

        self.devices = [Device(device_data=device) for device in result]

    def fetch_appliances(self) -> None:
        result: List[dict] = self.api.get(path="/appliances")
        self.appliances = [Appliance(appliance_data=appliance) for appliance in result]
