from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'expenses_test'

mysql = MySQL(app)


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


@app.route('/categories', methods=['GET'])
def get_categories():
    if request.method == "GET":

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM categories")
        myresult = cursor.fetchall()
        cursor.close()

        return jsonify(myresult)


@app.route('/categories/<string:category_id>', methods=['GET'])
def get_category_from_id(category_id):
    if request.method == "GET":

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM categories WHERE category_id = "+category_id)
        myresult = cursor.fetchone()

        cursor.close()

        return jsonify(myresult)


if __name__ == '__main__':
    app.run()
