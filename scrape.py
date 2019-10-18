from bs4 import BeautifulSoup
import requests

source = requests.get('https://medium.com/topic/editors-picks').content
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

# with open('index2.html', 'w') as out:
#     out.write(soup.prettify())

articles = soup.find_all('section', class_="gt gu ae co l gv gw gx gy gz")

for article in articles:
    print()
    headline = article.find('h3', class_="am ax ej bt ek bu fo hi hj ap as fp ep eq ar")
    print(headline.text)
    author = article.find('span', class_="bt b bu bv bw bx ap as es ep eq ar am ax")
    time = article.find('div', class_="gg t cv")
    print('     ' + author.text + '       ' + time.text)
    summary = article.find('h3', class_="bt fm fn fo as fp ep ap eq ar by")
    print(summary.text)
