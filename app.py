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

        desc = cursor.description
        column_names = [col[0] for col in desc]

        # TODO: improve this method, could work for every table like this....
        '''
        for index, row in enumerate(myresult):
            for i, col_name in enumerate(column_names):
                category = {str(col_name): str(row[i])}
                print(category)
                #print('colname: '+str(col_name)+' row: '+str(row[i]))
        '''
        categories = []
        for row in cursor.fetchall():
            category = {column_names[0]: row[0],
                        column_names[1]: str(row[1]),
                        column_names[2]: str(row[1]),
                        column_names[3]: str(row[3])}
            categories.append(category)
        cursor.close()

    return jsonify(categories)


@app.route('/categories/<string:category_id>', methods=['GET'])
def get_category_from_id(category_id):
    if request.method == "GET":

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM categories WHERE category_id = "+category_id)

        desc = cursor.description
        column_names = [col[0] for col in desc]

        myresult = cursor.fetchone()
        category = {column_names[0]: myresult[0],
                    column_names[1]: str(myresult[1]),
                    column_names[2]: str(myresult[1]),
                    column_names[3]: str(myresult[3])}

        cursor.close()

    return jsonify(category)


if __name__ == "__main__":
    app.run(debug=True)
