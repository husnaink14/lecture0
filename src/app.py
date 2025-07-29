from flask import Flask, render_template, request, redirect, url_for, flash
from . import main
from . import config

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    country_code = request.form['country_code'].strip().lower()

    if not country_code.isalpha() or len(country_code) != 2:
        flash("Please enter a valid 2-letter country code.", "error")
        return redirect(url_for('index'))

    # Update the COUNTRY_CODES list dynamically
    config.COUNTRY_CODES.clear()
    config.COUNTRY_CODES.append(country_code)

    try:
        main.main()
        flash(f"Successfully processed and saved data for country code '{country_code.upper()}'.", "success")
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
