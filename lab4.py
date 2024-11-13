from flask import Blueprint, render_template, request, redirect
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('/lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
      return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods=['POST'])
def div():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
      if x2 == '0':
            return render_template('lab4/div.html', error='На ноль делить нельзя!')
      x1 = int(x1)
      x2 = int(x2)
      result = x1 / x2
      return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/summa-form')
def summa_form():
      return render_template('lab4/summa-form.html')


@lab4.route('/lab4/summa', methods=['POST'])
def summa():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '' :
            x1 = 0
      if x2 == '':
            x2 = 0
      x1 = int(x1)
      x2 = int(x2)
      result = x1 + x2
      return render_template('lab4/summa.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/multiplication-form')
def multiplication_form():
      return render_template('lab4/multiplication-form.html')


@lab4.route('/lab4/multiplication', methods=['POST'])
def multiplication():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '':
           x1 = 1
      if x2 == '':
           x2 = 1 
      x1 = int(x1)
      x2 = int(x2)
      result = x1 * x2
      return render_template('lab4/multiplication.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/subtraction-form')
def subtraction_form():
      return render_template('lab4/subtraction-form.html')


@lab4.route('/lab4/subtraction', methods=['POST'])
def subtraction():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '' or x2 == '':
        return render_template('lab4/subtraction.html', error='Оба поля должны быть заполнены!')
      x1 = int(x1)
      x2 = int(x2)
      result = x1 - x2
      return render_template('lab4/subtraction.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/exponentiation-form')
def exponentiation_form():
      return render_template('lab4/exponentiation-form.html')


@lab4.route('/lab4/exponentiation', methods=['POST'])
def exponentiation():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '' or x2 == '':
        return render_template('lab4/exponentiation.html', error='Оба поля должны быть заполнены!')
      if x1 == '0' and x2 == '0':
        return render_template('lab4/exponentiation.html', error='Поля не должны быть равны нулю!')
      x1 = int(x1)
      x2 = int(x2)
      result = x1 ** x2
      return render_template('lab4/exponentiation.html', x1=x1, x2=x2, result=result)


tree_count = 0
max_trees = 10
@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
      global tree_count
      if request.method == 'GET':
           return render_template('lab4/tree.html', tree_count=tree_count, max_trees=max_trees)
      operation = request.form.get('operation')
      
      if operation == 'cut':
           tree_count -= 1
      elif operation == 'plant':
           if tree_count < max_trees:
                tree_count += 1
      return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123'}, 
    {'login': 'bob', 'password': '555'},
    {'login': 'nikita', 'password': '111'},
    {'login': 'sergey', 'password': '222'},
]  

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab4/login.html', authorized = False)
    login = request.form.get('login')
    password = request.form.get('password')
    for user in users:
         if login == user['login'] and password == user['password']:
              return render_template('/lab4/login.html', login=login, authorized=True)
    
    error = 'Неверные логин и/или пароль' 
    return render_template('lab4/login.html', error=error, authorized = False)