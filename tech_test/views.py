from werkzeug.utils import redirect
from .models import Pay
from flask import Blueprint, render_template, request, flash
from . import db

# unnecessary to use Blueprint for the scope of this project
views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        # retrieve posted form entries eg hours and wage in string
        hours = request.form.get("hours")
        wage = request.form.get("wage")
        # create complementary string
        total_text = str("Your total pay will be: £")
        
        # conditional statements to make sure a value has to always be entered coupled with flash messages
        if hours and wage == "0":
            flash("Please enter a number above 0...", category="error")
        

        elif hours == "0" and wage == str():
            flash("Please enter a number above 0 and enter your hourly wage", category="error")
        elif hours == str() and wage == "0":
            flash("Please enter a number above 0 and enter your hours worked", category="error")

        elif hours and wage:
            # converting inputs string eg hours, float and sum (hours * wage) into float type
            hours_float = float(hours)
            wage_float = float(wage)
            sum = float(hours_float * wage_float)

            # the result is represented with a f string, allowing to directly input variables of different types together
            result = f'{total_text}{sum:.2f} when you\'re working {hours_float:.2f} hours and earning £{wage_float:.2f}ph'
            
            # defined the pay data and added to the db
            # pay_total = Pay(pay=result)
            # db.session.add(pay_total)
            # db.session.commit()
            
            flash("Thank you for using Pay Calculator... Your results are below", category="success")
            return render_template("index.html", result=result)

        # else if hours/wage value is a string then...    
        elif hours or wage == str():
            flash("Please enter your hours worked and hourly wage...", category="error")
        
    return render_template("index.html")