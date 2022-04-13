"""test Flask with this"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import random
from golf import *

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'THISISTHECLASSSECRET'

# Flask-Bootstrap requires this line
Bootstrap(app)

class GolfForm(FlaskForm):
    clubSpeed  = DecimalField('How hard did you hit the ball (speed in ft/s)?', validators=[DataRequired(),NumberRange(min=1,max=600)])
    launchAngle = DecimalField('How high did you hit the ball (angle from ground to sky)?', validators=[DataRequired(),NumberRange(min=0,max=90)])
    northAngle = DecimalField('Which direction did you hit the ball (angle from right to left)?', validators=[DataRequired(),NumberRange(min=0,max=180)])
    submit = SubmitField('Swing!')

@app.route('/', methods=['GET', 'POST'])
def index():
    speed = 5
    weather = {}
    weather['Wind Speed'] = speed
    weather['Wind Direction'] = 'NE'
    weather['Wind Vector'] = [speed*math.cos(np.radians(45)), speed*math.cos(np.radians(45))]
    form = GolfForm()
    message = ""
    image = ""
    initial="none"
    miss = ""
    landed = "none"
    if form.validate_on_submit():
    # call the function
        initial="auto"
        speed = float(form.clubSpeed.data)
        angle = float(form.launchAngle.data)
        direction = float(form.northAngle.data)
        new_spot=drive(speed,direction,angle,[0,0],weather)
        if(new_spot[0] > 500-1 and new_spot[0] < 500 + 1 and new_spot[1] > 500 - 1 and new_spot[1] < 500 + 1):
            message = "Hole in ONE!!!"
            image = "hole-in-one.gif"
            miss = ""
        else:
            message = "Try again!"
            image = "missed.gif"
            miss = new_spot
            landed = "auto"

    return render_template('index.html', form=form, message=message, image=image, miss=miss, initial=initial, landed=landed)

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('error.html', error=e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error=e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
