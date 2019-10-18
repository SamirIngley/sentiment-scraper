from newspaper import Article
from PIL import Image
import nltk


# uz = 'nytimes.com/interactive/2019/10/15/us/elections/debate-speaking-time.html?action=click&module=Top%20Stories&pgtype=Homepage'
# url_list = [uz]

#nltk.download('punkt')
url = 'https://medium.com/'
article_list.append(url)


for item in article_list:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    print()
    print(article.authors)
    print(article.publish_date)
    print(article.keywords)
    print(article.summary)
