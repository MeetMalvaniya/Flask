from flask_wtf import Form
from wtforms import IntegerField,TextAreaField,SubmitField,RadioField,SelectField,StringField
from wtforms import validators,ValidationError



class contactform(Form):
    name=StringField("Name of Student",[validators.DataRequired("Pls Enter Your Name")])
    gender=RadioField("Gender",choices=[("M","Male"),["F","Female"]])
    address=TextAreaField("Address")
    email=StringField("EMAIL",[validators.input_required("Pls enter email"),validators.Email("Pls enter your email")])
    age=IntegerField("Age")
    language=SelectField("Language",choices=[("cpp","c++"),("py","python")])
    submit=SubmitField("send")