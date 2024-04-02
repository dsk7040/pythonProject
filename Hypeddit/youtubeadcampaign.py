import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait

class Youtube_ad():

    def __init__(self, driver):
        self.driver = driver
        self.AdsGoogle_account_xpath = "//button[@title='[321-446-9372]']"
        self.Googleaccount_next_button_xpath = "next_box_button_google-account-connect"
        self.trackurl_xpath = "//input[@id='track_url']"
        self.artist_name_xpath = "//input[@id='artist_name']"
        self.title_xpath = "//input[@id='title']"
        self.Select_genre_xpath = "//button[@title='Select genre']"
        self.Select_Bass_xpath = "//li[@data-original-index='2']//span[contains(text(),'Bass')]"
        self.next_box_button_music_id = "next_box_button_music"
        self.next_button_countries_id = "next_box_button_countries"
        self.next_button_interests_id = "next_box_button_interests-google"
        self.scheduleed_xpath = "//label[contains(text(),'Scheduled')]"
        self.start_time_xpath = "//input[@name='run_start_date']"
        self.select_month_xpath = "//span[contains(text(),'October')]"
        self.select_november_xpath = "//div[@style='display: block; left: 106px; top: 662.531px; position: absolute;']//div[@data-value='10']"
        self.select_start_time_xpath = "//body[1]/div[27]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]"
        self.End_time_xpath = "//input[@name='run_end_date']"
        self.select_end_time_xpath = "//body[1]/div[27]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[3]"
        self.next_box_button_budget_id = "next_box_button_budget"


    def new_youtubead(self, Trackurl, Artist_name, Title):
        self.driver.get("https://dev2.hypeddit.com/ads/create/youtube-growth-video")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.Googleaccount_next_button_xpath).click()
        self.driver.find_element(By.XPATH, self.trackurl_xpath).send_keys(Trackurl)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.artist_name_xpath).send_keys(Artist_name)
        self.driver.find_element(By.XPATH, self.title_xpath).send_keys(Title)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Select_genre_xpath).click()
        self.driver.find_element(By.XPATH, self.Select_Bass_xpath).click()
        self.driver.find_element(By.ID, self.next_box_button_music_id).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.next_button_countries_id).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.ID, self.next_button_interests_id))).click()
        # self.driver.find_element(By.ID, self.next_button_interests_id).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.scheduleed_xpath))).click()
        #self.driver.find_element(By.XPATH, self.scheduleed_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.start_time_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_month_xpath).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.select_november_xpath))).click()
        #self.driver.find_element(By.XPATH, self.select_november_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_start_time_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.End_time_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_end_time_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.next_box_button_budget_id).click()
        time.sleep(2)




