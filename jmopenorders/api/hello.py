from ..core.logger import logger


def Hello(name="World") -> str:
    logger.debug("executing hello command")

    return "Hello, {:s}!".format(name)  # TODO: use f-string fr python 3.6+
