import os
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Backend.ScraperPrototype import ScraperPrototype
from selenium.webdriver.chrome.options import Options as ChromeOptions
import undetected_chromedriver as uc


class MegapersonalsScraper(ScraperPrototype):

    def __init__(self):
        super().__init__()
        self.driver = None
        self.url = "https://megapersonals.eu"
        self.known_payment_methods = ['cashapp', 'venmo', 'zelle', 'crypto', 'western union', 'no deposit',
                                      'deposit', 'cc', 'credit card', 'card', 'applepay', 'donation', 'cash']

        # set date variables and path
        self.date_time = None
        self.main_page_path = None
        self.screenshot_directory = None

        # lists to store data and then send to csv file
        self.description = []
        self.name = []
        self.phoneNumber = []
        self.city = []
        self.location = []
        self.link = []
        self.post_identifier = []
        self.payment_methods_found = []

        # TODO other info needs to be pulled using regex?

    def initialize(self):
        # format date
        self.date_time = str(datetime.today())[0:19]
        self.date_time = self.date_time.replace(' ', '_').replace(':', '-')

        # create directories for screenshot and csv
        self.main_page_path = f'megapersonals_{self.date_time}'
        os.mkdir(self.main_page_path)
        self.screenshot_directory = f'{self.main_page_path}/screenshots'
        os.mkdir(self.screenshot_directory)

        options = uc.ChromeOptions()
        options.headless = False
        self.driver = uc.Chrome(use_subprocess=True, options=options)

        self.open_webpage()

        links = self.get_links()
        self.get_data(links)
        self.format_data_to_csv()
        self.close_webpage()

    def open_webpage(self):
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        assert "Page not found" not in self.driver.page_source
        # To get the first five - a simple loop. You could add that threading here
        self.driver.find_element(By.CLASS_NAME, 'btn').click()
        self.driver.find_element(By.XPATH, '//*[@id="choseCityContainer"]/div[3]/label').click()
        self.driver.find_element(By.XPATH, '//*[@id="choseCityContainer"]/div[3]/article/div[10]/label').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="choseCityContainer"]/div[3]/article/div[10]/article/p[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="megapCategoriesOrangeButton"]').click()

    def close_webpage(self):
        self.driver.close()

    def get_links(self):
        post_list = self.driver.find_elements(By.CLASS_NAME, 'listadd')

        # traverse through list of people to grab page links
        links = []
        for person in post_list:
            links.append(person.find_element(By.TAG_NAME, "a").get_attribute("href"))
        return links

    # TODO - change if location changes?
    def get_formatted_url(self):
        pass

    def get_data(self, links):
        links = set(links)

        description = ''
        counter = 0

        for link in links:
            # append link to list
            self.link.append(link)
            print(link)

            self.driver.get(link)
            assert "Page not found" not in self.driver.page_source

            try:
                description = self.driver.find_element(
                    By.XPATH, '/html/body/div/div[6]/span').text
                self.description.append(description)
                print(description)
            except NoSuchElementException:
                self.description.append('N/A')

            self.check_for_payment_methods(description)

            try:
                phone_number = self.driver.find_element(
                    By.XPATH, '/html/body/div/div[6]/div[1]/span').text
                self.phoneNumber.append(phone_number)
                print(phone_number)
            except NoSuchElementException:
                self.phoneNumber.append('N/A')

            try:
                name = self.driver.find_element(
                    By.XPATH, '/html/body/div/div[6]/p[1]/span[2]').text[5:]
                self.name.append(name)
                print(name)
            except NoSuchElementException:
                self.name.append('N/A')

            try:
                city = self.driver.find_element(
                    By.XPATH, '/html/body/div/div[6]/p[1]/span[1]').text[5:]
                self.city.append(city)
                print(city)
            except NoSuchElementException:
                self.city.append('N/A')

            try:
                location = self.driver.find_element(
                    By.XPATH, '/html/body/div/div[6]/p[2]').text[9:]
                self.location.append(location)
                print(location)
            except NoSuchElementException:
                self.location.append('N/A')

            self.post_identifier.append(counter)

            screenshot_name = str(counter) + ".png"
            self.capture_screenshot(screenshot_name)
            counter += 1

            if counter > 0:
                break

            print('\n')

    # TODO - move to class that handles data
    def format_data_to_csv(self):
        titled_columns = {
            'Post_identifier': self.post_identifier,
            'name': self.name,
            'phone-number': self.phoneNumber,
            'city': self.city,
            'location': self.location,
            'description': self.description,
            'payment_methods': self.payment_methods_found
        }

        data = pd.DataFrame(titled_columns)
        data.to_csv(f'{self.main_page_path}/megapersonals-{self.date_time}.csv', index=False, sep="\t")

    def check_for_payment_methods(self, description):
        payments = ''
        for payment in self.known_payment_methods:
            if payment in description.lower():
                print('payment method: ', payment)
                payments += payment + ' '

        if payments != '':
            self.payment_methods_found.append(payments)
        else:
            self.payment_methods_found.append('N/A')
            print('N/A')

    def capture_screenshot(self, screenshot_name):
        self.driver.save_screenshot(f'{self.screenshot_directory}/{screenshot_name}')

    # TODO - read keywords from keywords.txt
    def read_keywords(self):
        pass