import pytest
from pytestsDemo.LoggerClass import Logclass


@pytest.mark.usefixtures("data_load")
class TestLoggerCalling(Logclass):        ## Inheritance of LoggerClass from the Logger File

    def test_log(self, data_load):
        log = self.getlog()    ## mapping new variable log to main class method
        log.info(data_load[0]) ## need to remove other input(the string ones) as log will not be able to retrieve like PRINT
        log.info(data_load[1])
        log.info(data_load[2])
        print("Website: ", data_load[2])
