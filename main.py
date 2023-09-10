from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

CYCLE_INDEX = 0

chrome_options = Options()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)
actions = ActionChains(driver)

print("Loading page...")
driver.get("https://hh.ru/search/vacancy?text=Python&salary=&ored_clusters=true&enable_snippets=true&area=1")

next_page = driver.find_element(By.XPATH, "//a[@data-qa='pager-next']")
hrefs = next_page.get_attribute("href")
actions.move_to_element(next_page).perform()


vacancy_link = driver.find_elements(
    By.XPATH, "//a[@class='serp-item__title']")
# get_vacancy_title = driver.find_elements(By.CLASS_NAME, 'serp-item__title')

for i in vacancy_link:
    CYCLE_INDEX += 1
    href = i.get_attribute("href")
    print(f"{CYCLE_INDEX}. Вакансия: {i.text}, ссылка: {href}")

driver.quit()

if __name__ == "__main__":
    pass
