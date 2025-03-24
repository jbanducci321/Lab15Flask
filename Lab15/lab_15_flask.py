from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route('/')
def hello_word():
    return '<p> Nasan : LOL </p>'

@app.route('/jacob')
def add_template():
    return render_template('template.html')

@app.route('/image')
def display_image():
    return render_template('template_image.html')

'''Repository url: https://github.com/jbanducci321/Lab15Flask.git'''