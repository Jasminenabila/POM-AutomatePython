from selenium import webdriver
import time
import unittest
from pomModel import loginPage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/home/jasmine/Documents/chromedriver")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://equity-sms-staging.bamms.co")

        login = LoginPage(driver)
        login.enter_username("tr1@gmail.com")
        login.enter_password("password")
        login.click_login()
        time.sleep(3)
    
    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()
        