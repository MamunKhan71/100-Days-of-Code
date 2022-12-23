from flask import Flask
import random

app = Flask(__name__)
randomNum = random.randint(0, 9)
userInput = 0


def dec(fn):
    def wrapper():
        if userInput < randomNum:
            return "<h1 align='center'>Too Low, Try Again!!</h1> <br>" \
                   "<center><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=300px " \
                   "</center></img> "
        elif userInput > randomNum:
            return "<h1 align='center'>Too High, Try Again!!</h1> <br>" \
                   "<center><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=300px " \
                   "</center></img> "
        else:
            return "<h1 align='center'>You Found ME!</h1> <br>" \
                   "<center><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=300px " \
                   "</center></img> "

    return wrapper


@app.route('/')
def sayhi():
    return "<h1 align='center'>Guess the number between 0 and 9</h1> <br>" \
           "<center><img src='https://media.giphy.com/media/hqgD6bocRHhEjamBPA/giphy.gif' width=300px </center></img>"


@app.route('/<int:number>')
def inputGetter(number):
    global userInput
    userInput = number


if __name__ == "__main__":
    app.run(debug=True)
