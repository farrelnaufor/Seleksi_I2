from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def take_screenshot(name):
    driver.save_screenshot(f"{name}.png")

driver.get("https://indonesiaindicator.com/")
time.sleep(2)

wait = WebDriverWait(driver, 20)

#  Search  #
careers = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Careers']"))
)
assert careers.is_displayed(), "Menu Careers tidak ditemukan"
careers.click()

search = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search Job...']"))
)
assert search.is_enabled(), "Kolom search tidak dapat digunakan"

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search)
time.sleep(1)

search.send_keys("Full Stack Developer")
time.sleep(2)
search.send_keys(Keys.ENTER)
take_screenshot("search")

time.sleep(2)
search.send_keys(Keys.CONTROL, "a")
search.send_keys(Keys.DELETE)

#  Invalid Search  #
search.send_keys("asdfvfghjkladw")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)

no_result = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'No jobs found matching your search criteria.')]"))
)
assert no_result.is_displayed(), "No Result"

take_screenshot("search_invalid")

search.send_keys(Keys.CONTROL, "a")
search.send_keys(Keys.DELETE)

#  Fi;ter  #
dropdown = driver.find_element(By.CSS_SELECTOR, "select.dropdown-style")
assert dropdown.is_displayed(), "Dropdown filter tidak muncul"
dropdown.click()

driver.find_element(By.XPATH, "//option[normalize-space()='Data Analyst']").click()
time.sleep(2)

selected_option = dropdown.get_attribute("value")
assert selected_option is not None, "Filter tidak memilih opsi apapun"

take_screenshot("filter")

#  Online News  #
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

news_menu = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='News']"))
)
assert news_menu.is_displayed(), "Menu News tidak ditemukan"
news_menu.click()
time.sleep(2)

first_news = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='row g-8']//a[1]"))
)
assert first_news.is_displayed(), "Berita pertama tidak tampil"

driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", first_news)
time.sleep(1)

driver.execute_script("arguments[0].click();", first_news)
assert "news" in driver.current_url.lower(), "Halaman berita tidak terbuka"

take_screenshot("news")

driver.back()
time.sleep(2)

# Menu & Submenu #
driver.back()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

socmed = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='py-5 px-10']//a[1]"))
)
assert socmed.is_displayed(), "Tautan sosial media tidak ditemukan"
socmed.click()
time.sleep(3)

take_screenshot("sosmed")