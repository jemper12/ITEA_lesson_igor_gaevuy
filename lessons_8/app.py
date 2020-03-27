from flask import Flask, render_template, request, redirect, url_for
from db import ContexSqlManager, sql_all_cetegory, sql_select_current_category, sql_select_product, \
    sql_select_all_status, sql_inser_new_category, sql_inser_new_product

app = Flask(__name__)

"""
MVC
"""
""""
Создать базу данных товаров, у товара есть:
    Категория (связанная таблица),
    название, есть ли товар в продаже или на складе, цена, кол-во единиц.Создать html страницу. 
На первой странице выводить ссылки на все категории,
    при переходе на категорию получать список всех товаров в наличии ссылками, при клике на товар выводить его цену, 
    полное описание и кол-во единиц в наличии.
"""

DB = 'database.sqlite'


@app.route('/')
def index():
    with ContexSqlManager(DB) as db:
        exec_ = db.my_select(sql_all_cetegory)
        data = {}
        for to_data in exec_:
            data[to_data[0]] = to_data[1]

    return render_template('index.html', data=data)


@app.route('/category/<category_id>')
def category(category_id):
    with ContexSqlManager(DB) as db:
        exec_ = db.my_select(sql_select_current_category, category_id)
        data = {}
        for to_data in exec_:
            data[to_data[0]] = to_data[1]

    return render_template('category.html', data=data)


@app.route('/product/<product_id>')
def product(product_id):
    with ContexSqlManager(DB) as db:
        exec_ = db.my_select(sql_select_product, product_id)[0]
        name = exec_[0]
        cost = exec_[1]
        quantity = exec_[2]
        status = exec_[3]
        category_name = exec_[4]
        category_id = exec_[5]
        description = exec_[6]
    return render_template('product.html', name=name, cost=cost, quantity=quantity, status=status,
                           category_name=category_name, category_id=category_id, description=description)


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        category_dict = {}
        status_dict = {}

        with ContexSqlManager(DB) as db:

            category_list = db.my_select(sql_all_cetegory)
            for data in category_list:
                category_dict[data[0]] = data[1]

            status_list = db.my_select(sql_select_all_status)
            for data in status_list:
                status_dict[data[0]] = data[1]

        return render_template('admin.html', status_dict=status_dict, category_dict=category_dict)

    elif request.method == 'POST':
        if 'category_name' in request.form:
            if request.form['category_name'] != '':
                with ContexSqlManager(DB) as db:
                    db.my_execute(sql_inser_new_category, request.form['category_name'])
        else:
            if request.form['product_name'] != '' and request.form['cost'] != '' and \
                    request.form['quantity'] != '' and request.form['description'] != '':
                with ContexSqlManager(DB) as db:
                    # product_name, status_id, cost, quantity, category_id, description
                    db.my_execute(sql_inser_new_product, request.form['product_name'], request.form['status'],
                                  request.form['cost'], request.form['quantity'], request.form['category'],
                                  request.form['description'])
        return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)
