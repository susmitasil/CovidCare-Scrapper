from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pychrome
import os
import wget
import time
from send_images.api import *
import requests

def get_posts_from_posts(driver, profile):

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    anchors = driver.find_elements_by_xpath("//a[contains(@href,'/p/')]")
    # print(anchors)
    anchors = [a.get_attribute('href') for a in anchors]
    print(anchors)
# print(types)
# types = driver.find_elements_by_xpath("//a[@type]")
# print(types)

    path = os.path.dirname(__file__)
    path = os.path.join(path, "../../data_collected/posts/"+ profile)
    if not os.path.exists(path):
        os.makedirs(path)
    # os.mkdir(path)

    

    def get_single_image(counter, shortcode):
        images = driver.find_elements_by_tag_name('img')

        images = [image.get_attribute('src') for image in images]
    # print(images)
        save_as = os.path.join(path, str(shortcode)+"_"+ str(counter) + '.jpg')
        wget.download(images[1], save_as)
        upload_single_file(save_as)


    for post in anchors:
        counter = 0
        try:
            driver.get(post)
            time.sleep(0.5)
            shortcode = driver.current_url.split("/")[-2]
            get_single_image(counter, shortcode)
            counter += 1
            next_up = driver.find_elements_by_xpath(
            "//button[contains(@class, '_6CZji')][@tabindex='-1']/div[contains(@class,'coreSpriteRightChevron')]")
            print('----------------------------------------------------------------------')
            print(next_up)
            while(next_up):
            # if(len(next_up) == 1):
                next_up[0].click()
                time.sleep(0.5)
                get_single_image(counter,shortcode)
                counter += 1
            # elif(len(next_up) > 1):
            #     next_up[1].click()
            #     time.sleep(0.5)
            #     get_single_image(counter)
            #     counter += 1

                next_up = driver.find_elements_by_xpath(
                "//button[contains(@class, '_6CZji')][@tabindex='-1']/div[contains(@class,'coreSpriteRightChevron')]")
            
        except Exception:
            continue
    