from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'David Weirich',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 1, 2020',
    },
    {
        'author': 'Emily Huang',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 2, 2020',
    },

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
