import re
import requests
from params import params, cookies, headers
from lxml import html

# reg_exp_vacancy = r'(.*:\s)(https?:\/\/\S*)'
vacancy_name_regexp = r"(\d+\.\s.*?),"
vacancy_url_regexp = r"\s(https:\/\/[\w\/.?=-]+)"


def description_parser(name_re=vacancy_name_regexp, url_re=vacancy_url_regexp):
    with open('Parsed-23-00.txt', 'r', encoding='utf-8') as file:
        for current_vacancy in file:
            regexped_name = re.search(name_re, current_vacancy).group()
            regexped_url = re.search(url_re, current_vacancy).group()

            print(regexped_name)
            response = requests.get(regexped_url, params=params, cookies=cookies, headers=headers)

            html_string = response.text
            root = html.fromstring(html_string)

            vacancy_main_title = root.xpath(
                '//h1[@data-qa="vacancy-title"]/text()')
            vacancy_response_button_url = root.xpath(
                "//a[@class='bloko-button bloko-button_kind-success bloko-button_scale-large bloko-button_stretched']/@href[1]")
            # print(vacancy_response_button_url)
            vacancy_company_name = root.xpath('//a[@data-qa="vacancy-company-name"]/span/text()')
            print(vacancy_company_name)
            vacancy_description = ""


description_parser()

# try:
#                 driver.get(response_url)
#                 description_find_xpath = driver.find_element(
#                     By.CLASS_NAME, "g-user-content").text
#                 # description_get_element = description_find_xpath.get_attribute("div")
#             except (NoSuchElementException):
#                 driver.get(response_url)
#                 vacancy_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
#                     By.CLASS_NAME, "g-user-content"))).text
#                 # description_get_element = description_find_xpath.get_attribute("div")
#             print(description_find_xpath)
