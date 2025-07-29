from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        selection = request.form['option']
        # Example processing logic
        result = f"You selected: {selection.upper()}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

