import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

time = datetime.now().strftime("%H-%M")
CYCLE_INDEX = 0
driver = webdriver.Chrome()
actions = ActionChains(driver)

print("Loading page...")
driver.get(f"https://hh.ru/search/vacancy?area=1&employment=full&employment=part&employment=probation&excluded_text=маркетплейсы+вайлдберис+озон+недвижимость+стройка&experience=noExperience&industry=7.541&industry=7.539&industry=11.459&industry=44.393&professional_role=170&professional_role=2&professional_role=3&professional_role=37&professional_role=163&professional_role=68&schedule=fullDay&schedule=shift&schedule=flexible&search_field=name&search_field=company_name&search_field=description&clusters=true&enable_snippets=true&no_magic=true&ored_clusters=true&order_by=salary_asc&page=0")

try:
    next_page = driver.find_element(By.XPATH, "//a[@data-qa='pager-next']")
    next_page_button = next_page.get_attribute("href")
except (NoSuchElementException):
    next_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//a[@data-qa='pager-next']"))).get_attribute("href")


def page_parser():
    global CYCLE_INDEX
    for cycle in next_page_button:
        vacancy_find_xpath = driver.find_elements(
            By.XPATH, "//a[@class='serp-item__title']")
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
            try:
                vacancy_link_clean = re.sub('vologda\.', '', vacancy_link)
            except:
                vacancy_link_clean = vacancy_link
            output = (f"{vacancy_title}, {vacancy_link_clean}")
            with open(f'Parsed-{time}.txt', 'a', encoding='utf-8') as file: file.write(output + "\n")
        actions.move_to_element(next_page).click(next_page).perform()
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    return


driver.quit()

if __name__ == "__main__":
    page_parser()
