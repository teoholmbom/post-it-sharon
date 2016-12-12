from flask import Flask, render_template
from food import Food
import pickle

foods = ();

app = Flask(__name__)


@app.route('/')
def show_foods():
    return render_template('show_foods.html', foods=foods)


if __name__ == '__main__':
    # Tuple with objects of Food
    # foods0 = (
    #    Food('Banana', 200, 'Southeast Asia', 'Is a herb.'),
    #    Food('Watermelon', 30, 'Southern Africa', 'Worlds biggest berry.'),
    #    Food('Kale', 50, 'Greece', 'The closest relative to wild cabbage.')
    # )
    # pickle.dump(foods0, open("save.p", "wb"))

    foods = pickle.load(open("save.p", "rb"))
    print(foods)
    app.run()
