import os
import time

from dotenv import load_dotenv

# Load environment variables
# and disable pygame prompt
load_dotenv()
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = os.getenv("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import pygame

from tpegame import helpers
from tpegame.exceptions import PygameQuit
from tpegame.gui.background import Background
from tpegame.helpers import Colors


class Game:
    """A class to represent the game running.

    Attibutes:
        settings (dict): The game's settings
        WIDTH (int): Constant to set window's width
        HEIGHT (int): Constant to set window's height
        start (float): Time the game started at
    """

    def __init__(self, width: int = None, height: int = None, title: str = None):
        self.settings = helpers.load_settings()

        # Constants
        self.FPS = self.settings["fps"]
        self.WIDTH = self.settings["width"] if not width else width
        self.HEIGHT = self.settings["height"] if not height else height
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.WIN = pygame.display.set_mode(self.SIZE)
        self.BACKGROUND = Background(self.settings["background"], *self.SIZE)

        self.start_time = None

        # Set window title
        title = self.settings["title"] if not title else title
        pygame.display.set_caption(title)

    def handle_event(self, event) -> None:
        """Handles pygame events.

        Events like keyboard key presses,
        mouse clicks and movement is handled
        in this method.
        """

        if event.type == pygame.QUIT:
            raise PygameQuit("Exit the game loop.")
        return

    def start(self) -> None:
        """Starts the game loop"""

        # Set start time
        self.start_time = time.time()

        # Create clock to run frames on specific framerate
        clock = pygame.time.Clock()
        while True:
            # Tick with FPS counter
            clock.tick(self.FPS)

            # Handle game events
            for event in pygame.event.get():
                try:
                    self.handle_event(event)
                except PygameQuit:
                    pygame.quit()
                    return

            # Draw frame
            self.draw_window()

    def draw_window(self) -> None:
        """Draws frames for the game"""

        self.WIN.fill(Colors.WHITE)

        pygame.display.update()

    def __str__(self) -> str:
        return f"<Game({self.WIDTH=}, {self.HEIGHT=}, {self.start_time=})>"

    def __repr__(self) -> str:
        return self.__str__()


def main() -> None:
    """Main method to start the game"""

    game = Game()
    game.start()


if __name__ == "__main__":
    main()
