import logging


def test_logging_demo():
    ### mapping logger, fileHandler, formatter.....same format need to be followed
    logger = logging.getLogger(__name__)  ## need to import logging..."__name__" it will pull the test case name

    fileHandler = logging.FileHandler('logfile_tcname.log') ## logging is mapped to fileHandler which will generate the Log File in the given name

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") ##givin the format for the Log file
    # s is there to capture in string....asctime=time n date, levelname=type of log, name=testcasename, message=msg provided under level name in code

    fileHandler.setFormatter(formatter)  ## passing the formatter in the fileHandler
    logger.addHandler(fileHandler)  ## passing the fileHandler into Logger
    ####### "formatter---->>>>fileHandler---->>>>logger"

    logger.setLevel(logging.INFO)  #### from which hierarchy we need the logs...there can be a requirement where we don't want debug/info..
    #### we can simply put "logging.WARNING" then
    logger.debug("A debug statement is executed !!!!!")
    logger.info("An info statement is executed &^%^$^%$^")
    logger.warning("WARNING WARNING WARNING")
    logger.error("ERROR ERROR ERROR ERROR")
    logger.critical("SHOWSTOPPER BUG")

