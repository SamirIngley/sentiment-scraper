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


source = requests.get('https://medium.com/topic/editors-picks').content
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

# with open('index2.html', 'w') as out:
#     out.write(soup.prettify())

article_list = soup.select('h3') # list of articles
for article in article_list:
    print(article.text)
#print(article_list.text)

# for article in article_list:
#     print(article.title)
#     print(article.)
#     print(article.text)
#     # try:
#     headline = article.find_all('h3').text
#     # except Exception as e:
#     #     headline = article.h2.text
#
#     # author = article.find('a', class_="ds-link ds-link--styleSubtle postMetaInline postMetaInline--author").text
#     # time = article.find('span', class_="readingTime")['title']
#     # summary = article.find('div', class_="ui-summary ui-clamp3").text
#     # link = article.find()
#
#     print(headline)
#     # print('By: ' + author + '   ' + time)
#     # print(summary)
#
#     print()
