import os
from datetime import timedelta
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.permanent_session_lifetime = timedelta(hours=2)

def get_db_connection():
    connection = sql.connect('db/database.db')
    connection.row_factory = sql.Row
    return connection

def add_post(title, content):
    if request.method == 'POST':
        connection = sql.connect('db/database.db')
    
        with open('db/schema.sql') as f:
            connection.executescript(f.read())
    
        cursor = connection.cursor()

        title = request.form['title']
        content = request.form['content']

        cursor.execute(f"INSERT INTO posts (title, content) VALUES (?, ?)", (f'{title}', f'{content}'))
        connection.commit()
        connection.close()



@app.route('/')
def home():  # put application's code here
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():  # put application's code here

    return render_template('about.html')

@app.route('/contact')
def contact():  # put application's code here
    return render_template("contact.html")

@app.route('/login')
def login():  # put application's code here
    return render_template("login.html")








@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            add_post(title, content)
            return redirect(url_for('home'))

    return render_template("create.html")






@app.route('/logout')
def logout():  # put application's code here
    pass


if __name__ == '__main__':
    app.run(host="localhost",port=3000, debug=True)
