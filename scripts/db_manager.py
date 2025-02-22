import sqlite3
import os

# DB 연결하는 함수 
def connect_to_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '../database/problems.db')
    return sqlite3.connect(db_path)

# 테이블 만드는 함수 
def create_tables():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            school TEXT,
            year INTEGER,
            grade TEXT,
            semester TEXT,
            term INTEGER,
            unit INTEGER,
            theme TEXT,
            qNumInTest INTEGER,
            problem_text TEXT,
            answer TEXT,
            difficulty INTEGER,
            image_path TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exam_papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exam_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exam_id INTEGER,
            problem_id INTEGER,
            FOREIGN KEY (exam_id) REFERENCES exam_papers(id),
            FOREIGN KEY (problem_id) REFERENCES problems(id)
        )
    ''')

    conn.commit()
    conn.close()
