import json
import os
from dataclasses import dataclass


@dataclass
class Colors:
    """Colors in RGB for pygame."""

    WHITE: tuple[int] = (255, 255, 255)
    BLACK: tuple[int] = (0, 0, 0)
    RED: tuple[int] = (255, 0, 0)
    GREEN: tuple[int] = (0, 255, 0)
    BLUE: tuple[int] = (0, 0, 255)


def load_settings() -> dict[str, str | int]:
    """Loads the project's settings.

    Returns:
        A dictionary with the project settings.
    """

    # Get this file's path
    cwd = os.path.abspath(os.path.dirname(__file__))
    resources = os.path.join(cwd, "resources")

    # Load settings
    with open(os.path.join(resources, "settings.json")) as file:
        settings = json.load(file)

    # Load background image path
    settings["background"] = os.path.join(resources, "sprites", settings["background"])

    # Load duck sprites
    settings["duck_right"] = os.path.join(resources, "sprites", settings["duck_right"])
    settings["duck_left"] = os.path.join(resources, "sprites", settings["duck_left"])

    # Load background music
    settings["background_music"] = os.path.join(
        resources,
        "music",
        settings["background_music"],
    )

    return settings
