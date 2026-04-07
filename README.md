# 🎬 Online Movie Ticket Booking System

A simple web-based application to book movie tickets online. This project is developed using **Python (Flask)**, **MySQL**, and **HTML/CSS** as part of a college project.

---

## 📌 Features

* User Registration & Login
* View Available Movies
* Book Movie Tickets
* Simple and User-Friendly Interface

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Database:** MySQL

---

## 📂 Project Structure

```
movie_booking/
│
├── app.py
├── db.py
├── templates/
│     ├── login.html
│     ├── register.html
│     ├── home.html
│     ├── movies.html
│     ├── booking.html
│
└── static/
      └── style.css
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/movie-booking.git
cd movie_booking
```

### 2. Install Dependencies

```
pip install flask mysql-connector-python
```

### 3. Setup Database

Open MySQL and run:

```
CREATE DATABASE movie_db;

USE movie_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    time VARCHAR(20),
    date VARCHAR(20)
);

CREATE TABLE booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    movie_id INT,
    seats INT
);
```

---

## ▶️ Run the Application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📸 Screens

* Login Page
* Register Page
* Movie List
* Booking Page

---

## 🚀 Future Improvements

* Add Admin Panel
* Seat Selection UI
* Online Payment Integration
* Booking History

---

## ⚠️ Limitations

* No payment gateway
* Basic UI design
* Limited security features

---

## 👩‍💻 Authors

* Vaishnavi Kauthale
* Vaishnavi Korke

---

## 📚 References

* https://www.w3schools.com/
* https://www.bookmyshow.com/

---

## 🙏 Acknowledgement

Thanks to our project guide and college for their support and guidance throughout the project.

---

## 📃 License

This project is for educational purposes only.
