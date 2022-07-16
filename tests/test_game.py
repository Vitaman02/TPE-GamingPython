from collections import namedtuple
from unittest import TestCase, mock

import pygame
from pygame import Surface

from tpegame.exceptions import PygameQuit
from tpegame.game import Game

MockEvent = namedtuple("MockEvent", "type")
MOCK_GAME_SIZE = 500, 500


def mock_load_image(*args, **kwargs):
    return Surface(MOCK_GAME_SIZE)


def mock_set_mode(*args, **kwargs):
    return Surface(MOCK_GAME_SIZE)


def mock_set_caption(*args, **kwargs):
    return


class MockLogger:
    def __init__(self, *args, **kwargs):
        self.message = None
        return

    def __call__(self, *args, **kwargs):
        self.log(*args, **kwargs)
        return

    def log(self, message: str, *args, **kwargs):
        self.message = message


class GameTest(TestCase):
    MOCK_PATH = "./path/to/images/"
    MOCK_GAME_TITLE = "Mock Game"

    @classmethod
    def setUpClass(cls) -> None:
        with (
            mock.patch("pygame.image.load", mock_load_image),
            mock.patch("pygame.display.set_mode", mock_set_mode),
            mock.patch("pygame.display.set_caption", mock_set_caption),
        ):
            with mock.patch("tpegame.game.GameLogger", MockLogger):
                cls.game = Game(*MOCK_GAME_SIZE, cls.MOCK_GAME_TITLE)

    def test_game_handle_event(self):
        """Test Game initialization"""

        # Check that PygameQuit is raised on the quit event
        event_quit = MockEvent(pygame.QUIT)
        event_empty = MockEvent(None)

        try:
            self.game.handle_event(event_quit)
        except PygameQuit as e:
            # Check error message and that the exception is raised
            self.assertEqual(str(e), "Exit the game loop.")

        # Check that nothing happens on no handled events
        self.assertEqual(self.game.handle_event(event_empty), None)

    def test_game_str(self):
        """Test the __str__ and __repr__ methods"""

        width, height = MOCK_GAME_SIZE
        string = f"<Game({width=}, {height=}, start_time=None)>"

        # Check __str__ and __repr__ methods
        self.assertEqual(str(self.game), string)
        self.assertEqual(repr(self.game), string)
