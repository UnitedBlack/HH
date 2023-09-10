from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


CYCLE_INDEX = 0

# chrome_options = Options()
# chrome_options.add_argument("--headless")


driver = webdriver.Chrome()
actions = ActionChains(driver)

print("Loading page...")
driver.get("https://hh.ru/search/vacancy?area=1&employment=full&employment=part&employment=probation&excluded_text=маркетплейсы+вайлдберис+озон+недвижимость+стройка&experience=noExperience&industry=7.541&industry=7.539&industry=11.459&industry=44.393&professional_role=170&professional_role=2&professional_role=3&professional_role=37&professional_role=163&professional_role=68&schedule=fullDay&schedule=shift&schedule=flexible&search_field=name&search_field=company_name&search_field=description&clusters=true&enable_snippets=true&no_magic=true&ored_clusters=true&order_by=salary_asc&page=0")

next_page = driver.find_element(By.XPATH, "//a[@data-qa='pager-next']")
href_button_next = next_page.get_attribute("href")
# actions.move_to_element(next_page).perform()


vacancy_link = driver.find_elements(
    By.XPATH, "//a[@class='serp-item__title']")
# get_vacancy_title = driver.find_elements(By.CLASS_NAME, 'serp-item__title')

# for a in href_button_next:
#     for i in vacancy_link:
#         CYCLE_INDEX += 1
#         try:
#             href = i.get_attribute("href")
#             try:
#                 text = i.text
#             except NoSuchElementException:
#                 text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']")))
#             except NoSuchElementException:
#                 text = "Element not found"
#             except StaleElementReferenceException:
#                 text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']")))
#             except StaleElementReferenceException:
#                 text = "Element not found"
#         except StaleElementReferenceException:
#             href = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']")))
#         except StaleElementReferenceException:
#             href = "Element not found"
#         except NoSuchElementException:
#             href = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']")))
#         except NoSuchElementException:
#             href = "Element not found"
#         print(f"{CYCLE_INDEX}. Вакансия: {text}, ссылка: {href}")
#     actions.move_to_element(next_page).click(next_page).perform()

for a in href_button_next:
    vacancy_link = driver.find_elements(By.XPATH, "//a[@class='serp-item__title']")
    for i in vacancy_link:
        CYCLE_INDEX += 1
        try:
            href = i.get_attribute("href")
            try:
                text = i.text
            except (NoSuchElementException, StaleElementReferenceException):
                text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']"))).text
        except (NoSuchElementException, StaleElementReferenceException):
            href = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']"))).get_attribute("href")
        print(f"{CYCLE_INDEX}. Вакансия: {text}, ссылка: {href}")
    actions.move_to_element(next_page).click(next_page).perform()
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))


driver.quit()

if __name__ == "__main__":
    pass
