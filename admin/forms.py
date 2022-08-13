from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,DateTimeField,SubmitField

class ProductForm(FlaskForm):
    name=StringField('name')
    price=StringField('price')
    date=DateTimeField('date')
    submit=SubmitField('Add data')