# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:26:17 2019

@author: Zekihan
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import os
import json

closed = True

class InstagramBot():
    
    def __init__(self, email, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('C:\\Coding\\Programs\\chromedriver.exe', options=self.browserProfile)
        self.email = email
        self.password = password
        global closed
        closed = False

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            notnow = self.browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
            notnow.click()
            time.sleep(1)
        except:
            e = sys.exc_info()[1]
            print("Failed due to \"%s\"." %e)


    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2)
        else:
            print("You are already following this user")
    
    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")
    

    def getUserFollowersAll(self, username):
        self.browser.get('https://www.instagram.com/' + username)
        time.sleep(1)
        max = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_property("title")
        max = int(max)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        followersList.click()
        time.sleep(0.5)
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
            time.sleep(0.5)
            followersList.click()

        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers
    
    def getUserFollowedAll(self, username):
        self.browser.get('https://www.instagram.com/' + username)
        time.sleep(1)
        max = self.browser.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span')
        max = int(max.get_property("outerText"))
        followersLink = self.browser.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a')
        followersLink.click()
        time.sleep(2)
        followedList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followedList.find_elements_by_css_selector('li'))
    
        followedList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followedList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
            followedList.click()
            time.sleep(0.5)

        
        followed = []
        for user in followedList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followed.append(userLink)
            if (len(followed) == max):
                break
        return followed
    
    def closeBrowser(self):
        self.closed = True
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closed = True
        self.closeBrowser()
   
def inf_try(method,param1):
    complete = False
    while (not complete):
        try:
            result = method(param1)
            complete = True
            return result
        except:
            complete = False
            e = sys.exc_info()[1]
            print(e)

def save_results(mDict):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = (my_path + "\\data\\results.json")
    if not os.path.exists(my_path + "\\data"):
        os.mkdir(my_path + "\\data")
    if os.path.exists(path):  
        f = open(path,"r+")
        old = json.loads(f.read())
        f.close()
        mDict.update(old)
    save = json.dumps(mDict, indent=4)
    f= open(path,"w+")
    f.write(save)
    f.close()

def make_dict(username, followed, followers):
    dict4J = {}
    utftime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    temp1 = {}
    temp1["followed"] = followed
    temp1["followers"] = followers
    temp2 = {}
    temp2[username] = temp1
    dict4J[utftime] = temp2
    
def followerInsight(bot,username):
    followed = bot.getUserFollowedAll( username)
    followers = inf_try(bot.getUserFollowersAll, username)
    dict4J = make_dict(username, followed, followers)
    save_results(dict4J)
    
    print ("\n\n\n\n--------------------------------")
    for i in followed:
        if not i in followers :
            print(i)




username = input("topsitognu")
password = input("asd123")
bot = InstagramBot(username,password)
bot.signIn()
followerInsight(bot, "zekihanazman")
bot.closeBrowser()






