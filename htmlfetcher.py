import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class HTMLFetcher:
    def __init__(self) -> None:
        firefox_options = Options()
        firefox_options.add_argument('-headless')

        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('permissions.default.stylesheet', 2)
        firefox_profile.set_preference('permissions.default.image', 2)
        firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

        self.driver = webdriver.Firefox(executable_path=os.path.join(os.path.dirname(__file__), 'geckodriver'),
                                        firefox_options=firefox_options,
                                        log_path='/tmp/geckodriver.log',
                                        firefox_profile=firefox_profile)
        self.driver.set_page_load_timeout(10)

    def get(self, url: str, wait: int = 0) -> str:
        self.driver.delete_all_cookies()
        self.driver.get(url)
        time.sleep(wait)
        return self.driver.page_source

    def close(self) -> None:
        self.driver.close()
