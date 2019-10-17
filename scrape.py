from bs4 import BeautifulSoup
import requests

# with open('samplesite.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#
# # match = soup.title.text # gives text of first title tag
# # print(soup.prettify()) # indents html file more readable
# # print(match)
#
# article = soup.find('div', class_='article') # div tag w footer class
# # print(article)
#
# headline = article.h2.a.text # dig into headline - h2 tag, a tag, only text
# print(headline)
#
# summary = article.p.text # p tag text gives summary here
# print(summary)


source = requests.get('https://medium.com').text #.text makes it equal to the html in doc
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
print(article.prettify())
print()

headline = article.h1.text
print(' ~ ~ ' + headline)
author = article.find('a', class_="ds-link ds-link--styleSubtle postMetaInline postMetaInline--author").text
time = article.find('span', class_="readingTime")['title']
print('By: ' + author + '   ' + time)
summary = article.find('div', class_="ui-summary ui-clamp3").text
print(summary)
print()
