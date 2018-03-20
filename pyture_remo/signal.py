from .api import Api
from .base import Base


class Signal(Base):

    def __str__(self):
        return self.name

    def __init__(self, id: str, name: str = None, image: str = None):
        self.id: str = id
        self.name: str = name
        self.image: str = image
        self.api: Api = Api.instance()

    def send(self) -> dict:
        return self.api.post(path=f"/signals/{self.id}/send")
