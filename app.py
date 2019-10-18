from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from functools import reduce
import os
from newspaper import Article
from PIL import Image
import nltk

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/scrape_db')
client = MongoClient(host=f"{host}?retryWrites=false")
db = client.get_default_database()

web_sites = db.sites

article_list = list()


@app.route('/')
def index():
    """Return homepage."""

    return render_template('index.html', sites=web_sites.find())



@app.route('/updated', methods=["POST"])
def updated():
    url = request.form.get('url')

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    article_list.append((article.authors))
    article_list.append((article.publish_date))
    article_list.append((article.keywords))
    article_list.append((article.summary))
    return render_template('index.html', article_list=article_list)







if __name__ == '__main__':
    app.run(debug=True)
