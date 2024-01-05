from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home Page')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog Page')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfolio Page')

@app.route('/experience')
def experience():
    return render_template('experience.html', title='Experience')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Page')

if __name__ == '__main__':
    freezer = Freezer(app)
    freezer.freeze()
    app.run(debug=True)
