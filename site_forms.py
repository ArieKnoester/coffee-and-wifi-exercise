# https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
# https://wtforms.readthedocs.io/en/3.0.x/
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL


class AddCafeForm(FlaskForm):
    name = StringField(
        label="Cafe Name",
        validators=[DataRequired()]
    )
    location = URLField(
        label="Cafe Location on Google Maps (URL)",
        validators=[URL(), DataRequired()]
    )
    opens = StringField(
        label="Opening Time e.g. 8AM",
        validators=[DataRequired()]
    )
    closes = StringField(
        label="Closing Time e.g. 5:30PM",
        validators=[DataRequired()]
    )
    coffee_rating = SelectField(
        label="Coffee Rating",
        choices=["", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
        validators=[DataRequired()]
    )
    wifi_rating = SelectField(
        label="Wi-Fi Strength Rating",
        choices=["", "✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()]
    )
    power_availability = SelectField(
        label="Power Socket Availability",
        choices=["", "✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Add Cafe")
