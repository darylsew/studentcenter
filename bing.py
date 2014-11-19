from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

f = [i.strip() for i in open('creds').readlines()]
username = f[0]
password = f[1]
successes = 0
failures = 0
classes = [25225, 25383, 22868, 27916]

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

        # Actually inputting classes
        for i, cl in enumerate(classes):
            field = driver.find_element_by_id("crn_id" + str(i+1))
            field.send_keys(cl)

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
    time.sleep(300)
