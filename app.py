import os
print(os.getcwd())  # This will print the current working directory to ensure Flask is running from the correct location.

from flask import Flask, render_template, redirect, url_for, request, session
from wtforms import Form, StringField, PasswordField, FloatField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Your existing app code...
from flask import Flask, render_template, redirect, url_for, request, session
from wtforms import Form, StringField, PasswordField, FloatField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session handling

# Login Form
class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Next")

# BMI Form
class BMIForm(Form):
    weight = FloatField("Weight (kg)", validators=[DataRequired()])
    height = FloatField("Height (m)", validators=[DataRequired()])
    submit = SubmitField("Calculate BMI")

@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        session["username"] = form.username.data
        return redirect(url_for("bmi"))
    return render_template("login.html", form=form)

@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    form = BMIForm(request.form)
    bmi_result = None
    if request.method == "POST" and form.validate():
        weight = form.weight.data
        height = form.height.data
        bmi_result = round(weight / (height ** 2), 2)
    return render_template("bmi.html", form=form, bmi_result=bmi_result)

if __name__ == "__main__":
    app.run(debug=True)
