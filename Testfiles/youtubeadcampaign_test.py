from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
import time
import unittest
from Hypeddit.logintest import Logintest
from Hypeddit.youtubeadcampaign import Youtube_ad
import pytest


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        s = Service("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login = Logintest(self.driver)
        self.youtube = Youtube_ad(self.driver)

    def test_login(self):

        self.driver.get("https://dev2.hypeddit.com/devlock")
        self.login.devlock("BetterDevTest8675!")
        self.login.login("arnavangira@gmail.com", "123456")
        time.sleep(2)

    def test_youtube(self):
        #self.driver.get("https://dev2.hypeddit.com/ads/create/youtube-growth-video")
        self.youtube.new_youtubead("https://youtu.be/sQPpOiTAZ14?si=-TsFmzOYvbYWhlTx", "Deep",
                                   "Horror movie")
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()