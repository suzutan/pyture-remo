# -*- coding: utf-8 -*-

from typing import List, NoReturn
from .remo import Remo
from .api import Api
import unittest
import requests_mock
from pathlib import Path


class TestRemo(unittest.TestCase):

    def mock_init(self):
      api = Api().instance()
      api.init()
      api.api_endpoint = "mock://remo.example.com"
      adapter: requests_mock.Adapter = requests_mock.Adapter()
      api.session.mount('mock', adapter)

      with (Path(".") / "pyture_remo" / "testdata" / "devices.json").open("r") as f:
        adapter.register_uri('GET', f"{api.api_endpoint}/1/devices", text=f.read())
      with (Path(".") / "pyture_remo" / "testdata" / "appliances.json").open("r") as f:
        adapter.register_uri('GET', f"{api.api_endpoint}/1/appliances", text=f.read())

    def test_find_device(self):
        self.mock_init()
        # testing
        remo = Remo("test token")
        self.assertEqual(remo.device(name="test_device").id, "585b5f2c-4972-4acf-af48-57bdf2ac7fb2")

    def test_find_appliances(self):

        self.mock_init()
        # testing
        remo = Remo("test token")
        self.assertEqual(remo.appliance(name="light").id, "31e845ce-ef54-4331-a180-fdd09531b867")
