from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pychrome
import os
import wget
import time
from profiles.stories.stories import *
from profiles.posts.posts import *
from setup.setup import *
from shared.readCsv.readCsv import *

def get_posts_from_profiles(driver):
    
    profiles = read_info_from_csv('profiles')

    # profile = 'covidaidresources'
    # driver.get(url +profile + '/')

    # get_posts_from_stories(driver, profile)
    # get_posts_from_posts(driver, profile)

    rec_get_posts(driver,profiles)

def rec_get_posts(driver, profiles):

    if(len(profiles)==0):
        return
    else:
        driver.get(url +profiles[0] + '/')

        get_posts_from_stories(driver, profiles[0])
        get_posts_from_posts(driver, profiles[0])
        profiles.pop(0)

    rec_get_posts(driver, profiles)