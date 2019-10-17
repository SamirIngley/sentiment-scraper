from newspaper import Article
from PIL import Image

# uz = 'nytimes.com/interactive/2019/10/15/us/elections/debate-speaking-time.html?action=click&module=Top%20Stories&pgtype=Homepage'
# url_list = [uz]


article = Article('nytimes.com/interactive/2019/10/15/us/elections/debate-speaking-time.html?action=click&module=Top%20Stories&pgtype=Homepage')
article.download()
article.parse()
article.nlp()
article.authors
