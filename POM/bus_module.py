
import re
import time

from Library.excle_lib import ReadExcle
from Library.config import Configuration


class BusPage:

    obj_1 = ReadExcle()
    locator_reg = obj_1.read_locator(Configuration.BUS_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def TC_Bus_002(self):
        time.sleep(3)
        locator = self.locator_reg["bus_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_003(self, from_txt):
        time.sleep(3)
        pattern = r'[a-zA-Z]+'
        result = re.findall(pattern, from_txt)
        assert result, "invalid from location"
        locator = self.locator_reg["from_txt"]
        self.driver.find_element(*locator).send_keys(from_txt)
        time.sleep(3)
        locator = self.locator_reg["dropdown_1"]
        self.driver.find_element(*locator).click()

    def TC_Bus_005(self, to_txt):
        time.sleep(2)
        pattern = r'[a-zA-Z]+'
        result = re.findall(pattern, to_txt)
        assert result, "invalid To location"
        locator = self.locator_reg["to_txt"]
        self.driver.find_element(*locator).send_keys(to_txt)
        time.sleep(3)
        locator = self.locator_reg["dropdown_2"]
        self.driver.find_element(*locator).click()

    def TC_Bus_007(self):
        locator = self.locator_reg["up_down_arrow_btn"]
        self.driver.find_element(*locator).click()

    def TC_Bus_008(self):
        locator = self.locator_reg["pick_date_txt"]
        self.driver.find_element(*locator).click()
        time.sleep(2)
        # locator = self.locator_reg["next_month_btn"]
        # self.driver.find_element(*locator).click()
        # time.sleep(2)

    def TC_Bus_009(self):
        locator = self.locator_reg["select_date_from_pickdate"]
        self.driver.find_element(*locator).click()

    def TC_Bus_014(self):
        locator = self.locator_reg["Search_bus_btn"]
        self.driver.find_element(*locator).click()

    def TC_Bus_016(self):
        time.sleep(5)
        locator = self.locator_reg["Go_deal_cb"]
        self.driver.find_element(*locator).click()

        locator = self.locator_reg["Live_popular_cb"]
        self.driver.find_element(*locator).click()

        locator = self.locator_reg["free_can_cb"]
        self.driver.find_element(*locator).click()

        locator = self.locator_reg["Top_popular_cb"]
        self.driver.find_element(*locator).click()

        locator = self.locator_reg["Reset_popular"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_017(self):
        locator = self.locator_reg["bus_ac_type"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["bus_non_ac"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["bus_seater_type"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["bus_slepper_type"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["Reset_bustype"]
        self.driver.find_element(*locator).click()
        time.sleep(2)


    def TC_Bus_018(self):
        locator = self.locator_reg["dt_12_mid"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["dt_6_am"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["dt_12_noon"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["dt_6_pm"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["Reset_dt"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_019(self):
        locator = self.locator_reg["at_12_mid"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["at_6_am"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["at_12_noon"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["at_6_pm"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_reg["reset_at"]
        self.driver.find_element(*locator).click()
        time.sleep(2)


    def TC_Bus_020(self):
        locator = self.locator_reg["boarding_all_option"]
        self.driver.find_element(*locator).click()
        time.sleep(2)
        locator = self.locator_reg["Boarding_all_cb"]
        all_check_box = self.driver.find_elements(*locator)
        for check_box in all_check_box:
            check_box.click()
            time.sleep(2)
        locator = self.locator_reg["Boarding_reset"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_Bus_021(self):
        locator = self.locator_reg["Boarding_search"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_022(self):
        locator = self.locator_reg["Dropping_show_all_cb"]
        self.driver.find_element(*locator).click()
        time.sleep(2)
        locator = self.locator_reg["Dropping_all_cb"]
        all_check_box = self.driver.find_elements(*locator)
        for check_box in all_check_box:
            check_box.click()
            time.sleep(2)
        locator = self.locator_reg["Dropping_reset"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_Bus_023(self):
        locator = self.locator_reg["Dropping_search"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_024(self):
        locator = self.locator_reg["Bus_show_all_option"]
        self.driver.find_element(*locator).click()
        time.sleep(2)
        locator = self.locator_reg["Bus_op_all_cb"]
        all_check_box = self.driver.find_elements(*locator)
        for check_box in all_check_box:
            check_box.click()
            time.sleep(2)
        locator = self.locator_reg["Bus_reset"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_Bus_025(self):
        locator = self.locator_reg["Bus_op_search"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_026(self):
        try:
            locator = self.locator_reg["Amentices_show_all_cb"]
            self.driver.find_element(*locator).click()
            time.sleep(2)
            locator = self.locator_reg["Amentices_all_cb"]
            elements = self.driver.find_elements(*locator)
            for element in elements:
                element.click()
                time.sleep(2)
            locator = self.locator_reg["Amentices_reset"]
            self.driver.find_element(*locator).click()
            time.sleep(3)
        except:
            pass

    def TC_Bus_027(self):
        locator = self.locator_reg["sort_by_filt"]
        elements = self.driver.find_elements(*locator)
        for element in elements:
            element.click()
            time.sleep(2)
        self.driver.refresh()
        time.sleep(6)

    def TC_Bus_029(self):
        time.sleep(8)
        locator = self.locator_reg["select_seat_first"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_Bus_030(self):
        locator = self.locator_reg["boarding_point_hinj"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_Bus_031(self):
        locator = self.locator_reg["Dropping_point_time"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_032(self):
        locator = self.locator_reg["select_any_seat"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_Bus_033(self):
        locator = self.locator_reg["continue_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    # def TC_Bus_034(self):
    #     locator = self.locator_reg["yes_trip_insurance"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(2)

    def TC_Bus_035(self):
        time.sleep(6)
        locator = self.locator_reg["no_trip_insu"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_036(self,name_):
        pattern = r'[A-Z][a-z]*'
        result = re.findall(pattern, name_)
        assert result, "invalid full Name"
        locator = self.locator_reg["first_name"]
        self.driver.find_element(*locator).send_keys(name_)

    def TC_Bus_037(self,age):
        if 0<int(age)<200:
            locator = self.locator_reg["age_txt"]
            self.driver.find_element(*locator).send_keys(int(age))
            time.sleep(2)
        else:
            assert False, "invalid Age"

    def TC_Bus_038(self, gender):
        if gender.lower() == "male":
            locator = self.locator_reg["male_btn"]
            self.driver.find_element(*locator).click()
            time.sleep(2)
        else:
            locator = self.locator_reg["female_btn"]
            self.driver.find_element(*locator).click()
            time.sleep(2)

    def TC_Bus_040(self,email_):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email_)
        assert result, "invalid email"
        locator = self.locator_reg["tra_email"]
        self.driver.find_element(*locator).send_keys(email_)
        time.sleep(2)


    def TC_Bus_041(self,mobile_number):
        pattern = r'^[6-9]\d{9}$'
        result = re.findall(pattern, str(int(mobile_number)))
        assert result, "invalid Mobile Number"
        locator = self.locator_reg["tra_mobile"]
        self.driver.find_element(*locator).send_keys(int(mobile_number))
        time.sleep(2)

    # def TC_Bus_042(self):
    #     locator = self.locator_reg["personal_cb"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(2)

    def TC_Bus_043(self):
        locator = self.locator_reg["pay_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(15)

    def TC_Bus_044(self):
        time.sleep(6)
        locator = self.locator_reg["credit_debit"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_045(self, card_number):
        pattern = r'^4[0-9]{12}(?:[0-9]{3})?$'
        result = re.findall(pattern, str(int(card_number)))
        assert result, "invalid Card Number"
        locator = self.locator_reg["card_number_txt"]
        self.driver.find_element(*locator).send_keys(int(card_number))
        time.sleep(2)

    def TC_Bus_046(self):
        locator = self.locator_reg["expiray_month_click"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_047(self):
        locator = self.locator_reg["select_month"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_048(self):
        locator = self.locator_reg["expiray_year_click"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_049(self):
        locator = self.locator_reg["select_year"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def TC_Bus_050(self,cvv):
        pattern = r'^\d{3}'
        result = re.findall(pattern, str(int(cvv)))
        assert result, "invalid CVV Number"
        locator = self.locator_reg["card_cvv_txt"]
        self.driver.find_element(*locator).send_keys(int(cvv))
        time.sleep(2)

    def TC_Bus_051(self,name_on_card):
        pattern = r'[A-Z][a-z]*'
        result = re.findall(pattern, name_on_card)
        assert result, "invalid Card Name"
        locator = self.locator_reg["name_card_txt"]
        self.driver.find_element(*locator).send_keys(name_on_card)
        time.sleep(2)

    def TC_Bus_052(self):
        time.sleep(2)
        locator = self.locator_reg["save_and_pay_button"]
        self.driver.find_element(*locator).click()
        time.sleep(2)