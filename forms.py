from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class JobPerformanceScoreForm(FlaskFrom):
    username = StringField('Username', 
    validators=[DataRequired(), Length(min=2, max=20)]
    )

    email = StringField("Email", 
    validators=[DataRequired(), Email()]
    )

    password = PasswordField("Password", 
    validators=[DataRequired()]
    )

    confirm_password = PasswordField("Repeat Password", 
    validators=[DataRequired(), EqualTo('Password')]
    )

    submit = SubmitField("Submit")