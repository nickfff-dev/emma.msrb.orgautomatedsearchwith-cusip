import selenium
from selenium import webdriver
import requests
import time
import os
import sys
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)




dataz = {"CUSIP": [], "DATE":[]}

driver.get("https://emma.msrb.org/")
time.sleep(5)


def mwiko(val):
    driver.find_element_by_css_selector("#quickSearchText").send_keys(val)
    driver.find_element_by_css_selector("#quickSearchButton").click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try:
        driver.find_element_by_css_selector("#ctl00_mainContentArea_disclaimerContent_yesButton").click()
        time.sleep(5)
    except:
        print("next cusip search")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    trade = driver.find_element_by_css_selector("#lvRollup > tbody > tr:nth-child(1) > td:nth-child(2)").text
    dataz["CUSIP"].append(val)
    dataz["DATE"].append(trade)



vitus = open("cusip.txt").read().splitlines()

for vitu in vitus:
    mwiko(vitu)
        

df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in dataz.items()]))
df.to_csv("cusipdatesss2.csv")
print(df)