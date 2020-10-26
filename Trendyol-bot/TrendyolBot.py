#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import random
import string
from random import randint
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

delay = 10
# browser ı parametre olarak alıyoruz


def choose_driver():
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        "chromedriver", options=opts)
    return driver


def login(driver):

    username = "dogushankaya.itu@gmail.com"
    password = "trendyolcase"

    driver.get("https://www.trendyol.com/")
    time.sleep(7)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(3)
    WebDriverWait(driver, delay).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "login-register-button-container"))).click()
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "email"))).send_keys(username)
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.ID, "password"))).send_keys(password)
    driver.find_element_by_id('loginSubmit').click()


def signIn(driver, username, password):
    driver.get("https://www.trendyol.com/")
    time.sleep(7)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(3)

    driver.find_element_by_xpath("//li[@id='accountBtn']/div").click()
    time.sleep(2)

    driver.find_element_by_link_text(u"Hemen Üye Ol").click()
    driver.find_element_by_id("email").click()
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath(
        "//form[@id='registerForm']/section[3]/div/label").click()
    driver.find_element_by_xpath(
        "//form[@id='registerForm']/section[4]/div/label").click()
    driver.find_element_by_id("registerSubmit").click()
    # driver.find_element_by_link_text(u"Çıkış Yap").click()




def random_char():
    s = random.choice(string.ascii_lowercase)
    s += random.choice(string.ascii_lowercase)
    s += random.choice(string.ascii_lowercase)
    s += random.choice(string.ascii_uppercase)
    s += random.choice(string.digits)
    s += random.choice(string.ascii_uppercase)
    s += random.choice(string.ascii_lowercase)
    return s

browser = choose_driver()
username = random_char()+"@gmail.com"
password = random_char()
signIn(browser, username, password)