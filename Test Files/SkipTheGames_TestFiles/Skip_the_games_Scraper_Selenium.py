import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging
from selenium.webdriver.common.by import By
import pandas as pd
import undetected_chromedriver as uc


LOG_FILE = 'listings_results.log'
logging.basicConfig(level=logging.INFO,
                    datefmt="%m/%d/%Y %H:%M:%S", filename=LOG_FILE)


class TestScraper:
    def __init__(self):
        self.driver = None
        self.location = 'fort-myers'
        self.keywords = ['cash', 'Exotic']
        self.join = ''
        self.payment = ['cash', 'cashapp', 'venmo']
        self.url = f'https://www.skipthegames.com/posts/{self.location}/'
        self.text_search = ''

        # TODO these must be pulled from about_info, description, or activities
        # self.phone_number = []
        # self.name = []
        # self.sex = []
        # self.email = []
        # self.payment_method = []
        # self.location = []

        # lists to store data and then send to csv file
        self.link = []
        self.about_info = []
        self.description = []
        self.services = []

    def initialize(self):
        options = uc.ChromeOptions()
        options.headless = False
        self.driver = uc.Chrome(use_subprocess=True, options=options)
        self.open_webpage()

        links = self.get_links()
        self.get_data(links)
        self.format_data_to_csv()
        self.close_webpage()

        # self.check_post_for_keywords(self.get_data())

    def open_webpage(self) -> None:
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        assert "Page not found" not in self.driver.page_source

    def close_webpage(self) -> None:
        self.driver.close()

    # TODO fix bug to get thr correct links
    def get_links(self):
        posts = self.driver.find_elements(
            By.CSS_SELECTOR, 'html.no-js body div table.two-col-wrap tbody tr '
                             'td#gallery_view.listings-with-sidebar.list-search-results.gallery div.full-width '
                             'div.small-16.columns div.clsfds-display-mode.gallery div.day-gallery [href]')
        links = [post.get_attribute('href') for post in posts]

        print([link for link in set(links)])
        print('# of links:', len(set(links)))
        return links

    def get_data(self, links):
        links = set(links)
        counter = 0

        for link in links:
            # append link to list
            self.link.append(link)
            print(link)

            # self.driver.implicitly_wait(2)
            # time.sleep(1)
            self.driver.get(link)
            assert "Page not found" not in self.driver.page_source

            try:
                about_info = self.driver.find_element(
                    By.XPATH, '/html/body/div[7]/div/div[2]/div/table/tbody')
                print(about_info.text)
                self.about_info.append(about_info.text)
            except NoSuchElementException:
                self.about_info.append('N/A')

            try:
                services = self.driver.find_element(
                    By.XPATH, '//*[@id="post-services"]')
                print(services.text)
                self.services.append(services.text)
            except NoSuchElementException:
                self.services.append('N/A')

            try:
                description = self.driver.find_element(
                    By.XPATH, '/html/body/div[7]/div/div[2]/div/div[1]/div')
                print(description.text)
                self.description.append(description.text)
            except NoSuchElementException:
                self.description.append('N/A')

            # for line in info:
            #     if 'call' in line.lower():
            #         print(line)
            #         print('keyword found')

            screenshot_name = str(counter) + ".png"
            self.capture_screenshot(screenshot_name)
            counter += 1

            # if counter > 5:
            #     break

    def format_data_to_csv(self):
        titled_columns = {
            'Link': self.link,
            'about-info': self.about_info,
            'services': self.services,
            'Description': self.description
        }

        data = pd.DataFrame(titled_columns)
        data.to_csv('skipthegames_01-20-23.csv', index=False, sep="\t")

    # TODO
    def check_post_for_keywords(self, data):
        for keyword in self.keywords:
            if keyword in data[0] or keyword in data[1]:
                logging.info(data)
            break

    def capture_screenshot(self, screenshot_name):
        self.driver.save_screenshot(f'screenshots/{screenshot_name}')

    def read_keywords(self) -> str:
        return ' '.join(self.keywords)


if __name__ == "__main__":
    scraper = TestScraper()
    scraper.initialize()
