import sqlite3


class ContexSqlManager:
    def __init__(self, name):
        self._name = name

    def __enter__(self):
        self._conn = sqlite3.connect(self._name)
        return self

    def my_execute(self, sql, *args):
        cursor = self._conn.cursor()
        cursor.execute(sql, args)
        self._conn.commit()
        return cursor.fetchall()

    def my_select(self, sql, *args):
        cursor = self._conn.cursor()
        cursor.execute(sql, args)
        return cursor.fetchall()

    def __exit__(self, *args):
        self._conn.commit()
        self._conn.close()


sql_all_cetegory = """
select id, category_name from category
"""

sql_select_current_category = """
select id, product_name
from product
where status_id != 3
  and category_id = ?"""

sql_select_product = """
select product_name,
       cost,
       quantity,
       s.name as status,
       c.category_name as category,
       c.id as category_id,
       description
from product
join category c on product.category_id = c.id
join status s on product.status_id = s.id
where product.id = ?
"""

sql_select_all_status = """
select id, name from status
"""

sql_inser_new_category = """
insert into category (category_name)
values (?)
"""

sql_inser_new_product = """
insert into product (product_name, status_id, cost, quantity, category_id, description)
values (?,?,?,?,?,?)
"""