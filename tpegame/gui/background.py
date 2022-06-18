from os import PathLike

import pygame
from pygame import Surface


class Background:
    def __init__(self, path: str | PathLike, width: int, height: int):
        self.path = path
        self.width = width
        self.height = height
        self.scaled = self.scale(path, width, height)
        self.clickable = False

    @staticmethod
    def scale(path: str | PathLike, width: int, height: int) -> Surface:
        """Scale image to the size of the window."""

        image = pygame.image.load(path, "background")
        return pygame.transform.scale(image, (width, height))

    def __str__(self) -> str:
        clickable = self.clickable
        path = self.path
        return f"<Background({clickable=}, {path=})>"

    def __repr__(self) -> str:
        return self.__str__()
