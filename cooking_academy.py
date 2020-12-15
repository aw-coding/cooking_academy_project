from flask import Flask, render_template, Blueprint
from controllers.member_controller import members_blueprint
from controllers.lessons_controller import lessons_blueprint
from controllers.bookings_controller import bookings_blueprint





cooking_academy = Flask(__name__)




if __name__ == '__main__':
    cooking_academy.run(debug=True)

cooking_academy.register_blueprint(members_blueprint)
cooking_academy.register_blueprint(lessons_blueprint)
cooking_academy.register_blueprint(bookings_blueprint)


@cooking_academy.route('/')
def home():
    return render_template('index.html')