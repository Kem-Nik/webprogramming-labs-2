from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/a')
def a():
      return "без слэша"


@lab2.route('/lab2/a/')
def a2():
      return "со слэшем"


flower_list = ['роза','тюльпан', 'незабудка','ромашка']
@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
      if flower_id >= len(flower_list):
            return 'нет такого цветка', 404
      else:
            return "цветок:" + flower_list[flower_id]


@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
      flower_list.append(name)
      return f'''
<!doctype html>
<html>
    <body>
        <h1>Добавлен новый цветок</h1>
        <p> название нового цветка: { name }</p>
        <p> всего цветов: { len(flower_list) }</p>
        <p> полный список: { flower_list }</p>
    </body>
</html>
'''


@lab2.route('/lab2/add_flower/')
def no_name():
    return 'Вы не задали имя цветка', 400


@lab2.route('/lab2/flowers')
def all_flowers():
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1>Все цветы</h1>
            <p>Всего цветов: {len(flower_list)}</p>
            <ul>
                {''.join(f'<li>{flower}</li>' for flower in flower_list)}
            </ul>
            <p><a href="{url_for('clear_flowers')}">Очистить список цветов</a></p>
        </body>
    </html>
    '''


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('all_flowers'))


@lab2.route('/lab2/example')
def example():
    name,lab,course,group = 'Никита Алексеевич Кем', 2, '3 курс','ФБИ-22' 
    fruits = [
            {'name':'яблоки' , 'price': 100},
            {'name':'груши' , 'price': 120},
            {'name':'апельсины' , 'price': 80},
            {'name':'мандарины' , 'price': 95},
            {'name':'манго' , 'price': 321}
    ]
    return render_template('example.html', name=name, lab=lab, course=course, group = group, fruits = fruits)
  

@lab2.route('/lab2/')
def lab():
      return render_template('lab2.html')


@lab2.route('/lab2/filter')
def filter():
      phrase = "О <b> сколько </b> <u>нам</u> <i>открытий</i> чудных..."
      return render_template('filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
      delenie = "Делить на ноль нельзя" if b == 0 else a / b
      return f'''
    <!doctype html>
    <html>
        <body>
        <h1> Расчет с параметрами: </h1>
        <p>{a} + {b} = {a+b}</p>
        <p>{a} - {b} = {a-b}</p>
        <p>{a} * {b} = {a*b}</p>
        <p>{a} / {b} = {delenie}</p>
        <p>{a} <sup>{b}</sup> = {a**b}</p>
        </body>
    </html>
'''


@lab2.route('/lab2/calc/')
def calc_one():
    return redirect(url_for('calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def calc_two(a):
    return redirect(url_for('calc', a=a, b=1))


book_list = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Антиутопия", "pages": 328},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1225},
    {"author": "Гарпер Ли", "title": "Убить пересмешника", "genre": "Роман", "pages": 281},
    {"author": "Федор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
    {"author": "Дж. Р. Р. Толкин", "title": "Властелин колец", "genre": "Фэнтези", "pages": 1216},
    {"author": "Рей Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Фантастика", "pages": 194},
    {"author": "Антуан де Сент-Экзюпери", "title": "Маленький принц", "genre": "Сказка", "pages": 96},
    {"author": "Дэниел Киз", "title": "Цветы для Элджернона", "genre": "Фантастика", "pages": 311},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Роман", "pages": 504},
    {"author": "Александр Пушкин", "title": "Евгений Онегин", "genre": "Поэма", "pages": 384}
]
@lab2.route('/lab2/books')
def show_books():
    return render_template('books.html', books=book_list)


bmws = [
      {'name': 'BMW M2', 'img': 'm2.webp' },
      {'name': 'BMW M3', 'img': 'm3.webp' },
      {'name': 'BMW M4', 'img': 'm4.webp' },
      {'name': 'BMW M5', 'img': 'm5.jpg' },
      {'name': 'BMW M8', 'img': 'm8.webp' }
]
@lab2.route('/lab2/bmw')
def bmw():
      return render_template('bmws.html', bmws=bmws)
