from selenium import webdriver
from selenium.webdriver.common.by import By
import time
CYCLE_INDEX = 0
driver = webdriver.Chrome()

driver.get("https://hh.ru/search/vacancy?text=Python&salary=&ored_clusters=true&enable_snippets=true&area=1")
time.sleep(5)
# element = driver.find_elements(
#     By.XPATH, '//span[@data-page-analytics-event="vacancy_search_suitable_item"]')
get_vacancy_title = driver.find_elements(By.CLASS_NAME, 'serp-item__title')  # 

for i in get_vacancy_title:
    CYCLE_INDEX += 1
    print(CYCLE_INDEX, i.text)
driver.quit()

if __name__ == "__main__":
    pass
