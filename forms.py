from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, TimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd

train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")



class inputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=X_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )

    date_of_journey = DateField(
        label="Date of Journey",
        validators=[DataRequired()]
    )

    source = SelectField(
        label="Source",
        choices=X_data.source.unique().tolist(),
        validators=[DataRequired()]
    )

    dest = SelectField(
        label="Destination",
        choices=X_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )

    dep_time = TimeField(
        label="Departure Time",
        validators=[DataRequired()]
    )

    arr_time = TimeField(
        label="Arrival Time",
        validators=[DataRequired()]
    )

    duration = IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )

    stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )

    add_info = SelectField(
        label="Additional Info",
        choices=X_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )

    submit = SubmitField("Predict")