import time
from selenium.webdriver.common.by import By
class Logintest():

    def __init__(self, driver):
        self.driver = driver

        self.devpassword_textbox_xpath = "//input[@name='password']"
        self.devsubmit_button_xpath = "//button[normalize-space()='SUBMIT']"
        self.Hlogin_button_xpath = "//a[normalize-space()='Login']"
        self.username_textbox_id = "login_email"
        self.password_textbox_id = "login_password"
        self.login_button_id = "login_button"
        self.cancel_popup_xpath = "//button[@class='js-cookie-consent-agree cookie-consent__agree']"


    def devlock(self, devpassword):
        self.driver.find_element(By.XPATH, self.devpassword_textbox_xpath).send_keys(devpassword)
        self.driver.find_element(By.XPATH, self.devsubmit_button_xpath).click()
        self.driver.find_element(By.XPATH, self.Hlogin_button_xpath).click()

    def login(self, username, password):
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)
        self.driver.find_element(By.ID, self.login_button_id).click()
        self.driver.find_element(By.XPATH, self.cancel_popup_xpath).click()
        time.sleep(3)




