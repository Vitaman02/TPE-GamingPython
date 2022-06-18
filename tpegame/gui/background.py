from os import PathLike

import pygame


class Background:
    def __init__(self, path: str | PathLike, width: int, height: int):
        self.path = path
        self.width = width
        self.height = height
        self.scaled = self.scale(width, height)

    @staticmethod
    def scale(path: str | PathLike, width: int, height: int) -> None:
        """Scale image to the size of the window."""
        image = pygame.image.load(path, "background")
        return pygame.transform.scale(image, (width, height))
