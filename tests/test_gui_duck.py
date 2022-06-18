from unittest import TestCase, mock

from pygame import Surface

from tpegame.gui.duck import Duck

MOCK_DUCK_SIZE = 50, 50


def mock_load_image(*args, **kwargs):
    return Surface(MOCK_DUCK_SIZE)


class GUIDuckTest(TestCase):
    MOCK_PATH = "./path/to/duck.jpg"

    @classmethod
    def setUpClass(cls) -> None:
        with mock.patch("pygame.image.load", mock_load_image):
            cls.duck1 = Duck(cls.MOCK_PATH, *MOCK_DUCK_SIZE)
            cls.duck2 = Duck(cls.MOCK_PATH, *MOCK_DUCK_SIZE)

    def test_gui_duck_velocity(self):
        """Test Duck's velocity"""

        self.assertEqual(self.duck1.velocity, 1)
        self.assertEqual(self.duck2.velocity, 1)

    def test_gui_duck_clickable(self):
        """Test if Duck is clickable"""

        self.assertEqual(self.duck1.clickable, True)
        self.assertEqual(self.duck2.clickable, True)

    def test_gui_duck_size(self):
        """Test Duck's size after scaling."""

        self.assertEqual(self.duck1.scaled.get_size(), MOCK_DUCK_SIZE)
        self.assertEqual(self.duck2.scaled.get_size(), MOCK_DUCK_SIZE)

    def test_gui_duck_str(self):
        """Test the __str__ and __repr__ methods"""

        string = "<Duck(id={}, clickable=True, velocity=1)>"
        string_duck1 = string.format(self.duck1.id)
        string_duck2 = string.format(self.duck2.id)

        # Test __str__ method
        self.assertEqual(str(self.duck1), string_duck1)
        self.assertEqual(str(self.duck2), string_duck2)

        # Test __repr__ method
        self.assertEqual(repr(self.duck1), string_duck1)
        self.assertEqual(repr(self.duck2), string_duck2)
