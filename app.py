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




@app.route('/')
def index():
    """Return homepage."""

    return render_template('index.html', sites=web_sites.find())



@app.route('/updated', methods=["POST"])
def updated():
    url = request.form.get('url')

    article_list = list()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    article_list.append((article.authors))
    article_list.append((article.publish_date))
    article_list.append((article.keywords))
    article_list.append((article.summary))
    return render_template('index.html', article_list=article_list)


@app.route('/new')
def new_site():
    """Return new site creation page."""
    return render_template('new_site.html')

@app.route('/', methods=['POST'])
def create_site():
    """Make a new suit posting according to user's specifications."""
    site = {
        'url': request.form.get('url')
    }
    site_id = web_sites.insert_one(site).inserted_id
    return redirect(url_for('index.html', site_id=site_id))

@app.route('/site/<site_id>')
def show_sum(suit_id):
    """Show a single suit."""
    site = web_sites.find_one({'_id': ObjectId(site_id)})
    return render_template('index.html', site=site)

@app.route('/edit/<site_id>', methods=['POST'])
def update_suit(site_id):
    """Edit a suit posting."""
    new_site = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    web_sites.update_one(
        {'_id': ObjectId(site_id)},
        {'$set': new_site}
    )
    return redirect(url_for('show_site', site_id=site_id))

@app.route('/delete/<site_id>', methods=['POST'])
def delete_site(site_id):
    """Delete a suit."""
    web_sites.delete_one({'_id': ObjectId(site_id)})
    return redirect(url_for('index'))

@app.route('/edit/<site_id>', methods=['GET'])
def edit_site(site_id):
    """Page to submit an edit on a suit."""
    site = web_sites.find_one({'_id': ObjectId(site_id)})
    return render_template('edit_site.html', site=site)



if __name__ == '__main__':
    app.run(debug=True)
