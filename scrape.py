from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/ben/Desktop/DASH/ThisisMyCountry/imagescrape/chromedriver')
driver.get("https://thisismycountry.elevator.umn.edu/asset/getEmbed/5b59f50e3f3cb17b1b230b79/null/true")
# assert "umn" in driver.title
# select = driver.find_element_by_class_name('form-group').get_attribute('href')

# get text which is associated with href then use click() function
# this handles the login to access images
link = driver.find_element_by_link_text("University Sign In")
link.click()

# now we are logging into U of M
driver.find_element(By.XPATH, "//input[@id='username']").send_keys('<username>')
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('<password>', Keys.RETURN)
driver.implicitly_wait(1)
driver.find_element_by_class_name("auth-button").send_keys(Keys.RETURN)

elem = driver.find_element_by_name("imageContent").get_attribute('src')
print(elem)
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()