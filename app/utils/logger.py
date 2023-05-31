from loguru import logger

logger.add('py_log_{time}.log', rotation='12:00', retention='30 days')
