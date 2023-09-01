from bs4 import BeautifulSoup
import requests
from forhttp import cookies, headers, params

# url = "https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=&excluded_text=&professional_role=37&professional_role=170&professional_role=163&professional_role=68&industry=8&industry=43&industry=44&industry=49&industry=42&industry=41&industry=27&industry=39&industry=52&industry=7&industry=50&area=1&salary=&currency_code=RUR&experience=noExperience&employment=full&employment=part&employment=probation&schedule=fullDay&schedule=shift&schedule=flexible&order_by=relevance&search_period=0&items_on_page=50&page=0"

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0"
# }

# req = requests.get(url, headers = headers)
# src = req.text

# print(src)

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open("index.html", encoding="utf-8") as file:
     src = file.read()

soup = BeautifulSoup(src, "lxml")
all_vacancies_hrefs = soup.find_all(class_="serp-item__title")

for item in all_vacancies_hrefs:
     item_text = item.text
     item_href = item.get("href")
     print(f"{item_text}: {item_href}")


