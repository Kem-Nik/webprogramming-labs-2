from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)


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

        <footer>
            &copy; Никита Кем, ФБИ-22, 3 курс, 2024
        </footer>
    </body>
</html>
"""