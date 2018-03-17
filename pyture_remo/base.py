class Base:

    def __str__(self) -> str:
        return "\n".join([
            f"{x.ljust(20)}= {getattr(self, x)}" for x in [
                y for y in dir(self) if not y.startswith("__") and not y.endswith("__")
            ]
        ])
