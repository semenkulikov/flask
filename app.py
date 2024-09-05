from flask import Flask, render_template
from models import init_db
from logger import my_handler, stream_handler
import logging
app = Flask(__name__)

app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)
app_logger.addHandler(my_handler)
app_logger.addHandler(stream_handler)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    init_db()  # Initialize the database before running the app.
    app_logger.info("Starting the Flask application...")  # Log the start of the app
    app.run(debug=True)
