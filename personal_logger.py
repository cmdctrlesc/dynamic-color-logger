import logging

class CustomFormatter(logging.Formatter):

    def __init__(self, color):
        self.color = color

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    green =  "\u001b[32m"
    blue = "\u001b[36m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    COLORS = {
        "red": red + format + reset,
        "yellow": yellow + format + reset,
        "blue": blue + format + reset,
        "green": green + format + reset
    }

    def format(self, record):
        log_fmt = self.COLORS.get(self.color)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)



def create_personal_logger(color):

    logger = logging.getLogger("my personal " + color + " logger")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter(color))
    logger.addHandler(ch)

    return logger

