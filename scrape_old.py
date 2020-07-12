import re
import requests
from clean_old import get_question
from bs4 import BeautifulSoup
import io

main = 'https://byjus.com/maths/important-questions-class-10-maths/'
page = requests.get(main)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("table", class_='table-striped')
links = results.find_all('a')

URLS = []
titles = []

for i in range (0, len(links)):
    URLS.append(links[i]['href'])
    titles.append(links[i].string.strip("Important Questions"))

for i in range (0, len(URLS)):
    page = requests.get(URLS[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find("article", class_='post')
    results = results.text.replace("\xa0"," ")
    text = results.split('\n')
    questions = get_question(text)
    with io.open('data/' + titles[i],"w", encoding="utf-8") as file:
        print(titles[i])
        for question in questions:
            file.write(question + '\n')