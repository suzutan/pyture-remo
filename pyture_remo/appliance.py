from .base import Base
from .signal import Signal
from typing import List


class Appliance(Base):

    def __init__(self, data: dict):
        self.id = data["id"]
        self.model = data["model"]
        self.nickname = data["nickname"]
        self.image = data["image"]
        self.type = data["type"]
        self.settings = data["settings"]
        self.aircon = data["aircon"]
        self.signals: List = [Signal(**signal) for signal in data["signals"]]
