from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

f = [i.strip() for i in open('creds').readlines()]
username = f[0]
password = f[1]
successes = 0
failures = 0
class1 = 25225
class2 = 25383

def find_by_tag_val(tag, val):
    ls = driver.find_elements_by_tag_name(tag)
    return [e for e in ls if e.get_attribute("value") == val][0]

while True:
    try:
        driver = webdriver.Firefox()
        driver.get("https://ssb.cc.binghamton.edu/banner/twbkwbis.P_WWWLogin")
        (user, pw, login) = driver.find_elements_by_tag_name("input")
        user.send_keys(username)
        pw.send_keys(password)
        login.click()
        driver.get("https://ssb.cc.binghamton.edu/banner/bwskfreg.P_AltPin")
        submit = find_by_tag_val("input", "Submit")
        submit.click()
        first = driver.find_element_by_id("crn_id1")
        first.send_keys(class1)
        second = driver.find_element_by_id("crn_id2")
        second.send_keys(class2)
        submit = find_by_tag_val("input", "Submit Changes")
        submit.click()
        driver.close()
        successes += 1
        print("successes: " + str(successes))
    except:
        # In the event of non-deterministic html data...
        failures += 1
        print("failures: " + str(failures))
        driver.close()
    time.sleep(10)
