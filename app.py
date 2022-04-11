"""test Flask with this"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

class GolfForm(FlaskForm):
    clubSpeed  = DecimalField('What is your club speed (ft/s)?', validators=[DataRequired(),NumberRange(min=.01,max=600)])
    launchAngle = DecimalField('What is your launch angle (ground to sky)?', validators=[DataRequired(),NumberRange(min=0,max=89)])
    northAngle = DecimalField('What is your attack angle (left to right)?', validators=[DataRequired(),NumberRange(min=0,max=180)])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = GolfForm()
    message = ""
    if form.validate_on_submit():
    # call the function here holeInOne=golf(clubSpeed,launchAngle,northAngle)
    # if holeInOne:
    # message = "Hole in ONE!!!"
    # else:
        message = "Try again!"
    return render_template('index.html', form=form, message=message)
