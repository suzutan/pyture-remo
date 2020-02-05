# -*- coding: utf-8 -*-

import requests
from typing import List, NoReturn


class Api:
    _instance = None
    token: str = None
    api_endpoint: str = "https://api.nature.global"
    session: requests.Session = None

    @staticmethod
    def instance():
        if not hasattr(Api, "_instance"):
            Api._instance = Api()
        return Api._instance

    def __new__(cls):
        if cls._instance is None:
            cls.stat: List = []
            cls._instance: Api = object.__new__(cls)
        return cls._instance

    def init(self, token: str = ""):

        # sessionがtest内で初期化済の場合は新しく生成しない
        if self.session is None:
            self.session: requests.Session = requests.session()
        self.session.headers["Authorization"] = f"Bearer {token}"

        return self

    def get(self, path: str) -> dict:
        result = self.session.get(f"{self.api_endpoint}{path}")
        result.raise_for_status()
        return result.json()

    def post(self, path: str, data: dict = None) -> dict:
        result = self.session.post(f"{self.api_endpoint}{path}", data=data)

        result.raise_for_status()
        return result.json()


Api()
