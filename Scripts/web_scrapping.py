from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox, Chrome, FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common import *
from selenium.common.exceptions import InvalidSessionIdException
from urllib.parse import quote
from io import StringIO
from bs4 import BeautifulSoup
# from selenium.webdriver.firefox import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager as FirefoxDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import os
import platform
import pandas as pd
import numpy as np

import webbrowser as web
import time
from urllib.parse import quote


#---------------------------------------------------------------------------------------------------------
class Scrapper():
    def __init__(self,headless:bool,debug:bool,verbose:bool,timeout:int) -> None:
        #Create a headless Browser
        self.opts=ChromeOptions()
        if headless!=True:
            self.opts.add_argument('--headless=new')
        self.opts.add_argument("--incognito")
        self.opts.add_experimental_option('excludeSwitches',['enable-logging'])
        self.opts.add_argument("--start-maximized")
        self.browser=Chrome(options=self.opts,service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.celdas=np.chararray((21,13),255,unicode=True)
        self.cpc_list=[]
        self.page=list()
        self.timeout=timeout
        self.debug=debug
        self.verbose=verbose
        
        # self.prefs = {"download.default_directory":f"{PDF_PATH.replace('/',chr(92))}",
        #               "download.prompt_for_download":False,
        #               "download.directory_upgrade": True,
        #               "safebrowsing.enabled": True
        #               }
        # print(self.prefs)
        # self.opts.add_experimental_option('prefs',self.prefs)
        # self.capabilities['chromeOptions']['prefs']['download.prompt_for_download'] = False
    def get_scrap(self,URL):
        self.browser.get(URL)
        
        soup=BeautifulSoup(
            self.browser.find_element(By.XPATH,f'/html/body').get_attribute('innerHTML'),
            features="html.parser",
            )
        return str(soup)



scrappy_doo = Scrapper(headless=False,debug=True,verbose=True,timeout=15)


with open('scrap.html','x') as f:
    f.write(scrappy_doo.get_scrap('https://constructo.site/'))