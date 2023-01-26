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


@app.route('/', methods=('GET', 'POST'))
def student_dashboard():
    if request.method == 'GET':
        conn = get_db_connection()
        student = conn.execute('SELECT * FROM Student').fetchone()
        conn.close()
        return render_template('student_dashboard.html', student=student)
    elif request.method == 'POST':
        if request.form['submit_button'] == 'Get Seat in Mess A':
            conn = get_db_connection()
            allocated = conn.execute(
                'SELECT Allocated FROM Mess_Details WHERE Mess_Id=1').fetchone()
            allocated = int(allocated[0])+1
            conn.execute('UPDATE Mess_Details SET Allocated = ?'
                         ' WHERE Mess_Id = ?',
                         (allocated, 1))
            conn.commit()
            conn.close()

            conn = get_db_connection()
            student = conn.execute(
                'SELECT * FROM Student').fetchone()
            student_rno = student[1]
            conn.execute('UPDATE Student SET Mess_Id = ?,Ref_Id = ?'
                         ' WHERE Roll_No = ?',
                         (1, "allocated 1", str(student_rno)))
            conn.commit()
            conn.close()
            flash('Mess A was successfully alloted!')
            return redirect(url_for('student_dashboard', student=student))
        elif request.form['submit_button'] == 'Get Seat in Mess B':
            conn = get_db_connection()
            student_rno = conn.execute(
                'SELECT Roll_No FROM Student').fetchone()
            allocated = conn.execute(
                'SELECT Allocated FROM Mess_Details WHERE Mess_Id=2').fetchone()
            allocated = int(allocated[0])+1
            conn.execute('UPDATE Mess_Details SET Allocated = ?'
                         ' WHERE Mess_Id = ?',
                         (allocated, 2))
            # conn.execute('UPDATE Student SET Mess_Id = ?, Ref_Id = ?'
            #              ' WHERE Roll_No = ?',
            #              (2, "should become random soon", student_rno))
            conn.commit()
            conn.close()
            conn = get_db_connection()
            student = conn.execute(
                'SELECT * FROM Student').fetchone()
            student_rno = student[1]
            conn.execute('UPDATE Student SET Mess_Id = ?,Ref_Id = ?'
                         ' WHERE Roll_No = ?',
                         (2, "allocated 2", str(student_rno)))
            conn.commit()
            conn.close()
            flash('Mess B was successfully alloted!')
            return redirect(url_for('student_dashboard', student=student))
        elif request.form['submit_button'] == 'Get Seat in Mess C':
            conn = get_db_connection()
            student_rno = conn.execute(
                'SELECT Roll_No FROM Student').fetchone()
            allocated = conn.execute(
                'SELECT Allocated FROM Mess_Details WHERE Mess_Id=3').fetchone()
            allocated = int(allocated[0])+1
            conn.execute('UPDATE Mess_Details SET Allocated = ?'
                         ' WHERE Mess_Id = ?',
                         (allocated, 3))
            # conn.execute('UPDATE Student SET Mess_Id = ?, Ref_Id = ?'
            #              ' WHERE Roll_No = ?',
            #              (3, "should become random soon", student_rno))
            conn.commit()
            conn.close()
            conn = get_db_connection()
            student = conn.execute(
                'SELECT * FROM Student').fetchone()
            student_rno = student[1]
            conn.execute('UPDATE Student SET Mess_Id = ?,Ref_Id = ?'
                         ' WHERE Roll_No = ?',
                         (3, "allocated 3", str(student_rno)))
            conn.commit()
            conn.close()
            flash('Mess C was successfully alloted!')
            return redirect(url_for('student_dashboard', student=student))
        elif request.form['submit_button'] == 'Get Seat in Mess D':
            conn = get_db_connection()
            student_rno = conn.execute(
                'SELECT Roll_No FROM Student').fetchone()
            allocated = conn.execute(
                'SELECT Allocated FROM Mess_Details WHERE Mess_Id=4').fetchone()
            allocated = int(allocated[0])+1
            conn.execute('UPDATE Mess_Details SET Allocated = ?'
                         ' WHERE Mess_Id = ?',
                         (allocated, 4))
            # conn.execute('UPDATE Student SET Mess_Id = ?, Ref_Id = ?'
            #              ' WHERE Roll_No = ?',
            #              (4, "should become random soon", student_rno))
            conn.commit()
            conn.close()
            conn = get_db_connection()
            student = conn.execute(
                'SELECT * FROM Student').fetchone()
            student_rno = student[1]
            conn.execute('UPDATE Student SET Mess_Id = ?,Ref_Id = ?'
                         ' WHERE Roll_No = ?',
                         (4, "allocated 4", str(student_rno)))
            conn.commit()
            conn.close()
            flash('Mess D was successfully alloted!')
            return redirect(url_for('student_dashboard', student=student))
        elif request.form['submit_button'] == 'Get Seat in Mess E':
            conn = get_db_connection()
            student_rno = conn.execute(
                'SELECT Roll_No FROM Student').fetchone()
            allocated = conn.execute(
                'SELECT Allocated FROM Mess_Details WHERE Mess_Id=5').fetchone()
            allocated = int(allocated[0])+1
            conn.execute('UPDATE Mess_Details SET Allocated = ?'
                         ' WHERE Mess_Id = ?',
                         (allocated, 5))
            # conn.execute('UPDATE Student SET Mess_Id = ?, Ref_Id = ?'
            #              ' WHERE Roll_No = ?',
            #              (5, "should become random soon", student_rno))
            conn.commit()
            conn.close()
            conn = get_db_connection()
            student = conn.execute(
                'SELECT * FROM Student').fetchone()
            student_rno = student[1]
            conn.execute('UPDATE Student SET Mess_Id = ?,Ref_Id = ?'
                         ' WHERE Roll_No = ?',
                         (5, "allocated 5", str(student_rno)))
            conn.commit()
            conn.close()
            flash('Mess E was successfully alloted!')
            return redirect(url_for('student_dashboard', student=student))
        return render_template('student_dashboard.html', student=student)


@app.route('/mess_allocation_homepage', methods=('GET', 'POST'))
def mess_allocation_homepage():
    if request.method == 'GET':
        conn = get_db_connection()
        mess = conn.execute('SELECT * FROM Mess_Details').fetchall()
        conn.close()
        return render_template('mess_allocation_homepage.html', mess=mess)
    elif request.method == 'POST':
        conn = get_db_connection()
        mess = conn.execute('SELECT * FROM Mess_Details').fetchall()
        conn.close()
        return render_template('mess_allocation_homepage.html', mess=mess)
# @app.route('/<int:post_id>')
# def post(post_id):
#     post = get_post(post_id)
#     return render_template('post.html', post=post)


# @app.route('/create', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#         author = request.form['author']

#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO posts (title, content,author) VALUES (?, ?, ?)',
#                          (title, content, author))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#     return render_template('create.html')


# @app.route('/<int:id>/edit', methods=('GET', 'POST'))
# def edit(id):
#     post = get_post(id)

#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#         author = request.form['author']

#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('UPDATE posts SET title = ?, content = ?,author = ?'
#                          ' WHERE id = ?',
#                          (title, content, author, id))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))

#     return render_template('edit.html', post=post)


# @app.route('/<int:id>/delete', methods=('POST',))
# def delete(id):
#     post = get_post(id)
#     conn = get_db_connection()
#     conn.execute('DELETE FROM posts WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     flash('"{}" was successfully deleted!'.format(post['title']))
#     # session['_flashes'].clear()
#     return redirect(url_for('index'))


# @app.route('/#')
# def about():
#     return render_template('about.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
