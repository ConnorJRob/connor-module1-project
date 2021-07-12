import re
from flask import Flask, render_template

from controllers.adventurer_controller import adventurers_blueprint
from controllers.lesson_controller import lessons_blueprint
from controllers.enrolment_controller import enrolments_blueprint

app = Flask(__name__)

app.register_blueprint(adventurers_blueprint)
app.register_blueprint(lessons_blueprint)
app.register_blueprint(enrolments_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)