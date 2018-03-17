
class User:



    def __str__(self) -> str:
        return "\n".join([
            f"{x.ljust(20)}= {getattr(self, x)}" for x in [
                y for y in dir(self) if not y.startswith("__") and not y.endswith("__")
            ]
        ])
    def __init__(self, **kwargs):
        self.id: str = kwargs.get("id")
        self.name: str = kwargs.get("name")
        self.superuser: bool = kwargs.get("superuser")
