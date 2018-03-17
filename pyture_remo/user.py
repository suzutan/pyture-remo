from .base import Base


class User(Base):

    def __init__(self, **kwargs):
        self.id: str = kwargs.get("id")
        self.name: str = kwargs.get("name")
        self.superuser: bool = kwargs.get("superuser")
