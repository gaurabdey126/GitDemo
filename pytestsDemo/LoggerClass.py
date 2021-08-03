import inspect
import logging

class Logclass:
    def getlog(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile_tcname.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
