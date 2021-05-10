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

def get_posts_from_profiles(driver):
    

    profile = 'covidaidresources'
# profile = 'covidhelpindia'
# profile = 'dhoondh'
    driver.get(url +profile + '/')

    get_posts_from_stories(driver, profile)
    get_posts_from_posts(driver, profile)