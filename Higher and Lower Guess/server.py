from flask import Flask
import random

app = Flask(__name__)
randomNum = random.randint(0, 9)


@app.route('/')
def sayhi():
    return "<h1 align='center'>Guess the number between 0 and 9</h1> <br>" \
           "<center><img src='https://media.giphy.com/media/hqgD6bocRHhEjamBPA/giphy.gif' width=300px </center></img>"


def high():
    return "<h1 align='center'>Too High, Try Again!!</h1> <br>" \
           "<center><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=300px </center></img>"


def low():
    return "<h1 align='center'>Too Low, Try Again!!</h1> <br>" \
           "<center><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=300px </center></img>"


def found():
    return "<h1 align='center'>You Found ME!</h1> <br>" \
           "<center><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=300px </center></img>"


def choice_validator(userInput, randomInt):
    if userInput == randomInt:
        found()
    elif userInput > randomInt:
        high()
    else:
        low()


@app.route('/<int:number>')
def inputGetter(number):
    userInput = number
    print(randomNum)
    print(userInput)
    choice_validator(userInput, randomNum)

    return "Hello "


if __name__ == "__main__":
    app.run(debug=True)
