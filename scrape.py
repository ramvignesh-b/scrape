import re
import requests
# from clean import get_question
from bs4 import BeautifulSoup
import io

main = 'https://byjus.com/maths/important-questions-class-10-maths/'
page = requests.get(main)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("table", class_='table-striped')
links = results.find_all('a')

URLS = []
titles = []
text = ''
flag = 0

for i in range (0, len(links)):
    URLS.append(links[i]['href'])
    titles.append(links[i].text.strip("Important Questions"))
'''
# Try getting the questions via <strong> tag
for i in range (0, len(URLS)):
    page = requests.get(URLS[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("strong")
    for result in results:
        if re.search('^Q.', result.text) or re.search('^[0-9]', result.text):
            flag = 1 
        if flag:
            text += result.text + '\n'
    filename = 'data/' + titles[i]
    with io.open(filename,"w", encoding="utf-8") as file:
        file.write(text + '\n')
    text = ''
'''

# Combine Question and solutions
for i in range (0, len(URLS)):
    page = requests.get(URLS[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find("article", class_="post")
    results = results.find_all("p")
    for result in results:
        if re.search('^Q.', result.text) or re.search('^[0-9].', result.text):
            text += '\n'
            flag = 1 
        if flag:
            text += result.text + '\n'
    filename = 'combined/' + titles[i]
    print(titles[i])
    with io.open(filename,"w", encoding="utf-8") as file:
        file.write(text + '\n')
    text = ''
    flag = 0