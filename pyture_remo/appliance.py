from .base import Base


class Appliance(Base):

    def __init__(self, appliance_data: dict):
        self.id = appliance_data["id"]
        self.model = appliance_data["model"]
        self.nickname = appliance_data["nickname"]
        self.image = appliance_data["image"]
        self.type = appliance_data["type"]
        self.settings = appliance_data["settings"]
        self.aircon = appliance_data["aircon"]
        self.signals = appliance_data["signals"]
