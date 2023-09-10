from selenium import webdriver # это для бравзера
from selenium.webdriver.common.by import By # это для парсинга
import time # это на всякий случай для ожидания, но там встроенный метод есть его потом импортировать надо
from selenium.webdriver.chrome.options import Options # это для опций
# это счетчик итераций (это я просто жаваскриптер, он в жсе юзается и он там по умолчанию его не надо объявлять)
CYCLE_INDEX = 0
# Это создание опции хеадлесс чтобы оно не открывало каждый раз браузер
chrome_options = Options()
chrome_options.add_argument("--headless")
# Экземпляр класса
driver = webdriver.Chrome(options=chrome_options)
# загрузка страницы
print("Loading page...")
driver.get("https://hh.ru/search/vacancy?text=Python&salary=&ored_clusters=true&enable_snippets=true&area=1")
# это вот основной дроч
# element = driver.find_elements(
#     By.XPATH, '//span[@data-page-analytics-event="vacancy_search_suitable_item"]/@href')
# get_vacancy_title = driver.find_elements(By.CLASS_NAME, 'serp-item__title') 
# не забывай что надо использовать цикл фор как минимум потому что driver.find_elementS возвращает список
# а список надо перебирать циклом фор
# for i in element:
#     CYCLE_INDEX += 1
#     print(CYCLE_INDEX, i.text)

# закрытие бравзера
driver.quit()
# это похуй
if __name__ == "__main__":
    pass
