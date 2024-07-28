from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    json_path = os.path.join(app.root_path, 'json', 'index_cards.json' )

    with open(json_path, 'r', encoding='utf-8') as f:
        cards =json.load(f)

    return render_template('index.html', cards=cards)


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
