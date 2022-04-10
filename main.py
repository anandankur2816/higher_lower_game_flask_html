# Create a flask app for higher lower game
from flask import Flask, render_template, request, redirect, url_for
from random import randint

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


def make_underline(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


no = randint(0, 10)


@app.route('/')
def index():
    return "<h1> Guess the number between 0 and 9 </h1> " \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'> <br> <a href='/'>" \
           " Guess the number and go to 'guess/<your_guessed_no>'  </a>"


@app.route('/guess/<int:user_input>')
def fun(user_input):
    if user_input == no:
        return redirect(url_for('win'))
    elif user_input > no:
        return redirect(url_for('high'))
    else:
        return redirect(url_for('low'))


@app.route('/high')
def high():
    return "<h1 color='red'> Too High. Guess Again </h1> " \
           "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'> </img>"


@app.route('/low')
def low():
    return "<h1 color='green'> Too Low. Guess Again </h1> " \
           "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'> </img>"


@app.route('/win')
def win():
    return "<h1> You Win </h1> " \
           "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'> </img>"

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Good Bye"



if __name__ == '__main__':
    app.run(debug=True, port=5000)

