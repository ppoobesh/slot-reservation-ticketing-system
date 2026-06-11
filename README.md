# 🚀 Internship Registration Management System

A web-based Internship Registration Management System built using Flask and MySQL. The application allows students to register for internship programs, stores their information securely in a database, and provides an interface to view all registered candidates.

## 📌 Features

* Internship registration form
* Student information management
* MySQL database integration
* Form validation
* Duplicate email prevention
* Welcome page after successful registration
* View all registered students/interns
* Responsive and user-friendly interface

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask
* MySQL Connector

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Database

* MySQL

---

## 📂 Project Structure

```text
Internship-Registration-System/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── welcome.html
│   ├── students.html
│   └── email.html
│
├── requirements.txt
├── internship_db.sql
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/internship-registration-system.git
cd internship-registration-system
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/macOS

```bash
source .venv/bin/activate
```

### 4. Install Required Packages

```bash
pip install flask mysql-connector-python
```

or

```bash
pip install -r requirements.txt
```

### 5. Create MySQL Database

```sql
CREATE DATABASE internship_db;
```

### 6. Create Students Table

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    college VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    year_of_study VARCHAR(20) NOT NULL,
    internship_domain VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 7. Configure Database Connection

Update the database credentials in `app.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'internship_db'
}
```

### 8. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://localhost:5000
```

---

## 📋 Application Workflow

1. User opens the registration page.
2. User enters internship registration details.
3. Form data is validated.
4. Information is stored in the MySQL database.
5. A welcome page displays the submitted details.
6. Administrators can view all registered students through the students page.

---

## 🎯 Key Functionalities

### Registration Module

* Collects student details
* Validates user input
* Prevents duplicate registrations

### Database Management

* Stores internship registration records
* Retrieves registered student data
* Handles database connection errors

### Student Records Module

* Displays all registered students
* Shows internship details and registration information


## 🔮 Future Enhancements

* Admin authentication and login
* Email verification system
* Internship approval workflow
* Search and filter functionality
* Export records to Excel/PDF
* Dashboard with analytics
* REST API integration

---

## 👨‍💻 Author

**Poobesh Pradeepkumar**

* GitHub: https://github.com/ppoobesh

---

## 📄 License

This project is developed for educational and learning purposes.

---

⭐ If you find this project useful, please consider giving it a star on GitHub.
