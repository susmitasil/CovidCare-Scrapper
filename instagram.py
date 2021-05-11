from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time
from hashtags.hashtags import *
from profiles.profiles import *
from setup.setup import *

options = webdriver.ChromeOptions()
options.add_argument("--remote-debugging-port=8000")
driver = webdriver.Chrome(r'D:/python\Web_Scrapping/chromedriver.exe', chrome_options=options)

driver.get(url)
driver.maximize_window()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys('covid.locator')
password.send_keys('susmita1')

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

get_posts_by_hashtags(driver)
get_posts_from_profiles(driver)


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # driver.execute_script("window.scrollTo(0,4000);")
# images = driver.find_elements_by_tag_name('img')
# images = [image.get_attribute('src') for image in images]
# # print(types)
# # types = driver.find_elements_by_xpath("//a[@type]")
# # print(types)

# # counter =0 
# # for post in anchors:
# #     driver.get(post)
# #     type_as = driver.find_element_by_xpath("//meta[@property='og:type']").get_attribute("content")
# #     if type == 'image':
# #         download_url = driver.find_element_by_xpath("//meta[@property='og:image']").get_attribute('content')
# #         save_as = os.path.join(path, keyword[1:] + str(counter)+ '.jpg')
# #         wget.download(image, save_as)
# #         counter +=1
#         # urllib.request.urlretrieve(download_url, '{}.jpg'.format(shortcode))
        
#     # else:
#         # download_url = driver.find_element_by_xpath("//meta[@property='og:video']").get_attribute('content')
#         # urllib.request.urlretrieve( download_url , '{}.mp4'.format( shortcode ))
#         # pass

# counter =0 
# for image in images:
#     save_as = os.path.join(path, keyword[1:] + str(counter)+ '.jpg')
#     wget.download(image, save_as)
#     counter +=1
# print(path)
