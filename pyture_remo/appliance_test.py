# -*- coding: utf-8 -*-

import json
import unittest
from pathlib import Path

from .appliance import Appliance


class TestAppliance(unittest.TestCase):

    def test_find_signal(self):
        with (Path(".") / "pyture_remo" / "testdata" / "appliances.json").open("r") as f:
            appliance_data = json.load(f)
        appliance: Appliance = Appliance(appliance_data[0])
        signal, found = appliance.signal("全灯")

        self.assertTrue(found)
        self.assertEqual(signal.id, "ef0debba-49f1-4b0d-a4b2-0d8ab8dfc4f7")
