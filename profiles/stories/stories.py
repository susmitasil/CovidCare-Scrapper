from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pychrome
import os
import wget
import time


def output_on_start(**kwargs):
    print("STARTED ", kwargs)


def output_on_end(**kwargs):
    print("FINISHED ", kwargs)


def get_posts_from_stories(driver,profile):
    

    # profile = 'covidaidresources'
# profile = 'covidhelpindia'
# profile = 'dhoondh'
    # driver.get("https://www.instagram.com/"+profile + '/')

    path = os.path.dirname(__file__)
    path = os.path.join(path, "../../data_collected/stories/"+ profile)
    if not os.path.exists(path):
        os.makedirs(path)
    # os.mkdir(path)

    
    def get_story_image(counter):
        images = driver.find_elements_by_tag_name('img')
        shortcode = driver.current_url.split("/")[-2]
        images = [image.get_attribute('src') for image in images]
        save_as = os.path.join(path, str(shortcode)+ "_" + str(counter) + '.jpg')
        wget.download(images[0], save_as)
    # counter +=1


# profile_pic = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='%s's profile picture']" %profile))).click()
    profile_pic = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button']"))).click()
    time.sleep(5)

    counter = 0
    
    get_story_image(counter)
    counter += 1

    next_up = driver.find_elements_by_xpath("//button[@class='FhutL']")
    print(next_up)
    while(next_up):
        if(len(next_up) == 1):
            next_up[0].click()
            get_story_image(counter)
            counter += 1
        # elif(len(next_up) > 1):
        #     next_up[1].click()
        #     get_story_image(counter)
        #     counter += 1

        next_up = driver.find_elements_by_xpath("//button[@class='FhutL']")