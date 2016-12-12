from flask import Flask, render_template, request
from food import Food
import pickle

foods = ();

app = Flask(__name__)

def createPickle():
    # Create ist with objects of Food
    temp_foods = [
        Food('Banana', 200, 'Southeast Asia', 'Is a herb.'),
        Food('Watermelon', 30, 'Southern Africa', 'Worlds biggest berry.'),
        Food('Kale', 50, 'Greece', 'The closest relative to wild cabbage.')
    ]
    # Create a pickle containing temp_foods list
    pickle.dump(temp_foods, open("save.p", "wb"))


@app.route('/', methods=['GET', 'POST'])
def foods():
    if request.method == 'POST':
        temp_food = Food(request.form['name'], request.form['energy'], 'N/A', request.form['fact'])
        foods.append(temp_food)
        pickle.dump(foods, open("save.p", "wb"))

    return render_template('show_foods.html', foods=foods)



if __name__ == '__main__':
    createPickle()
    foods = pickle.load(open("save.p", "rb"))
    app.run(debug=True)
