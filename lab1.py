from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route('/lab1')
def lab():
        return """
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <div>
            Flask — фреймворк для создания веб-приложений на языке <br>
            программирования Python, использующий набор инструментов <br>
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так <br>
            называемых микрофреймворков — минималистичных каркасов <br>
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div>
        <a href='/menu'>меню</a>

        <h2>Релизованные роуты</h2>
        <a href="lab1/oak">lab1/oak - дуб</a> <br>
        <a href="lab1/student">lab1/student - студент</a> <br>
        <a href="lab1/python">lab1/python - python</a> <br>
        <a href="lab1/car">lab1/car - сar</a>

        <footer>
            &copy; Никита Кем, ФБИ-22, 3 курс, 2024
        </footer>
    </body>
</html>
"""


@lab1.route('/lab1/oak')
def oak():
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/student')
def student():
        return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Кем Никита Алексеевич</h1>
        <img src="''' + url_for('static', filename='nstu.jpg') + '''">
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div class="py">
            <h2>Для чего нужен Python?</h2>
            <img src="''' + url_for('static', filename='py.webp') + '''">
        </div>
        <div>
            Data Science и машинное обучение. Эти два направления IT тесно связаны друг с другом. Наука о данных заключается в обработке больших массивов информации из базы данных, а машинное обучение — в разработке компьютерных алгоритмов, способных учиться на ней и делать точные прогнозы. В Data Science используют Python для включения очистки и разметки данных, поиска и обработки статистической информации, ее визуализацию в виде диаграмм, графиков и т.д. С помощью библиотеки Python ML классифицируются изображения, тексты, поисковый трафик, осуществляется распознавание лиц и речи, глубинное машинное обучение.
        </div> <br>
        <div>
            Веб-разработка. Многие крупные интернет-компании, такие как Google, Facebook*, программируют на Python свои самые известные проекты, например, Instagram*, YouTube, Dropbox и т.д. Этот язык позволяет вести веб-разработку на стороне сервера, потому что его обширная библиотека включает множество решений как раз для реализации сложных серверных функций. За счет своей простоты использования Python широко применяется небольшими командами и одиночными разработчиками для создания сайтов, десктопных и мобильных веб-приложений.
        </div> <br>
            Разработка и тестирование ПО. Возможности Python используются тестировщиками и разработчиками для поиска и исправления ошибок, автоматической сборки, разработки прототипов программного обеспечения, управления проектами и т.д. Кроме того, с помощью сред модульного тестирования «Питона» осуществляется проверка функций. Также на этом языке создаются тестовые скрипты, имитирующие различные сценарии использования ПО. Разработчики аппаратных платформ (например, IBM, Hewlett-Packard, Intel) тоже используют Python для тестирования своей продукции.
        </div>
    </body>
</html>
'''


@lab1.route('/lab1/car')
def car():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body class="car">
        <img src="''' + url_for('static', filename='car.jpg') + '''">
        <div>
            <div class="car">
                BMW AG — немецкий производитель автомобилей, мотоциклов, двигателей, а также велосипедов. Более 45 % акций принадлежит семье Квандт. Председателем правления компании является Оливер Ципсе. Главный дизайнер — Йозеф Кабан. В списке крупнейших публичных компаний мира Forbes Global 2000 за 2022 год BMW Group заняла 64-е место, а в списке Fortune Global 500 — 59-е место
            </div> <br>
            <div class="car">
                По-русски название «BMW» произносится «бэ-эм-вэ́», что близко к немецкому произношению; изредка встречается написание «БМВ». Существует также несколько «неофициальных» названий: из англоязычного произношения аббревиатуры «би-эм-дабл-ю» для мотоциклов фирмы исторически сложилось название «бимер» (англ. beemer), для автомобилей — похожее, но не равнозначное «биммер» (англ. bimmer)
            </div> <br>
            <div class="car">
                В логотипе компании чёрное кольцо было заимствовано от логотипа завода авиационных моторов Раппа. Белые и голубые сектора указывают на флаг и герб Баварии, в свою очередь основанных на гербе рода Виттельсбахов, правивших Баварией с конца XII по начало XX века.
            </div>
        <div>
    </body>
</html>
'''