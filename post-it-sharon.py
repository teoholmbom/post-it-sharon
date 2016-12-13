from flask import Flask, render_template, request, redirect, url_for
from food import Food
import pickle

foods = []

app = Flask(__name__)


def create_pickle():
    # Create ist with objects of Food
    temp_foods = [
        Food('Banana', 200, 'Southeast Asia', 'Is a herb.'),
        Food('Watermelon', 30, 'Southern Africa', 'Worlds biggest berry.'),
        Food('Kale', 50, 'Greece', 'The closest relative to wild cabbage.')
    ]
    # Create a pickle containing temp_foods list
    pickle.dump(temp_foods, open("save.p", "wb"))


@app.route('/')
def display_foods():
    return render_template('show_foods.html', foods=foods)


@app.route('/food/add', methods=['POST'])
def add_food():
    # Create new Food object with data from form
    temp_food = Food(request.form['name'], request.form['energy'], request.form['origin'], request.form['fact'])
    foods.append(temp_food)
    pickle.dump(foods, open("save.p", "wb"))
    return redirect(url_for('display_foods'))


if __name__ == '__main__':
    while True:
        try:
            foods = pickle.load(open("save.p", "rb"))
            break
        except EOFError:
            create_pickle()
        except ImportError:
            create_pickle()
        except IndexError:
            create_pickle()
        except FileNotFoundError:
            create_pickle()

    app.run(debug=True)
