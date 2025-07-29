# app.py
from flask import Flask, render_template, request
import importlib
from . import main
from . import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    country_code = request.form['country_code'].lower()

    # Overwrite config.COUNTRY_CODES dynamically
    config.COUNTRY_CODES.clear()
    config.COUNTRY_CODES.append(country_code)

    try:
        main.main()
        result = f"Successfully processed and saved data for country code '{country_code.upper()}'."
    except Exception as e:
        result = f"An error occurred: {str(e)}"

    return f"<h2>Result:</h2><p>{result}</p>"

if __name__ == '__main__':
    app.run(debug=True)
