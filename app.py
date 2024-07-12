from flask import Flask, url_for, render_template
from forms import inputForm
import time
import pandas as pd
import joblib

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = inputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            airline = [form.airline.data],
            date_of_journey = [form.date_of_journey.data.strftime("%Y-%m-%d")],
            source = [form.source.data],
            destination = [form.dest.data],
            dep_time = [form.dep_time.data.strftime("%H:%M:%S")],
            arrival_time = [form.arr_time.data.strftime("%H:%M:%S")],
            duration = [form.duration.data],
            total_stops = [form.stops.data],
            additional_info = [form.add_info.data]
        ))
        prediction = model.predict(x_new)[0]
        message = f"Predicted Price = {prediction:,.0f} INR"
    else:
        message = "Provide Valid Credentials"
    return render_template("predict.html", title="Predict", form=form, output=message)




if __name__ == "__main__":
    app.run(debug=True)