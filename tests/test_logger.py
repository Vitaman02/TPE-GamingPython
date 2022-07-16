import logging
from unittest import TestCase, mock

from tpegame.logger import GameLogger


class MockOS(mock.Mock):
    def __init__(self, files: bool = True, *args, **kwargs):
        super().__init__()
        self.files = files

    def listdir(self, *args, **kwargs):
        if not self.files:
            return []

        return ["1-tpegame.log", "2-tpegame.log"]


class MockFileHandler(mock.Mock):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.level = logging.INFO

        print(args, kwargs)
        # self.path = path


class LoggerTest(TestCase):
    def test_logger(self):
        """Test the logger class"""

        with mock.patch("tpegame.logger.os", MockOS()):
            with mock.patch("tpegame.logger.logging.FileHandler", MockFileHandler):
                logger = GameLogger()
                logger.log("Test message")
                self.assertEqual(logger.message, "Test message")
                self.assertEqual(logger.logger.level, logging.INFO)

    def test_logger_no_files(self):
        """Test logger without returning any files in the diretory"""

        with mock.patch("tpegame.logger.os", MockOS(files=False)):
            with mock.patch("tpegame.logger.logging.FileHandler", MockFileHandler):
                logger = GameLogger()
                logger("Test message")
                self.assertEqual(logger.message, "Test message")
                self.assertEqual(logger.logger.level, logging.INFO)
