from selenium import webdriver      
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


### This scripts loads 200 pages using selenium and passes to beautiful soup the resulting html

## Variables definition
targetPages =200
delay = 10
page = 1

MY_URL = 'https://www.money.co.uk/mortgages/first-time-buyer-mortgages.htm'

## Assigning key XPATHs
COOKIE_ACCEPT_BUTTON_XPATH = '//*[@id="pageWrapper"]/div[3]/div/div/span'
LOAD_MORE_BUTTON_START_XPATH = '//*[@id="ct_113_foot_btn_more_input"]' 
LOAD_MORE_BUTTON_ONGOING_XPATH ='//*[@id="ct_113_foot_btn_more"]'


## Loading drivers
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get(MY_URL)

## Kicking off
title = driver.title
print("Loading started", title)

## Accepting cookies:
print("Accepting cookies")
cookieAcceptanceButton = driver.find_element_by_xpath(COOKIE_ACCEPT_BUTTON_XPATH)
cookieAcceptanceButton.click()

## Loading second page: 
time.sleep(2)
page = page + 1
print("Loading page", page)
loadMoreButton = driver.find_element_by_xpath(LOAD_MORE_BUTTON_START_XPATH)
loadMoreButton.click()


## defining searching function



click_more=True
while click_more:
        try: 
                loadMoreButton = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, LOAD_MORE_BUTTON_ONGOING_XPATH)),"Cannot find 'Load More' button")
                loadMoreButton.click()
                page = page + 1
                print ("Loading page", page)

        except TimeoutException:
                click_more = False


# while True:
#         try:
#                 print("Loading page", page)
#                 time.sleep(5)
#                 wait = WebDriverWait(driver, 10)
#                 element = wait.until()
#                 loadMoreButton = driver.find_element_by_xpath(LOAD_MORE_BUTTON_ONGOING_XPATH).click()
#                 page = page + 1
#         except 
#                 pass

print("Loading completed, total of:", page, "pages were loaded")

#driver.close()


#fails because of this <div class="overlayBg overlayLoading" style="display: block; opacity: 0.149903;"></div>

# ## Loading pages
# while page < targetPages:
#     try:
#         print("Loading page", page)

#         #waiting until 10s
#         WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,LOAD_MORE_BUTTON_ONGOING_XPATH))

#         #click the button
#         loadMoreButton = driver.find_element_by_xpath(LOAD_MORE_BUTTON_ONGOING_XPATH)
#         loadMoreButton.click()

#         #increase the page number
#         page = page + 1
