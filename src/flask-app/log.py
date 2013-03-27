import logging

def setup_logging(level=logging.INFO):
    if level == logging.DEBUG:
        logging.basicConfig(level=level, format="%(asctime)s [%(levelname)-7s] [line %(lineno)d] %(name)s: %(message)s")
    else:
        logging.basicConfig(level=level, format="%(asctime)s [%(levelname)-7s] %(name)s: %(message)s")


logging.getLogger("extdirect").setLevel(logging.DEBUG)


