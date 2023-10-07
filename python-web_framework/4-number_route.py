from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    text = escape(text.replace('_', ' '))
    return "C {}".format(text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_variable(text):
    text = escape(text.replace('_', ' '))
    return "Python {}".format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        return "Not Found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
