# -*- coding: utf-8 -*-


class Device:

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __init__(self, data: dict):
        self.name: str = data["name"]
        self.id: str = data["id"]
        self.created_at: str = data["created_at"]
        self.updated_at: str = data["updated_at"]
        self.firmware_version: str = data["firmware_version"]
        self.temperature_offset: str = data["temperature_offset"]
        self.humidity_offset: str = data["humidity_offset"]
        self.firmware_version: str = data["firmware_version"]
        self.firmware_version: str = data["firmware_version"]
        self.newest_events: dict = data["newest_events"]
        self.humidity: float = data["newest_events"]["hu"]["val"]
        self.temperature: float = data["newest_events"]["te"]["val"]

    def get_temperature(self) -> float:
        return self.temperature

    def get_humidity(self) -> float:
        return self.humidity
