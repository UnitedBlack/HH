import re
import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from lxml import html
from params import params, cookies, headers

class DescriptionParserGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Description Parser GUI')
        self.setGeometry(100, 100, 800, 600)

        self.file_label = QLabel('File Name:')
        self.file_input = QLineEdit()
        
        self.name_regex_label = QLabel('Name Regex:')
        self.name_regex_input = QLineEdit()
        self.name_regex_input.setText(r"(\d+\.\s.*?),")
        
        self.url_regex_label = QLabel('URL Regex:')
        self.url_regex_input = QLineEdit()
        self.url_regex_input.setText(r"\s(https:\/\/[\w\/.?=-]+)")
        
        self.parse_button = QPushButton('Parse')
        self.parse_button.clicked.connect(self.description_parser)

        self.result_text = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_input)
        layout.addWidget(self.name_regex_label)
        layout.addWidget(self.name_regex_input)
        layout.addWidget(self.url_regex_label)
        layout.addWidget(self.url_regex_input)
        layout.addWidget(self.parse_button)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def description_parser(self):
        file_name = self.file_input.text()
        name_re = self.name_regex_input.text()
        url_re = self.url_regex_input.text()
        
        with open(file_name, 'r', encoding='utf-8') as file:
            for current_vacancy in file:
                regexped_name = re.search(name_re, current_vacancy).group()
                regexped_url = re.search(url_re, current_vacancy).group()
                response = requests.get(regexped_url, params=params, cookies=cookies, headers=headers)
                html_string = response.text
                root = html.fromstring(html_string)

                vacancy_main_title = " ".join(root.xpath('//h1[@data-qa="vacancy-title"]/text()'))
                vacancy_response_button_url = " ".join(root.xpath('//a[@data-qa="vacancy-response-link-top"]/@href'))
                vacancy_company_name = " ".join(root.xpath('//a[@data-qa="vacancy-company-name"]/span/text()'))
                vacancy_description = " ".join(root.xpath('//div[@data-qa="vacancy-description"]//text()'))
                
                # Append the result to the QTextEdit widget
                self.result_text.append(f"Name: {vacancy_main_title}")
                self.result_text.append(f"URL: {vacancy_response_button_url}")
                self.result_text.append(f"Company: {vacancy_company_name}")
                self.result_text.append(f"Description: {vacancy_description}\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DescriptionParserGUI()
    window.show()
    sys.exit(app.exec_())
