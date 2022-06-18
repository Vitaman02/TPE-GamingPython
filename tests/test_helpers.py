import json
import os
from pathlib import Path
from unittest import TestCase

from tpegame.helpers import Colors, load_settings


class HelpersTest(TestCase):
    PATH = Path(__file__).parent.parent
    SETTINGS_PATH = os.path.join(PATH, "tpegame", "resources", "settings.json")

    # Expected JSON keys with mock values
    EXPECTED_JSON = {
        "fps": 1,
        "width": 1,
        "height": 1,
        "title": "mock title",
        "background": "mock background",
        "duck_left": "mock duck left",
        "duck_right": "mock duck right",
    }

    ANNOTATIONS = {
        "WHITE": (255, 255, 255),
        "BLACK": (0, 0, 0),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
    }

    def setUp(self):
        self.JSON_KEYS = self.EXPECTED_JSON.keys()
        self.ANNOTATION_KEYS = self.ANNOTATIONS.keys()

    def test_settings_keys(self):
        """Test that all the expected keys in the settings exist."""

        # Load settings JSON
        with open(self.SETTINGS_PATH) as file:
            settings = json.load(file)

        # Check JSON keys
        self.assertEqual(settings.keys(), self.JSON_KEYS)

    def test_load_settings(self):
        """Test the load_settings function."""

        # Check settings keys
        settings = load_settings()
        self.assertEqual(settings.keys(), self.JSON_KEYS)

    def test_colors_dataclass(self):
        """Test the colors from the Colors dataclass."""

        # Check Colors fields
        fields = Colors.__annotations__.keys()
        self.assertEqual(fields, self.ANNOTATION_KEYS)

        # Check color values
        self.assertEqual(Colors.WHITE, (255, 255, 255))
        self.assertEqual(Colors.BLACK, (0, 0, 0))
        self.assertEqual(Colors.RED, (255, 0, 0))
        self.assertEqual(Colors.GREEN, (0, 255, 0))
        self.assertEqual(Colors.BLUE, (0, 0, 255))
