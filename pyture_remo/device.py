class Device:

    def __str__(self) -> str:
        return "\n".join([
            f"{x.ljust(20)}= {getattr(self, x)}" for x in [
                y for y in dir(self) if not y.startswith("__") and not y.endswith("__")
            ]
        ])

    def __init__(self, device_data: dict):
        self.name: str = device_data["name"]
        self.id: str = device_data["id"]
        self.created_at: str = device_data["created_at"]
        self.updated_at: str = device_data["updated_at"]
        self.firmware_version: str = device_data["firmware_version"]
        self.temperature_offset: str = device_data["temperature_offset"]
        self.humidity_offset: str = device_data["humidity_offset"]
        self.firmware_version: str = device_data["firmware_version"]
        self.firmware_version: str = device_data["firmware_version"]
        self.humidity: dict = {
            "value": device_data["newest_events"]["hu"]["val"],
            "created_at": device_data["newest_events"]["hu"]["created_at"],
        }
        self.temperature: dict = {
            "value": device_data["newest_events"]["te"]["val"],
            "created_at": device_data["newest_events"]["te"]["created_at"],
        }
