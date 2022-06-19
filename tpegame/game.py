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
from tpegame.gui.duck import Duck


class Game:
    """A class to represent the game running.

    Attibutes:
        settings (dict): The game's settings.
        FPS (int): The frame rate of the game.
        WIDTH (int): Constant to set window's width.
        HEIGHT (int): Constant to set window's height.
        SIZE (:obj:`tuple` of :obj:`int`): A tuple with the width and height.
        WIN (:obj:`Surface`): The window the game is played on.
        BACKGROUND (:obj:`Background`): The background of the game.
        start_time (float): Time the game started at.
    """

    def __init__(self, width: int = None, height: int = None, title: str = None):
        self.settings = helpers.load_settings()

        # Set constants
        self.FPS = self.settings["fps"]
        self.WIDTH = self.settings["width"] if not width else width
        self.HEIGHT = self.settings["height"] if not height else height
        self.SIZE = (self.WIDTH, self.HEIGHT)
        self.WIN = pygame.display.set_mode(self.SIZE)
        self.BACKGROUND = Background(self.settings["background"], *self.SIZE).scaled

        # Set window background image
        self.WIN.blit(self.BACKGROUND, (0, 0))

        self.start_time = None
        self.duck_width = 150
        self.duck_height = 150
        self.ducks = self.setup_ducks()

        # Set window title
        title = self.settings["title"] if not title else title
        pygame.display.set_caption(title)

    def setup_ducks(self, duck_amount: int = 10) -> list:
        """Sets up duck sprite on the game window"""

        # Set ducks per row
        # ? Can be optimized, spaggheti
        rows = ["duck_right", "duck_left"]
        increments = [self.duck_width, -self.duck_width]
        positions = [
            (-self.duck_width, self.duck_height),
            (self.WIDTH, self.HEIGHT - self.duck_height * 2),
        ]
        ducks = []
        for index, row in enumerate(rows):
            increment = increments[index]
            for _ in range(duck_amount):
                # Create Duck sprite
                duck = Duck(
                    self.settings[row],
                    self.duck_width,
                    self.duck_height,
                ).scaled

                # Draw duck on window
                position = positions[index][0] + increments[index], positions[index][1]
                self.WIN.blit(duck, position)
                increments[index] += increment
                ducks.append(duck)

        return ducks

    def handle_event(self, event) -> None:
        """Handles pygame events.

        Events like keyboard key presses,
        mouse clicks and movement is handled in this method.
        """

        # Exit safely the game on QUIT
        if event.type == pygame.QUIT:
            raise PygameQuit("Exit the game loop.")

        # TODO handle duck click
        return

    def start_background_music(self) -> None:
        """Starts the background song"""

        pygame.mixer.init()
        pygame.mixer.music.load(self.settings["background_music"])
        pygame.mixer.music.play(-1)

    def stop_background_music(self) -> None:
        """Stop playing background music"""

        pygame.mixer.music.stop()

    def start(self) -> None:  # pragma: no cover
        """Starts the game loop"""

        # Set start time
        self.start_time = time.time()

        # Setup background music
        self.start_background_music()

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

    def draw_window(self) -> None:  # pragma: no cover
        """Draws frames for the game"""

        pygame.display.update()

    def __str__(self) -> str:
        width, height = self.SIZE
        start_time = self.start_time
        return f"<Game({width=}, {height=}, {start_time=})>"

    def __repr__(self) -> str:
        return self.__str__()


def main() -> None:  # pragma: no cover
    """Main method to start the game"""

    game = Game()
    game.start()


if __name__ == "__main__":  # pragma: no cover
    main()
