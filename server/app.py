from flask import Flask, jsonify, request
import json
import pyodbc
import pandas.io.sql as pdsql
from makeDB import create_table

app = Flask(__name__)

@app.route('/api/products/add', methods=['POST'])
def products_add():
    if request.method == 'POST':
        eq = request.get_json()
        
        sql_query = "INSERT INTO products(className, name, price) VALUES(?, ?, ?)"
        values = (eq['className'], eq['name'], eq['price'])
        print(values)
        result = execute_query_sql(sql_query, values)
        
        sql_query = "SELECT id FROM products ORDER BY id DESC limit 1"
        result = read_query_sql(sql_query)
        eq['id'] = result['id']

        return jsonify(eq)

@app.route('/api/products/list', methods=['GET'])
def products_list():
    if request.method == 'GET':
        class_name = request.args.get('className')
        sql_query = "SELECT id, name, price FROM products WHERE className = {}".format(class_name)
        result = read_query_sql(sql_query, return_list=True)
        
        return jsonify({'data':result})

@app.route('/api/products/delete', methods=['POST'])
def products_delete():
    if request.method == 'POST':
        eq = request.get_json()
        sql_query = "DELETE FROM products WHERE id = ?"
        values = (eq['id'])

        execute_query_sql(sql_query,values)

        success = {"success": True}
        return jsonify(success)

@app.route('/api/order/add', methods=['POST'])
def order_add():
    if request.method == 'POST':
        eq = request.get_json()
        sql_query = "INSERT INTO orders (className, productID, amount) VALUES(?, ?, ?)"
        Values = (eq['className'], eq['productID'], eq['amount'])
        execute_query_sql(sql_query,Values)
        
        
        sql_query = 'SELECT * FROM orders ORDER BY id DESC limit 1'
        result = read_query_sql(sql_query)
        return jsonify(result)    

@app.route('/api/order/delete', methods=['POST'])
def order_delete():
    if request.method == 'POST':
        eq = request.get_json()
        sql_query = "DELETE FROM orders WHERE id = ?"
        values = (eq['id'])
        execute_query_sql(sql_query, values)

        success = {"success": True}
   
        return jsonify(success)

@app.route('/api/order/total', methods=['GET'])
def order_total():
     if request.method == 'GET':
        class_name = request.args.get('className')
        
        sql_query = "SELECT SUM(price * amount) AS total FROM orders LEFT JOIN products ON orders.productID = products.id WHERE orders.className = {0}".format(class_name)
        result = read_query_sql(sql_query)
        
        return jsonify(result)

def execute_query_sql(sql_query,values=()):
    con = pyodbc.connect(r'DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=salesioFes.db;Trusted_connection=yes')
    cur = con.cursor()
    cur.execute(sql_query,values)
    con.commit()
    con.close()

def read_query_sql(sql_query, return_list=False):
    con = pyodbc.connect(r'DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=salesioFes.db;Trusted_connection=yes')
    df = pdsql.read_sql(sql_query, con)
    con.close()
    
    data = df.to_dict('records')
    if return_list:
        return data
    if len(data) > 0:
        d = data[0]
        for k in d.keys():
            if not d[k] is str:
                d[k] = str(d[k])

        return d
    else:
        return "no data"

if __name__ == "__main__":
    create_table()
    app.run(debug=True)