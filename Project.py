from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators

app = Flask(__name__)




@app.route('/Split1')
def Split1():

    return render_template('Split1.html')

@app.route('/Equal')
def Equal():
    return render_template('Equal.html')

@app.route('/Basedonrecipient')
def Basedonrecipient():
    return render_template('Basedonrecipient.html')

@app.route('/Customize')
def Customize():
    return render_template('Customize.html')

@app.route('/R_Equal')
def R_Equal():
    return render_template('R_Equal.html')

@app.route('/R_Basedonrecipient')
def R_Basedonrecipient():
    return render_template('R_Basedonrecipient.html')

@app.route('/R_Customize')
def R_Customize():
    return render_template('R_Customize.html')
@app.route('/head')
def head():
    return render_template('head.html')


if __name__ == '__main__':
    app.run()
