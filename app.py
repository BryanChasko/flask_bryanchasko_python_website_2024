from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

@app.route('/')
def home():
    """Render Home Page."""
    return render_template('home.html', title='Home Page')

@app.route('/blog.html')
def blog():
    """Render Blog Page."""
    return render_template('blog.html', title='Blog Page')

@app.route('/portfolio.html')
def portfolio():
    """Render Portfolio Page."""
    return render_template('portfolio.html', title='Portfolio Page')

@app.route('/experience.html')
def experience():
    """Render Experience Page."""
    return render_template('experience.html', title='Experience Page')

@app.route('/contact.html')
def contact():
    """Render Contact Page."""
    return render_template('contact.html', title='Contact Page')

freezer = Freezer(app)

@freezer.register_generator
def url_generator():
    """Generate URLs for pages."""
    yield '/'
    yield '/blog.html'
    yield '/portfolio.html'
    yield '/experience.html'
    yield '/contact.html'

if __name__ == '__main__':
    app.config['FREEZER_DESTINATION'] = 'build'
    freezer.freeze()
    app.run(debug=False)
