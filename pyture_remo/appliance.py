# -*- coding: utf-8 -*-

from typing import List, NoReturn, Optional

from .signal import Signal
from .light import Light
from .tv import TV


class Appliance:

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nickname}"

    def __init__(self, data: dict) -> NoReturn:
        self._set_member(data)

    def update(self, data: dict) -> NoReturn:
        self._set_member(data)

    def _set_member(self, data: dict) -> NoReturn:
        self.id: str = data["id"]
        self.model: dict = data["model"]
        self.nickname: str = data["nickname"]
        self.name: str = data["nickname"]  # alias for nickname
        self.image: str = data["image"]
        self.type: str = data["type"]
        self.settings: dict = data["settings"]
        self.aircon: dict = data["aircon"]
        self.light: Light = Light(self.id, data["light"]) if self.type == "LIGHT" else None
        self.tv: TV = TV(self.id, data["tv"]) if self.type == "TV" else None
        self.signals: List = [Signal(**signal) for signal in data["signals"]]

    def signal(self, name: str) -> (Optional[Signal], bool):
        result: Optional[Signal] = next(filter(lambda x: name == x.name, self.signals), None)

        return result, (result is not None)
