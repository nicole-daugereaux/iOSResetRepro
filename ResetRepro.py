####################################################################
# Skeleton for Appium tests on Sauce Labs Real Devices - Unified Platform
# This is currently in BETA and will only work for private devices
####################################################################

###################################################################
# Imports that are good to use
###################################################################
from appium import webdriver
import requests
from time import sleep
import os
import urllib3
import json
import random
import sys
from colorama import Fore, Back, Style


androidTest = False
iosTest = True
useApp = True
appLocation = 'storage:8edd0c51-afcb-42b0-a158-5fb0a0186559'

###################################################################
# Selenium with Python doesn't like using HTTPS correctly
# and displays a warning that it uses Unverified HTTPS request
# The following disables that warning to clear the clutter
# But I should find a way to do the proper requests
###################################################################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###################################################################
# Pull a random Pokemon name to use as the test name
###################################################################
# pokemon_names_url = urllib3.PoolManager().request('GET', 'https://raw.githubusercontent.com/sindresorhus/pokemon/master/data/en.json')
# pokemon_names = json.loads(pokemon_names_url.data.decode('utf-8'))
# random_pokemon = random.choice(pokemon_names)

###################################################################
# Choose if you want Android of iOS capabilities
# Uncomment one of those lines
###################################################################
# androidTest = True
# iosTest = True

###################################################################
# Select Data Center
# Set region to 'US' or 'EU'
# Test will default to 'US' if left blank or set to any other than 'US' or 'EU'
###################################################################
region = 'US'

###################################################################
# Common parameters (desired capabilities)
###################################################################
projectParameters = {

    }

androidParameters = {

}

iosParameters = { # Define iOS Parameters here
    'platformVersion' : '13',
    'platformName' : 'iOS',
    'name': 'ios reset test',
}

###################################################################
# Merge parameters into a single capability dictionary

###################################################################
sauceParameters = {}
if androidTest != True and iosTest != True:
    print('You need to specify a platform to test on!')
    sys.exit()
elif androidTest == True and iosTest == True:
    print('Don\'t be greedy! Only choose one platform!')
    sys.exit()
elif androidTest:
    sauceParameters.update(androidParameters)
    if useApp:
        sauceParameters['app'] = appLocation # Use app if it's specified
    else:
        sauceParameters['browserName'] = 'Chrome' # Otherwise use Chrome
        #Note! Replace 'Chrome' with 'Browser' for older versions of Android to use the stock browser
elif iosTest:
    sauceParameters.update(iosParameters)
    if useApp:
        sauceParameters['app'] = appLocation
    else:
        sauceParameters['browserName'] = 'safari'



# This concatenates the tags key above to add the build parameter
sauceParameters.update({'build': 'Investigation'})

###################################################################
# Connect to Sauce Labs
###################################################################
try:
    region
except NameError:
    region = 'US'

if region != 'EU':
    print(Fore.MAGENTA + 'You are using the US data center for an RDC test, so a bald eagle is obviously running your tests.' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)
elif region == 'EU':
    print (Fore.CYAN + 'You are using the EU data center for an RDC test, you beautiful tropical fish!' + Style.RESET_ALL)
    driver = webdriver.Remote(
        command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.eu-central-1.saucelabs.com:443/wd/hub',
        desired_capabilities=sauceParameters)

###################################################################
# Test logic goes here
###################################################################
sleep(5)
driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="test-Username"]').send_keys('standard_user');
driver.find_element_by_xpath('//XCUIElementTypeSecureTextField[@name="test-Password"]').send_keys('secret_sauce');
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="test-LOGIN"]').click();
driver.reset()
sleep(5)
driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="test-Username"]').send_keys('standard_user');
driver.find_element_by_xpath('//XCUIElementTypeSecureTextField[@name="test-Password"]').send_keys('secret_sauce');
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="test-LOGIN"]').click();
driver.reset()
sleep(5)
driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="test-Username"]').send_keys('standard_user');
driver.find_element_by_xpath('//XCUIElementTypeSecureTextField[@name="test-Password"]').send_keys('secret_sauce');
driver.find_element_by_xpath('//XCUIElementTypeButton[@name="test-LOGIN"]').click();
driver.reset()

driver.quit()
