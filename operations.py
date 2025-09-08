import sqlite3
from database import get_connection

def get_connection():
    return sqlite3.connect("elearning.db")

# ---------------- Students ----------------
def add_student(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print(f"✅ Student '{name}' added successfully!")

def view_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    print("\n👩‍🎓 Students:")
    for row in rows:
        print(row)

# ---------------- Courses ----------------
def add_course(title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO courses (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    print(f"✅ Course '{title}' added successfully!")

def view_courses():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    rows = cur.fetchall()
    conn.close()
    print("\n📚 Courses:")
    for row in rows:
        print(row)

# ---------------- Enrollments ----------------
def enroll_student(student_id, course_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO enrollments (student_id, course_id, progress) VALUES (?, ?, 0)", (student_id, course_id))
    conn.commit()
    conn.close()
    print(f"🎓 Student {student_id} enrolled in Course {course_id} successfully!")

def view_enrollments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT s.name, c.title, e.progress
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
    """)
    rows = cur.fetchall()
    conn.close()
    print("\n📋 Enrollments:")
    for row in rows:
        name, course, progress = row
        print(f"👩‍🎓 {name} → 📚 {course} → 📈 {progress}%")

def update_progress(student_id, course_id, progress):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE enrollments SET progress=? WHERE student_id=? AND course_id=?", (progress, student_id, course_id))
    conn.commit()
    conn.close()
    print(f"📈 Progress updated to {progress}% for student {student_id} in course {course_id}")

# ---------------- Dashboard ----------------
def dashboard():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    students_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM courses")
    courses_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM enrollments")
    enrollments_count = cur.fetchone()[0]

    conn.close()

    print("\n📊 Dashboard")
    print(f"👩‍🎓 Total Students: {students_count}")
    print(f"📚 Total Courses: {courses_count}")
    print(f"📝 Total Enrollments: {enrollments_count}")
