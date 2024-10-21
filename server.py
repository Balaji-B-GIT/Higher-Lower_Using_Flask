from flask import Flask
import random
app = Flask(__name__)

random_number = random.randrange(0,9)



def ans(random_num):
    @app.route('/<int:number>')
    def wrapper(number):
        if number < random_num:
            return ('<h1 style = "color:red">Too low, Try again</h1>'
            '<img align="center" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="">')
        elif number > random_num:
            return ('<h1 style = "color:purple">Too high, Try again</h1>'
            '<img align="center" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="">')
        else:
            return ('<h1 style = "color:green">You Found!!!</h1>'
            '<img align="center" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="">')


@app.route('/')
def guess_the_num():
    return ('<h1>Guess the number between 0 to 9</h1>'
            '<img align="center" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="">')

@ans
def guess_the_num():
    return ('<h1>Guess the number between 0 to 9</h1>'
            '<img align="center" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="">')



if __name__ == "__main__":
    app.run(debug=True)