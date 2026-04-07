from flask import Flask, render_template, request, redirect
from db import get_db

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html')


# Register
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",
                       (name,email,password))
        db.commit()

        return redirect('/login')

    return render_template('register.html')


# Login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s",
                       (email,password))
        user = cursor.fetchone()

        if user:
            return redirect('/movies')
        else:
            return "Invalid Login"

    return render_template('login.html')


    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM movies")
    data = cursor.fetchall()

    return render_template('movies.html', movies=data)


# Booking
@app.route('/book/<int:id>', methods=['GET','POST'])

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO booking (user_id,movie_id,seats) VALUES (1,%s,%s)",
                       (id,seats))
        db.commit()

        return "Ticket Booked Successfully"

    return render_template('booking.html', movie_id=id)


if __name__ == '__main__':
    app.run(debug=True)def book(id):
    if request.method == 'POST':
        seats = request.form['seats']
# Show Movies
@app.route('/movies')
def movies():

