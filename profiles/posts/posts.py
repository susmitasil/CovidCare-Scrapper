from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pychrome
import os
import wget
import time

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
    os.mkdir(path)

    counter = 0

    def get_single_image(counter):
        images = driver.find_elements_by_tag_name('img')

        images = [image.get_attribute('src') for image in images]
    # print(images)
        save_as = os.path.join(path, profile + str(counter) + '.jpg')
        wget.download(images[1], save_as)


    for post in anchors:
        driver.get(post)
        time.sleep(0.5)
        get_single_image(counter)
        counter += 1
        next_up = driver.find_elements_by_xpath(
            "//button[contains(@class, '_6CZji')][@tabindex='-1']/div[contains(@class,'coreSpriteRightChevron')]")
        print('----------------------------------------------------------------------')
        print(next_up)
        while(next_up):
            if(len(next_up) == 1):
                next_up[0].click()
                time.sleep(0.5)
                get_single_image(counter)
                counter += 1
            elif(len(next_up) > 1):
                next_up[1].click()
                time.sleep(0.5)
                get_single_image(counter)
                counter += 1

            next_up = driver.find_elements_by_xpath(
                "//button[contains(@class, '_6CZji')][@tabindex='-1']/div[contains(@class,'coreSpriteRightChevron')]")
    