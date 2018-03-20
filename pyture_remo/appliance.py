# -*- coding: utf-8 -*-

from .signal import Signal
from typing import List


class Appliance:

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nickname}"

    def __init__(self, data: dict):
        self.id = data["id"]
        self.model = data["model"]
        self.nickname = data["nickname"]
        self.image = data["image"]
        self.type = data["type"]
        self.settings = data["settings"]
        self.aircon = data["aircon"]
        self.signals: List = [Signal(**signal) for signal in data["signals"]]

    def find_signal(self, name: str) -> Signal:
        result = list(filter(lambda x: name == x.name, self.signals))

        if not len(result):
            raise ValueError(name)

        return result[0]

    def find_signals(self) -> List[Signal]:
        return self.signals
