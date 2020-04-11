
from flask import Flask
from flask import render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/API/*": {"origins": "*"}})


app.config['CORS_HEADERS'] = 'Content-Type'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'matteo00'
app.config['MYSQL_DB'] = 'expenses_tracker'

mysql = MySQL(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


'''
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        category_name = details['category_name']
        category_description = details['category_description']
        category_color = details['category_color']
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO categories(name, description,color) VALUES (%s, %s,%s)", (category_name, category_description, category_color))
        mysql.connection.commit()
        cursor.close()
        return 'success'
    return render_template('index.html')
'''


@app.route('/API/categories', methods=['GET', 'POST'])
@cross_origin()
def get_categories():
    result = []
    if request.method == "GET":

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM categories")

        response = cursor.fetchall()
        desc = cursor.description
        column_names = [col[0] for col in desc]

        for num, row in enumerate(response):
            result.append(dict(zip(column_names, row)))

        cursor.close()
    elif request.method == "POST":
        post_data = request.get_json()

        name = post_data['name']
        description = post_data['description']
        color = post_data['color']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO categories(name, description,color) VALUES (%s, %s,%s)", (name, description, color))
        mysql.connection.commit()

        result.append(
            {"name": name, "description": description, "color": color})

        cursor.close()

    return jsonify(result)


@app.route('/API/expenses', methods=['GET'])
def get_expenses():
    if request.method == "GET":
        result = []

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM expenses")

        response = cursor.fetchall()
        desc = cursor.description
        column_names = [col[0] for col in desc]

        for num, row in enumerate(response):
            result.append(dict(zip(column_names, row)))

        cursor.close()

    return jsonify(result)


@app.route('/API/categories/<string:category_id>', methods=['GET'])
def get_category_from_id(category_id):
    if request.method == "GET":

        result = {}

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM categories WHERE category_id = "+category_id)

        response = cursor.fetchone()
        desc = cursor.description
        column_names = [col[0] for col in desc]

        if response is not None:
            result = dict(zip(column_names, response))

        cursor.close()

    return jsonify(result)


@app.route('/API/expenses/<string:expense_id>', methods=['GET'])
def get_expense_from_id(expense_id):
    if request.method == "GET":
        result = {}

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM expenses WHERE expense_id = "+expense_id)

        response = cursor.fetchone()
        desc = cursor.description
        column_names = [col[0] for col in desc]

        if response is not None:
            result = dict(zip(column_names, response))

        cursor.close()

    return jsonify(result)


if __name__ == "__main__":
    app.debug = True
    app.run()
