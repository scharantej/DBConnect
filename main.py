
from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect_db', methods=['POST'])
def connect_db():
    name = request.form['name']
    email = request.form['email']
    connection = mysql.connector.connect(host='localhost',
                                         database='flask_db',
                                         user='root',
                                         password='password')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
