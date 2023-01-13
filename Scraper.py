from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/rizho/OneDrive/Desktop/STEP TO FUTURE/PYTHON SPECIAL/SCRAPING PART1/chromedriver.exe")
browser.get(START_URL)
time.sleep(100)

headers = ["name","distance","mass","radius"]
Star_Data = []

def scrap():

    for i in range(0,1):
         soup = BeautifulSoup(browser.page_source,"html.parser")



scrap()