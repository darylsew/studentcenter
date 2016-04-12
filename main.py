from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

f = [i.strip() for i in open('creds').readlines()]
username = f[0]
password = f[1]
successes = 0
failures = 0

NETWORK_SLOWNESS = 3
while True:
    try:
        driver = webdriver.PhantomJS()
        driver.get("http://www.studentcenter.cornell.edu")
        netidinput = driver.find_element_by_id("netid")
        passwdinput = driver.find_element_by_id("password")
        netidinput.send_keys(username)
        passwdinput.send_keys(password)
        driver.find_element_by_name("Submit").click()
        time.sleep(NETWORK_SLOWNESS)
        driver.find_element_by_id("DERIVED_SSS_SCR_SSS_LINK_ANCHOR3").click()
        time.sleep(NETWORK_SLOWNESS)
        driver.find_element_by_id("SSR_DUMMY_RECV1$sels$2$$0").click()
        time.sleep(NETWORK_SLOWNESS)
        driver.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").click()
        time.sleep(NETWORK_SLOWNESS)
        driver.find_element_by_id("DERIVED_REGFRM1_LINK_ADD_ENRL$82$").click()
        time.sleep(NETWORK_SLOWNESS)
        driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SUBMIT").click()
        successes += 1
        print("successes: " + str(successes))
        # Try every 100 seconds
        time.sleep(100)
        driver.close()
        os.system("pkill -9 phantomjs")
    except:
        # Deal w non-deterministic html data...
        # or network issues or whatever
        failures += 1
        print("failures: " + str(failures))
        driver.close()
