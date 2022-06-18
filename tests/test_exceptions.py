from unittest import TestCase

from tpegame.exceptions import PygameQuit


class ExceptionsTest(TestCase):
    def test_pygamequit(self):
        """Test the PygameQuit exception"""

        # Raise class and test result
        try:
            raise PygameQuit("Mock exit game loop.")
        except PygameQuit as e:
            self.assertEqual(e.__class__, PygameQuit)
            self.assertEqual(str(e), "Mock exit game loop.")

        # Check docstring
        self.assertEqual(PygameQuit.__doc__, "Class for exiting the game loop.")
