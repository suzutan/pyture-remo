import requests
from .base import Base


class Api(Base):

    def __init__(self, token: str):
        self.session: requests.Session = requests.session()
        self.api_endpoint: str = "https://api.nature.global/1"
        self.session.headers["Authorization"] = f"Bearer {token}"

    def get(self, path: str) -> dict:
        result = self.session.get(f"{self.api_endpoint}{path}")

        result.raise_for_status()
        return result.json()

    def post(self, path: str, data: dict) -> dict:
        result = self.session.post(f"{self.api_endpoint}{path}", data=data)

        result.raise_for_status()
        return result.json()
