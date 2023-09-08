from bs4 import BeautifulSoup
import requests
from forhttp import cookies, headers, params
from lxml import etree

import requests

vacancy = []

for_searching = "Маркетолог"
text_string = params['text'] = for_searching


def getting_html():
    response = requests.get('https://hh.ru/search/vacancy',
                            params=params, cookies=cookies, headers=headers)

    with open("index1.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    return response

response = getting_html()

with open("RequestResult.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
xml_doc = src
all_vacancies_hrefs = soup.find_all(class_="serp-item__title")
# all_vacancies_hrefs = soup.select(".serp-item__title")
# all_vacancies_hrefs = soup.find(class_="serp-item").find("span").find_all("a")

# all_vacancies_hrefs = soup.find_all('h3')

# print(all_vacancies_hrefs)
print(len(all_vacancies_hrefs))

# for i, item in enumerate(all_vacancies_hrefs):
#      item_text = item.text
#      item_href = item.get("href")
#      print(f"{i+1}. {item_text}: {item_href}")
