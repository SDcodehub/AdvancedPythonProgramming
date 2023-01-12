from flask.views import  MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from temperature import Temperature
from calories import Calories

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform=calories_form)

    def post(self):
        caloriesform = CaloriesForm(request.form)
        weight = float(caloriesform.weight.data)
        height = float(caloriesform.height.data)
        age = int(caloriesform.age.data)

        country = caloriesform.country.data
        city = caloriesform.city.data

        temp = Temperature(country, city)
        cal = Calories(weight, height, age, temperature=temp.get())

        return render_template("calories_form_page.html",
                               caloriesform=caloriesform,
                               calories = cal.calculate(),
                               result = True)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default="50")
    height = StringField("Height: ", default="5.5")
    age = StringField("Age: ", default="30")
    country = StringField("Country: ", default="India")
    city = StringField("City: ", default="Benguluru")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run()