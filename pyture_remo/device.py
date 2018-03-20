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
        self.humidity: dict = {
            "value": data["newest_events"]["hu"]["val"],
            "created_at": data["newest_events"]["hu"]["created_at"],
        }
        self.temperature: dict = {
            "value": data["newest_events"]["te"]["val"],
            "created_at": data["newest_events"]["te"]["created_at"],
        }

    def get_temperature(self) -> float:
        return self.temperature["value"]

    def get_humidity(self) -> float:
        return self.humidity["value"]
