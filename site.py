from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from functools import reduce
import os

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/scrape_db')
client = MongoClient(host=f"{host}?retryWrites=false")
db = client.get_default_database()

web_site = db.web_site






@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', suits=space_suits.find())


@app.route('/new')
def new_suit():
    """Return new suit creation page."""
    return render_template('new_suit.html')

@app.route('/new', methods=['POST'])
def create_suit():
    """Make a new suit posting according to user's specifications."""
    suit = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    suit_id = space_suits.insert_one(suit).inserted_id
    return redirect(url_for('show_suit', suit_id=suit_id))

@app.route('/suit/<suit_id>')
def show_suit(suit_id):
    """Show a single suit."""
    suit = space_suits.find_one({'_id': ObjectId(suit_id)})
    return render_template('show_suit.html', suit=suit)

@app.route('/edit/<suit_id>', methods=['POST'])
def update_suit(suit_id):
    """Edit a suit posting."""
    new_suit = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'img_url': request.form.get('img_url')
    }
    space_suits.update_one(
        {'_id': ObjectId(suit_id)},
        {'$set': new_suit}
    )
    return redirect(url_for('show_suit', suit_id=suit_id))

@app.route('/delete/<suit_id>', methods=['POST'])
def delete_suit(suit_id):
    """Delete a suit."""
    space_suits.delete_one({'_id': ObjectId(suit_id)})
    return redirect(url_for('index'))

@app.route('/edit/<suit_id>', methods=['GET'])
def edit_suit(suit_id):
    """Page to submit an edit on a suit."""
    suit = space_suits.find_one({'_id': ObjectId(suit_id)})
    return render_template('edit_suit.html', suit=suit)




if __name__ == '__main__':
    app.run(debug=True)
