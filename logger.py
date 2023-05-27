from logging import Formatter, Logger, StreamHandler, getLogger


LOG_FORMAT = "%(asctime)s - [%(levelname)s] - %(message)s"


def get_stream_handler(level: str = "INFO") -> StreamHandler:
    stream_handler = StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(Formatter(LOG_FORMAT))
    return stream_handler


def get_logger(name: str, level: str = "INFO") -> Logger:
    logger = getLogger(name)
    logger.setLevel(level)
    logger.addHandler(get_stream_handler(level))
    return logger
