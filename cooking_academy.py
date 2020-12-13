from flask import Flask, render_template


cooking_academy = Flask(__name__)


@cooking_academy.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    cooking_academy.run(debug=True)