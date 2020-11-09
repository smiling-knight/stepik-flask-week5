from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length


class UserOrderData(FlaskForm):
    name = StringField("Имя", validators=[InputRequired(), Length(min=2, message="Имя не должно быть короче 2 символов")])
    address = StringField("Адрес", validators=[InputRequired()])
    email = StringField("Электропочта", validators=[InputRequired()])
    phone_number = StringField("Телефон", validators=[InputRequired()])
