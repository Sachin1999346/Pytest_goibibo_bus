import datetime
import time

import pytest

from Library.excle_lib import ReadExcle
from POM.bus_module import BusPage
from Library.config import Configuration


class TestBusPage:
    obj = ReadExcle()
    data = obj.read_test_data(Configuration.BUS_TEST_DATASHEET)

    @pytest.mark.parametrize("From_t, To_t, full_name, age,gender, email,number_,card_number_1, cvv_number, card_name",data)
    def test_click_login_link(self, init_driver, From_t, To_t, full_name,age,gender, email, number_,card_number_1, cvv_number, card_name):
        global driver
        try:
            driver = init_driver
            bus = BusPage(driver)
            bus.TC_Bus_002()
            bus.TC_Bus_003(From_t)
            bus.TC_Bus_005(To_t)
            bus.TC_Bus_008()
            bus.TC_Bus_009()
            bus.TC_Bus_014()

            bus.TC_Bus_016()
            bus.TC_Bus_017()
            bus.TC_Bus_018()
            bus.TC_Bus_019()
            bus.TC_Bus_020()
            bus.TC_Bus_021()
            bus.TC_Bus_022()
            bus.TC_Bus_023()
            bus.TC_Bus_024()
            bus.TC_Bus_025()
            bus.TC_Bus_026()
            bus.TC_Bus_027()

            bus.TC_Bus_029()
            bus.TC_Bus_030()
            bus.TC_Bus_031()
            bus.TC_Bus_032()
            bus.TC_Bus_033()

            # bus.TC_Bus_034()
            bus.TC_Bus_035()
            bus.TC_Bus_036(full_name)
            bus.TC_Bus_037(age)
            bus.TC_Bus_038(gender)
            bus.TC_Bus_040(email)
            bus.TC_Bus_041(number_)
            # bus.TC_Bus_042()
            bus.TC_Bus_043()

            bus.TC_Bus_044()
            bus.TC_Bus_045(card_number_1)
            bus.TC_Bus_046()
            bus.TC_Bus_047()
            bus.TC_Bus_048()
            bus.TC_Bus_049()
            bus.TC_Bus_050(cvv_number)
            bus.TC_Bus_051(card_name)
            bus.TC_Bus_052()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOTS_PATH+name)
            raise err_msg





