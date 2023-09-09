from bs4 import BeautifulSoup
import requests
from forhttp import cookies, headers, params
from lxml import etree

import requests

vacancy = []

for_searching = "Маркетолог"
text_string = params['text'] = for_searching


def download_pages(start_url):
    url = start_url
    while url is not None:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        with open(f"{url.split('/')[-1]}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        next_link = soup.find('a', {'rel': 'nofollow'})  # modify this line according to the site's structure
        url = next_link['href'] if next_link else None

start_url = 'https://hh.ru/search/vacancy?area=1&employment=full&employment=part&employment=probation&excluded_text=маркетплейсы+вайлдберис+озон+недвижимость+стройка&experience=noExperience&industry=7.541&industry=7.539&industry=11.459&industry=44.393&professional_role=170&professional_role=2&professional_role=3&professional_role=37&professional_role=163&professional_role=68&schedule=fullDay&schedule=shift&schedule=flexible&search_field=name&search_field=company_name&search_field=description&clusters=true&enable_snippets=true&no_magic=true&ored_clusters=true&order_by=salary_asc&page=0'
download_pages(start_url)

response = getting_html()

# with open("index1.html", encoding="utf-8") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")
# xml_doc = src
# all_vacancies_hrefs = soup.find_all(class_="serp-item__title")
# # all_vacancies_hrefs = soup.select(".serp-item__title")
# # all_vacancies_hrefs = soup.find(class_="serp-item").find("span").find_all("a")

# # all_vacancies_hrefs = soup.find_all('h3')

# # print(all_vacancies_hrefs)
# print(len(all_vacancies_hrefs))

# for i, item in enumerate(all_vacancies_hrefs):
#      item_text = item.text
#      item_href = item.get("href")
#      print(f"{i+1}. {item_text}: {item_href}")


