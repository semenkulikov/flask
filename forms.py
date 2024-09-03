from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField


class Base(FlaskForm):
    """ Базовый класс для форм """
    def __init__(self):
        super().__init__()
