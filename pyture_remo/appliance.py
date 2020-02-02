# -*- coding: utf-8 -*-

from .signal import Signal
from typing import List, NoReturn


class Appliance:

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nickname}"

    def __init__(self, data: dict) -> NoReturn:
        self.id: str = data["id"]
        self.model: str = data["model"]
        self.nickname: str = data["nickname"]
        self.name: str = data["nickname"]  # alias for nickname
        self.image: str = data["image"]
        self.type: str = data["type"]
        self.settings: str = data["settings"]
        self.aircon: str = data["aircon"]
        self.signals: List = [Signal(**signal) for signal in data["signals"]]

    def signal(self, name: str) -> Signal:
        result = list(filter(lambda x: name == x.name, self.signals))

        if not len(result):
            raise ValueError(name)

        return result[0]
