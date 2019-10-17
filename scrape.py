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


source = requests.get('https://medium.com').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    print(article.text)
    #print(article.prettify())
    # headline = article.h1.text
    # author = article.div.text
    # print(headline)
    # print(author)
    print()
