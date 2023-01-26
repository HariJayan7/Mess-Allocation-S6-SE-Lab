import sqlite3
from flask import session
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# def get_post(post_id):
#     conn = get_db_connection()
#     post = conn.execute('SELECT * FROM posts WHERE id = ?',
#                         (post_id,)).fetchone()
#     conn.close()
#     if post is None:
#         abort(404)
#     return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# @app.route('/')
# def index():
#     conn = get_db_connection()
#     posts = conn.execute('SELECT * FROM posts').fetchall()
#     conn.close()
#     return render_template('index.html', posts=posts)
@app.route('/', methods=('GET', 'POST'))
def home_page():
    return render_template('home_page.html')


@app.route('/login_wardens', methods=('GET', 'POST'))
def login_wardens():
    return render_template('login_wardens.html')

# this is for password change for managers and wardens distinguished
# by their username which is passed as an arg from their respective dashboards


@app.route('/<username>/sign_up', methods=('GET', 'POST'))
def sign_up(username):
    if request.method == 'POST':
        username_entered = request.form['username']
        password_entered = request.form['password']
        repeat_password_entered = request.form['repeat_password']
        if repeat_password_entered == password_entered and username == username_entered:
            conn = get_db_connection()
            try_manager = conn.execute(
                'SELECT * FROM Mess_Login_Creds WHERE Username = ?', (username,)).fetchone()
            try_warden = conn.execute(
                'SELECT * FROM Warden_Login_Creds WHERE Username = ?', (username,)).fetchone()
            conn.close()
            if try_manager:
                conn = get_db_connection()
                conn.execute('UPDATE Mess_Login_Creds SET Passcode = ?'
                             ' WHERE Username = ?',
                             (password_entered, username))
                conn.commit()
                conn.close()
                flash('Password Changed Successfully')
                return redirect(url_for('login_managers'))

            elif try_warden:
                conn = get_db_connection()
                conn.execute('UPDATE Warden_Login_Creds SET Passcode = ?'
                             ' WHERE Username = ?',
                             (password_entered, username))
                conn.commit()
                conn.close()
                flash('Password Changed Successfully')
                return redirect(url_for('login_wardens'))
            else:
                flash('Entered Wrong Username')
                return redirect(url_for('sign_up', username=username))
        elif username == username_entered:
            flash('Passwords entered were not the same...Failed to change password')
            return redirect(url_for('sign_up', username=username))
        else:
            flash('Username entered was incorrect...Failed to change password')
            return redirect(url_for('sign_up', username=username))
    return render_template('sign_up.html', username=username)


@app.route('/login_managers', methods=('GET', 'POST'))
def login_managers():
    if request.method == 'POST':
        username = request.form['Username']
        password_entered = request.form['Password']
        conn = get_db_connection()
        passcode = conn.execute(
            'SELECT Passcode FROM Mess_Login_Creds WHERE Username=?', (username,)).fetchone()
        conn.close()
        if passcode[0] == password_entered:
            conn = get_db_connection()
            details = conn.execute(
                'SELECT * FROM Mess_Manager WHERE Manager_Id=?', (username,)).fetchone()
            conn.close()
            return redirect(url_for('mess_manager_dashboard', username=username))
        else:
            flash('Wrong Password')
            return redirect(url_for('login_managers'))

    return render_template('login_managers.html')


@app.route('/<username>/mess_manager_dashboard', methods=('GET', 'POST'))
def mess_manager_dashboard(username):
    conn = get_db_connection()
    details = conn.execute(
        'SELECT * FROM Mess_Manager WHERE Manager_Id=?', (username,)).fetchone()
    mess_id = details[2]
    students = conn.execute(
        'SELECT * FROM Student WHERE Mess_Id=?', (mess_id,)).fetchall()
    mess_details = conn.execute(
        'SELECT * FROM Mess_Details WHERE Mess_Id=?', (mess_id,)).fetchone()

    conn.close()

    return render_template('mess_manager_dashboard.html', details=details, students=students, mess_details=mess_details)


@app.route('/student_login', methods=('GET', 'POST'))
def student_login():
    return render_template('student_login.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
