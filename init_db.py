import sqlite3

def init_db():
    conn = sqlite3.connect("elearning.db")
    cur = conn.cursor()

    # Drop old tables if they exist
    cur.execute("DROP TABLE IF EXISTS enrollments;")
    cur.execute("DROP TABLE IF EXISTS students;")
    cur.execute("DROP TABLE IF EXISTS courses;")

    # Create Students table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
    """)

    # Create Courses table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    );
    """)

    # Create Enrollments table (using student_id, course_id)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        progress INTEGER DEFAULT 0,
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (course_id) REFERENCES courses (id)
    );
    """)

    # Insert sample students
    cur.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("John Doe", "john@example.com"))
    cur.execute("INSERT INTO students (name, email) VALUES (?, ?)", ("Alice Smith", "alice@example.com"))

    # Insert sample courses
    cur.execute("INSERT INTO courses (name, description) VALUES (?, ?)", ("Python Basics", "Learn Python from scratch"))
    cur.execute("INSERT INTO courses (name, description) VALUES (?, ?)", ("HTML & CSS", "Learn web development basics"))

    # Insert sample enrollments
    cur.execute("INSERT INTO enrollments (student_id, course_id, progress) VALUES (?, ?, ?)", (1, 1, 20))
    cur.execute("INSERT INTO enrollments (student_id, course_id, progress) VALUES (?, ?, ?)", (2, 2, 50))

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_db()
