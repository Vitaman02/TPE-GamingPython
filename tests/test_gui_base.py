from unittest import TestCase

from tpegame.gui.base import BaseElement


# TODO This class will be implemented in a later issue,
# TODO so no need to write tests right now.
class GUIBaseElementTest(TestCase):
    def test_gui_base_element(self):
        """Test BaseElement"""

        base = BaseElement()

        # Check class attributes
        self.assertEqual(base.clickable, False)
        self.assertEqual(base.path, None)
        self.assertEqual(base.width, None)
        self.assertEqual(base.height, None)
