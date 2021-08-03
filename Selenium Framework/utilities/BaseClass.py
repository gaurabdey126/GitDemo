import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    ## for explicit wait
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    ## dropdown selection by text
    def dropdownOptionbyText(self, locator, text):
        dropdown = Select(locator)  # from selenium.webdriver.support.select import Select
        dropdown.select_by_visible_text(text)

    ## Logger details for e2e test case
    def getLog(self):
        loggerName = inspect.stack()[1][3]   ## need to import inspect
        logger = logging.getLogger(loggerName)  ## need to import logging
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)  ## setting level DEBUG, INFO, WARNING, ERROR, CRITICAL
        return logger




