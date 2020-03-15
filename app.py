from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql.matteobaldassin.com'
app.config['MYSQL_USER'] = 'matteoba94047'
app.config['MYSQL_PASSWORD'] = 'matteo00'
app.config['MYSQL_DB'] = 'matteoba94047'

mysql = MySQL(app)


'''
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
'''


if __name__ == '__main__':
    app.run()
