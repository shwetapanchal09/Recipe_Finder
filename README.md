# Recipe Finder

Recipe Finder is a Flask web application that allows users to search for recipes based on ingredients and view detailed information about each recipe. The application utilizes the Spoonacular API to fetch recipe data and displays it on a user-friendly interface.

## Features

- **Search Recipes**: Enter an ingredient to find related recipes.
- **View Recipe Details**: Click on a recipe to view its detailed information, including ingredients, instructions, and nutritional data.
- **Responsive UI**: User-friendly interface with basic CSS styling.

## Tech Stack

- **Flask**: A lightweight WSGI web application framework for Python.
- **HTML/CSS**: For the front-end interface.
- **Spoonacular API**: Provides recipe data.
- **dotenv**: For managing environment variables.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/recipe-finder.git
   cd recipe-finder
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables**:

   - Create a `.env` file in the root directory.
   - Add your Spoonacular API key to the `.env` file:

     ```
     API_KEY=your_spoonacular_api_key_here
     ```

5. **Run the Application**:

   ```bash
   python app.py
   ```

6. **Open Your Browser**:

   Navigate to `http://localhost:5000` to use the application.

## File Structure

```
recipe-finder/
│
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html         # Home page for searching recipes
│   └── recipe.html        # Recipe details page
│
├── static/
│   └── style.css          # Basic CSS styling for the app
│
├── .env                   # Environment variables file (contains API key)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## How to Use

1. **Search for Recipes**:
   - Enter an ingredient in the search box on the home page.
   - Click the "Search" button to fetch recipes related to the ingredient.
  
2. **View Recipe Details**:
   - Click on a recipe title to view detailed information.
   - The details page shows ingredients, instructions, and nutritional information (if available).

## Shift Type Handling

- **Automatic Shift Type Assignment**:
  - If both `from_time` and `to_time` are provided in a Timesheet, the `shift_type` is automatically set to "Office Shift."
  - If no times are provided, the `shift_type` is set to "Work From Home."
  - If a leave is applied, the `shift_type` changes to "On Leave."

## Error Handling

- **Troubleshooting Save Issues**:
  - Encountered a `500 Internal Server Error` when saving Timesheet data under certain conditions.
  - Debugged and adjusted server and client-side handling to resolve data parsing issues.

## Dependencies

- **Flask**: Web framework for Python.
- **requests**: For making API calls to the Spoonacular API.
- **dotenv**: To manage environment variables securely.

## API Key

To use the Spoonacular API, you need an API key. You can obtain it from the [Spoonacular website](https://spoonacular.com/food-api).



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Spoonacular API](https://spoonacular.com/food-api) for providing recipe data.
- [Flask](https://flask.palletsprojects.com/) for the backend framework.
```

