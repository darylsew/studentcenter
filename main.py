from selenium import webdriver
from selenium.webdriver.common.keys import Keys

f = [i.strip() for i in open('creds').readlines()]
username = f[0]
password = f[1]
lect = 11885
disc1 = 11886
disc2 = 11889
successes = 0
failures = 0
while True:
    try:
        driver = webdriver.Firefox()
        driver.get("http://www.studentcenter.cornell.edu")
        netidinput = driver.find_element_by_id("netid")
        passwdinput = driver.find_element_by_id("password")
        netidinput.send_keys(username)
        passwdinput.send_keys(password)
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_id("DERIVED_SSS_SCL_LINK_ADD_ENRL").click()
        semesters = driver.find_elements_by_name("SSR_DUMMY_RECV1$sels$0")
        semesters[1].click()
        driver.find_element_by_name("DERIVED_SSS_SCT_SSR_PB_GO").click()
        
        # Code for searching (no need to repeat; student center caches classes in cart)
        #driver.find_element_by_name("DERIVED_REGFRM1_CLASS_NBR$42$").send_keys(int(lect))
        #driver.find_element_by_id("DERIVED_REGFRM2_SSR_PB_ADDTOLIST2$44$").click()
        #discussions = driver.find_elements_by_name("SSR_CLS_TBL_RE$sels$0")
        #discussions[0].click()
        #driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB").click()
        #driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB").click()
        driver.find_element_by_id("DERIVED_REGFRM1_LINK_ADD_ENRL").click()
        driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SUBMIT").click()
        driver.close()
        successes += 1
        print "successes: ", successes
    except:
        # Non-deterministic html data...
        failures += 1
        print "failed run", failures
        driver.close()


