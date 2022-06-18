from unittest import TestCase, mock

from pygame import Surface

from tpegame.gui.background import Background

MOCK_BACKGROUND_SIZE = 500, 500


def mock_load_image(*args, **kwargs):
    return Surface(MOCK_BACKGROUND_SIZE)


class GUIBackgroundTest(TestCase):
    MOCK_PATH = "./path/to/background.jpg"

    @classmethod
    def setUpClass(cls) -> None:
        width, height = MOCK_BACKGROUND_SIZE

        # Mock the image load function from pygame
        with mock.patch("pygame.image.load", mock_load_image):
            cls.background = Background(cls.MOCK_PATH, width, height)

    def test_gui_background_size(self):
        """Test Background's size"""

        # Check background size after scaling
        size = self.background.scaled.get_size()
        self.assertEqual(size, MOCK_BACKGROUND_SIZE)

    def test_gui_background_str(self):
        """Test __str__ and __repr__ methods"""

        # Check __str__ and __repr__ methods
        clickable = self.background.clickable
        path = self.background.path
        string = f"<Background({clickable=}, {path=})>"
        self.assertEqual(str(self.background), string)
        self.assertEqual(repr(self.background), string)

    def test_gui_background_clickable(self):
        """Test if background is clickable"""

        self.assertEqual(self.background.clickable, False)
