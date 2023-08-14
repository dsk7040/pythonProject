from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import unittest
from Hypeddit.logintest import Logintest
from Hypeddit.fangate import Fangate


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get("https://dev2.hypeddit.com/devlock")

        self.login = Logintest(self.driver)
        self.login.devlock("BetterDevTest8675!")
        self.login.login("harry@baltech.in", "123456")
        time.sleep(2)

        # def Test_fangate(self):
        self.fangate = Fangate(self.driver)
        self.fangate.create_fangate("https://open.spotify.com/track/0FBQ4NrrHUbR9kus7rzrOj?si=174f5e1d4de345e9",
                                    "C:\\Users\\Baltech\\Downloads\\Salasar Balaji Tone.mp3", "Arjit singh")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()


print("Fangate Success")
