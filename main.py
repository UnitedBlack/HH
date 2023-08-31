
# import requests
# import lxml
# from bs4 import BeautifulSoup as bs

# response = requests.get('https://hh.ru/search/vacancy',
#                         params=params, cookies=cookies, headers=headers)  # Делает хттп запрос на сайт хх

# with open("RequestResult.html", "w", encoding="utf-8") as file:
#     file.write(response.text)  # Конвертирует полученный запрос в html файл RequestResult.html в папке найдешь

# soup = bs(response.content, 'html.parser')  # переопределение для работы с библиотекой soup, 
# # эта библиотека позволяет парсить хтмл который мы скачали и сохранили на предыдущей строке

# title = soup.find_all('a', class_="serp-item__title") # парсит каждый блок с вакансией 
# respond_button = soup.find_all(
#     class_="bloko-button bloko-button_kind-success bloko-button_scale-small").find("span")
# # парсит кнопки "откликнуться" в каждом блоке вакансий
# print(respond_button)
