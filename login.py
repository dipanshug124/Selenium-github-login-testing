from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from STQA.Pages.loginPage import LoginPage
from STQA.Pages.homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(obj):
        obj.driver = webdriver.Chrome(executable_path="C:/Users/Gaurav/PycharmProjects/pythonProject2/venv/drivers/chromedriver.exe")
        obj.driver.implicitly_wait(10)
        obj.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://github.com/login")

        login = LoginPage(driver)
        login.username("Gaurav-jaybhay")
        login.password("Gaurav3011@")
        login.login()

        homepage = HomePage(driver)
        homepage.welcome()
        homepage.logout()

        time.sleep(2)

    def test_02_login_invalid_username(self):
        driver = self.driver
        driver.get("https://github.com/login")

        login = LoginPage(driver)
        login.username("dipanshu124@gmail.com")
        login.password("Gaurav3011@")
        login.login()

        message = login.check_if_invalid()
        self.assertEqual(message, """

      Incorrect username or password.

  """)

        time.sleep(2)

    @classmethod
    def tearDownClass(obj):
        obj.driver.close()
        obj.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Gaurav/PycharmProjects/pythonProject2/venv/STQA/Reports'))
