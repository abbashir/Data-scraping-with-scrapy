from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
# for Headless
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_path = which("chromedriver")

# driver = webdriver.Chrome(executable_path=chrome_path)
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get("https://duckduckgo.com")
search_input = driver.find_element_by_id("search_form_input_homepage")
search_input.send_keys("My User Agent")

# search_btn = driver.find_element_by_id("search_button_homepage")
# search_btn.click()

search_input.send_keys(Keys.ENTER)
print(driver.page_source)
print("End")

# driver.close()
