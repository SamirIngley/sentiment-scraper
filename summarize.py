from newspaper import Article
from PIL import Image
import nltk


# uz = 'nytimes.com/interactive/2019/10/15/us/elections/debate-speaking-time.html?action=click&module=Top%20Stories&pgtype=Homepage'
# url_list = [uz]

#nltk.download('punkt')

url = 'https://medium.com/@jeric.hunter/bartornot-a3030fb819b5'

article = Article(url)
print(article)
article.download()
article.parse()
article.nlp()
print(article.authors)
print(article.publish_date)
print(article.keywords)
print(article.summary)
