from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'nikita_kem_orm'
    db_user = 'nikita_kem_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "nikita_kem_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)


@app.route('/')


@app.route('/index')
def start():
      return redirect("/menu", code=302)


@app.route('/menu')
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, WEB-программирование, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        
        <div>
            <a href='/lab1'>Лабораторная работа 1</a>
        </div>

        <div>
            <a href='/lab2'>Лабораторная работа 2</a>
        </div>

        <div>
            <a href='/lab3'>Лабораторная работа 3</a>
        </div>

        <div>
            <a href='/lab4'>Лабораторная работа 4</a>
        </div>
        
        <div>
            <a href='/lab5'>Лабораторная работа 5</a>
        </div>
        <div>
            <a href='/lab6'>Лабораторная работа 6</a>
        </div>
        <div>
            <a href='/lab7'>Лабораторная работа 7</a>
        </div>
        <div>
            <a href='/lab8'>Лабораторная работа 8</a>
        </div>
        <div>
            <a href='/lab9'>Лабораторная работа 9</a>
        </div>

        <footer>
            &copy; Никита Кем, ФБИ-22, 3 курс, 2024
        </footer>
    </body>
</html>
"""