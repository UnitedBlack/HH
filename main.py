from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

CYCLE_INDEX = 0
driver = webdriver.Chrome()
actions = ActionChains(driver)
search_name = 'python'


print("Loading page...")
driver.get(f"https://hh.ru/search/vacancy?text={search_name}&salary=&ored_clusters=true&area=1")

try:
    next_page = driver.find_element(By.XPATH, "//a[@data-qa='pager-next']")
    next_page_button = next_page.get_attribute("href")
except (NoSuchElementException):
    next_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//a[@data-qa='pager-next']"))).get_attribute("href")


def page_parser():
    global CYCLE_INDEX
    for cycle in next_page_button:
        vacancy_find_xpath = driver.find_elements(By.XPATH, "//a[@class='serp-item__title']")
        for vacancy_find in vacancy_find_xpath:
            CYCLE_INDEX += 1
            try:
                vacancy_link = vacancy_find.get_attribute("href")
                try:
                    vacancy_title = vacancy_find.text
                except (NoSuchElementException):
                    vacancy_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                        By.XPATH, "//a[@class='serp-item__title']"))).text
            except (NoSuchElementException):
                vacancy_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                    By.XPATH, "//a[@class='serp-item__title']"))).get_attribute("href")
            print(f"{CYCLE_INDEX}. Вакансия: {vacancy_title}, ссылка: {vacancy_link}")
        actions.move_to_element(next_page).click(next_page).perform()
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    return


page_parser()

driver.quit()

if __name__ == "__main__":
    pass