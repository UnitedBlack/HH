import re
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

driver = webdriver.Chrome()
actions = ActionChains(driver)

def description_parser():
    with open('parserHH.txt', 'r', encoding='utf-8') as file:
        for elem in file:
            # print(line)
            reg_exp_vacancy = r'(.*:\s)(https?:\/\/\S*)'
            match = re.match(reg_exp_vacancy, elem)
            if match:
                vacancy_name, response_url = match.groups()
                # print(response_url)
            try:
                driver.get(response_url)
                description_find_xpath = driver.find_element(
                    By.CLASS_NAME, "g-user-content").text
                # description_get_element = description_find_xpath.get_attribute("div")
            except (NoSuchElementException):
                driver.get(response_url)
                vacancy_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                    By.CLASS_NAME, "g-user-content"))).text
                # description_get_element = description_find_xpath.get_attribute("div")
            print(description_find_xpath)


description_parser()

