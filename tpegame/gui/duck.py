import pygame
from pygame.sprite import Sprite


class DuckSprite(Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.clicked = False

    def is_clicked(self, position) -> bool:
        return bool(self.rect.collidepoint(position))

    def __str__(self) -> str:
        return f"<DuckSprite({self.image=}, {self.clicked=})>"

    def __repr__(self) -> str:
        return self.__str__()
