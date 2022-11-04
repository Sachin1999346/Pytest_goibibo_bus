#path or url are store inthis file all
class Configuration:

    URL = "https://www.goibibo.com/"
    # CHROME_PATH = r"C:\Users\Shree\PycharmProjects\HTD_Project\drivers\chromedriver.exe"
    CHROME_PATH = r"../drivers/chromedriver.exe"

    # FIREFOX_PATH = r"C:\Users\Shree\PycharmProjects\HTD_Project\drivers\geckodriver.exe"
    FIREFOX_PATH = r'../drivers/geckodriver.exe'

    # MSEDGE_PATH = r"C:\Users\Shree\PycharmProjects\HTD_Project\drivers\msedgedriver.exe"
    MSEDGE_PATH = r"../drivers/msedgedriver.exe"

    LOCATORS_PATH = r"C:\Users\Shree\PycharmProjects\Sprint2_Goibibo_Bus\test_data\Goibibo_locator.xlsx"
    # LOCATORS_PATH = r'../test_data/Goibibo_locator.xlsx'

    TESTDATA_PATH = r"C:\Users\Shree\PycharmProjects\Sprint2_Goibibo_Bus\test_data\Goibibo_TestData.xlsx"
    # TESTDATA_PATH = r'../test_data/Goibibo_TestData.xlsx'

    # REPORTS_PATH = r"C:\Users\Shree\PycharmProjects\HTD_Project\Reports\\"
    REPORTS_PATH = r"../Reports/"

    # SCREENSHOTS_PATH = r"C:\Users\Shree\PycharmProjects\HTD_Project\Screenshots\\"
    SCREENSHOTS_PATH = r"../Screenshots/"
    # gives report and screenshot folder path \\

    BUS_LOCATOR_SHEET = "Bus_page_locator"
    BUS_TEST_DATASHEET = "bus_test_data"