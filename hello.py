# -*- coding:utf-8 -*-

# import area
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# class area
class NameForm(FlaskForm):
    name = StringField('What\'s your name?', validators=[DataRequired()])
    submit = SubmitField('submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    print(form.name)
    print(form.submit)
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        redirect(redirect(url_for('index')))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))


# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)


# main area
if __name__ == '__main__':
    manager.run()
