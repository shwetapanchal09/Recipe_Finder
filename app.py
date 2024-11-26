from flask import Flask, render_template, request
import requests
from dotenv  import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
# Replace this with an actual API endpoint that provides recipe data
API_URL = "https://api.spoonacular.com/recipes/complexSearch"
API_KEY = os.getenv('API_KEY')

# Home route with a search form
@app.route('/')
def index():
    return render_template('index.html')

# Route to display recipe search results
@app.route('/search', methods=['GET'])
def search():
    ingredient = request.args.get('ingredient')
    if ingredient:
        # Query the API with the search term
        params = {
            'apiKey': API_KEY,
            'query': ingredient,
            'number': 10,  # Limit the number of results
        }
        response = requests.get(API_URL, params=params)
        data = response.json()
        recipes = data.get('results', [])
    else:
        recipes = []

    return render_template('index.html', recipes=recipes, ingredient=ingredient)

# Route to display detailed recipe info
@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe_info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    response = requests.get(recipe_info_url, params={'apiKey': API_KEY})
    recipe = response.json()
    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)

