from flask import Flask, render_template
from controllers.member_controller import members_blueprint
from controllers.lessons_controller import lessons_blueprint


cooking_academy = Flask(__name__)



cooking_academy.register_blueprint(members_blueprint)
cooking_academy.register_blueprint(lessons_blueprint)


@cooking_academy.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    cooking_academy.run(debug=True)