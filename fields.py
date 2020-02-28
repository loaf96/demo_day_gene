from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TestField(FlaskForm):
    testfield = StringField('TestField', validators=[DataRequired(), Length(min=1)])

    submit = SubmitField('Test')