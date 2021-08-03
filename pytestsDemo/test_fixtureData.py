import pytest


@pytest.mark.usefixtures("data_load")
class TestData:
    def test_profile(self, data_load):
        print("First Name: ", data_load[0])
        print("Second Name: ", data_load[1])
        print("Website: ", data_load[2])
