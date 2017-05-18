import logging
logging.basicConfig(filename="log1.txt", level=logging.DEBUG, 
	format="%(asctime)s->%(levelname)s->%(message)s")
logging.info("**********************************Program started")
logging.info("Inofrmation message")
logging.debug("debug message")
logging.warn("warn message")
logging.exception("except message")
logging.error("error message")