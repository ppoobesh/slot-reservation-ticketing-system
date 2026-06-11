from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'internship_db'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"❌ Database connection failed: {e}")
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register_student():
    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        college = request.form.get('college', '').strip()
        department = request.form.get('department', '').strip()
        year_of_study    = request.form.get('year_of_study', '').strip()
        internship_domain = request.form.get('internship_domain', '').strip()
        start_date       = request.form.get('start_date', '').strip()
        end_date         = request.form.get('end_date', '').strip()

    # Basic validation
    if not all([full_name, email, phone, college, department,
                year_of_study, internship_domain, start_date, end_date]):
        return render_template('index.html', error='All fields are required.')

    conn = get_db_connection()
    if not conn:
        return render_template('index.html', error='Database connection failed.')

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO students
            (full_name, email, phone, college, department, year_of_study, internship_domain, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (full_name, email, phone, college, department,
                             year_of_study, internship_domain, start_date, end_date))
        conn.commit()

        # Pass details to welcome page
        student = {
            'full_name': full_name,
            'email': email,
            'phone': phone,
            'college': college,
            'department': department,
            'year_of_study': year_of_study,
            'internship_domain': internship_domain,
            'start_date': start_date,
            'end_date': end_date,
        }
        return render_template('welcome.html', student=student)

    except mysql.connector.IntegrityError:
        return render_template('index.html', error='This email is already registered.')
    except Error as e:
        return render_template('index.html', error=f'Database error: {str(e)}')
    finally:
        cursor.close()
        conn.close()


@app.route('/students')
def all_students():
    conn = get_db_connection()
    if not conn:
        return render_template('students.html', students=[], error='Database connection failed.')

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for s in students:
            for key in ['start_date', 'end_date', 'registered_at']:
                if s.get(key):
                    s[key] = str(s[key])
        return render_template('students.html', students=students)
    except Error as e:
        return render_template('students.html', students=[], error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/email')
def validate_email():
    return render_template('email.html')


if __name__ == '__main__':
    print("🚀 Flask server starting at http://localhost:5000")
    app.run(debug=True, port=5000)