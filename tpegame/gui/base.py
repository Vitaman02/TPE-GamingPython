class BaseElement:
    """Base class for drawn elements and sprites.

    This class will represent graphical object in the game.
    """

    def __init__(self):
        # Default clickable value for GUI elements
        # should always be False and set to True manually.
        self.clickable = False
        self.path = None
        self.width = None
        self.height = None
