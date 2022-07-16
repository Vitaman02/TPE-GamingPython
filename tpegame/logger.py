import logging
import os
import sys
from pathlib import Path

# Get current path
cwd = Path(__file__).parent
logs_path = cwd.joinpath("logs")


class GameLogger:
    def __init__(self, level: int = logging.INFO) -> None:
        # Setup logger
        logger = logging.getLogger("TPEGAME")
        logger.setLevel(level)

        # Setup formatter
        formatting = "[%(asctime)s] [%(name)s] [%(levelname)s] :: %(message)s"
        formatter = logging.Formatter(formatting, datefmt="%Y-%m-%d %H:%M:%S")

        # Set file handlers
        next_file = self._find_next_log_id(logs_path)
        file_path = logs_path.joinpath(next_file).absolute()
        file_handler = logging.FileHandler(str(file_path))

        # Set stream handler
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

        self.logger = logger

    def __call__(self, message: str, level: int | None = None) -> None:
        self.log(message, level)

    def _find_next_log_id(self, path: str | Path) -> str:
        """Find what the next filename for logs should be"""

        # Check if path exists
        path = str(path)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Path {path} does not exist")

        # Find all the filenames and find the next id
        file_ids = [file.split("-")[0] for file in os.listdir(path)]
        if not file_ids:
            return "1-tpegame.log"

        max_id = max(map(int, file_ids))
        return f"{max_id + 1}-tpegame.log"

    def log(self, message: str, level: int | None = None) -> None:
        """Format message and log"""

        if not level:
            level = self.logger.level

        self.logger.log(level, message)
        self.message = message
