class Appliance:

    def __str__(self) -> str:
        return "\n".join([
            f"{x.ljust(20)}= {getattr(self, x)}" for x in [
                y for y in dir(self) if not y.startswith("__") and not y.endswith("__")
            ]
        ])

    def __init__(self, appliance_data: dict):
        self.id = appliance_data["id"]
        self.model = appliance_data["model"]
        self.nickname = appliance_data["nickname"]
        self.image = appliance_data["image"]
        self.type = appliance_data["type"]
        self.settings = appliance_data["settings"]
        self.aircon = appliance_data["aircon"]
        self.signals = appliance_data["signals"]
