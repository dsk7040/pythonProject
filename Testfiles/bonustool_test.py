from selenium import webdriver
import time
import unittest
from selenium.webdriver.firefox.service import Service as FirefoxService
from Hypeddit.logintest import Logintest
from Hypeddit.music_video import videocreate
class videomaker:
    def newgate(self):
        self.driver = webdriver
        s = FirefoxService("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)

        driver = self.driver
        driver.get("https://dev2.hypeddit.com/devlock")
        login = Logintest(driver)
        login.devlock("BetterDevTest8675!")
        login.login("sonideepak@baltech.in", "123456")
        time.sleep(2)

    def bonustools(self):
        bonus = videocreate(self.driver)
        bonus.musictovideo("C:\\Users\\Baltech\\Downloads\\Music\\arjit songs.mp3",
                           "C:\\Users\\Baltech\\Downloads\\Music\\2sec.mp3",
                           "C:\\Users\\Baltech\\Downloads\\Music\\2sec.mp3",
                           "C:\\Users\\Baltech\\Downloads\\hanuman.jpg",
                           "dsk7040@gmail.com")


object = videomaker()
object.newgate()
object.bonustools()





