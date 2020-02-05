# -*- coding: utf-8 -*-

import unittest
from pathlib import Path

import requests_mock

from .api import Api
from .remo import Remo


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
        device, found = remo.device(name="test_device")

        self.assertTrue(found)
        self.assertEqual(device.id, "585b5f2c-4972-4acf-af48-57bdf2ac7fb2")

    def test_find_appliances(self):
        self.mock_init()
        # testing
        remo = Remo("test token")
        appliance, found = remo.appliance(name="light")
        self.assertTrue(found)

        self.assertEqual(appliance.id, "31e845ce-ef54-4331-a180-fdd09531b867")
