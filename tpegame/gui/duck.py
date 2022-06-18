import itertools
from os import PathLike

import pygame


class Duck:
    generate_id = itertools.count()
    next(generate_id)

    def __init__(self, path: str | PathLike, width: int, height: int):
        self.path = path
        self.width = width
        self.height = height
        self.scaled = self.scale(path, width, height)
        self.velocity = 1
        self.clickable = True
        self.id = next(self.generate_id)
        self.duck = self.scaled

    def scale(self, path: str | PathLike, width: int, height: int):
        """Scale element to appropriate size"""

        image = pygame.image.load(path, "duck")
        return pygame.transform.scale(image, (width, height))

    def __str__(self) -> str:
        clickable = self.clickable
        velocity = self.velocity
        return f"<Duck(id={self.id}, {clickable=}, {velocity=})>"

    def __repr__(self) -> str:
        return self.__str__()
