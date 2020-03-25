from flask import Flask
from flask import render_template
from .db import POST

app = Flask(__name__)

"""
MVC
"""


@app.route('/')
def index():
    page_title = 'My first page'
    name = ['MyPage', 'hello']
    return render_template('index.html', page_title=page_title, name=name)


@app.route('/posts')
def posts():
    return render_template('posts.html', posts=POST)


@app.route('/post/')
@app.route('/post/<int:post_id>')
def post(post_id=None):

    return render_template('post_body.html', post_body=POST[post_id-1])


@app.route('/hi')
def hola():
    names = ['Igor',
             'Anton',
             'Max',
             'Ann',
             'Luiz']
    return render_template('hi.html', names=names)


if __name__ == '__main__':
    app.run(debug=True)
