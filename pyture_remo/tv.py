# -*- coding: utf-8 -*-

from typing import List, NoReturn, Optional

from .button import Button

class TV:

    def __str__(self):
        return f"{self.__class__.__name__}: {self.appliance_id}"

    def __init__(self, appliance_id: str, data: dict) -> NoReturn:
        self.appliance_id: str = appliance_id
        self.input: str = data["state"]["input"]
        self.buttons: List = [Button(appliance_id=appliance_id, appliance_type="tv", **button) for button in data["buttons"]]

    def button(self, name: str) -> (Optional[Button], bool):
        result: Optional[Button] = next(filter(lambda x: name == x.name, self.buttons), None)

        return result, (result is not None)
