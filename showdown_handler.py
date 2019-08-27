from selenium import webdriver
import time
# from selenium.webdriver.common.keys import keys

#replace this for usage
username = "jonny_appleseed"
password = "Password1"

driver = webdriver.Firefox()
driver.get("https://play.pokemonshowdown.com")
time.sleep(1)
driver.find_element_by_css_selector("button[name='login']").click()
time.sleep(1)

elem = driver.find_element_by_css_selector("input[name='username']")
elem.clear()
elem.send_keys(username)
time.sleep(1)

driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(1)

elem = driver.find_element_by_css_selector("input[name='password']")
elem.clear()
elem.send_keys(password)
time.sleep(1)

driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(1)

driver.find_element_by_css_selector("button[name='search']").click()
def select_input(command):
    if command[0] == "use":
        elem = driver.find_element_by_css_selector("button[data-move='"+command[1][1:].title() +"']")
        elem.click()
        return True
    elif command[0] == "go":
        elem = driver.find_element_by_xpath("//button[contains(text(),'" + command[1][1:].title() + "')]")
        elem.click()
        return True
    # elif command[0] == "data":
    #
    # elif command[0] == "weak":
