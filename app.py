from flask import Flask, render_template
from models import init_db
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    init_db()  # Initialize the database before running the app.
    app.run(debug=True)
