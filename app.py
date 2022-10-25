from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<user_dessert>')
def favorite_dessert(user_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f"How did you know I liked {user_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a story to the user that changes based on their selected adjective and noun."""
    return f"Today {noun} is very {adjective}. {noun} just wants to dance but is {adjective} so {noun} is not going to dance."

@app.route('/multiply/<number1>/<number2>')
def multiplication(number1, number2):
    if number1.isdigit() and number2.isdigit():
        calculation = int(number1) * int(number2)
        return f"{number1} times {number2} is {calculation}."
    else:
        return f"Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    if n.isdigit():
        new_word = ''
        for i in range(int(n)):
           new_word = new_word + word + ' '
        return new_word
    else:
       return f"Invalid input. Please try again by entering a word and a number!"

@app.route('/dicegame')
def dicegame():
    random_number = random.randint(1, 6)
    if random_number == 6:
        return f"You rolled a {random_number}. You won!"
    else:
        return f"You rolled a {random_number}. You lost!"



if __name__ == '__main__':
    app.run(debug=True)
