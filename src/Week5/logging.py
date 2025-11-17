from logging import getLogger,StreamHandler,Formatter,INFO

logger=getLogger(__name__)
stream_handler=StreamHandler()
logger.setLevel(INFO)

formatter=Formatter("[%(levelname)s]%(asctime)s-%(message)s")
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

logger.debug("Debugメッセージです")
logger.info("Infoメッセージです")
logger.warning("Warningメッセージです")
logger.error("Errorメッセージです")
logger.critical("Criticalメッセージです")

