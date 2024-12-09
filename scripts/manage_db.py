import sqlite3

# SQLite 데이터베이스 연결 함수
def connect_to_db():
    return sqlite3.connect('database/problems.db')  # 데이터베이스 파일명

# 테이블 생성 함수
def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    # 문제 데이터 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            grade INTEGER,
            subject TEXT,
            difficulty TEXT,
            image_path TEXT
        )
    ''')

    conn.commit()
    conn.close()

# 데이터 삽입 함수
def insert_problem(question, answer, grade, subject, difficulty, image_path):
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO problems (question, answer, grade, subject, difficulty, image_path)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, answer, grade, subject, difficulty, image_path))

    conn.commit()
    conn.close()

# 데이터 조회 함수
def fetch_problems():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM problems')
    problems = cursor.fetchall()

    conn.close()
    return problems

# 연결 테스트 및 테이블 생성
if __name__ == "__main__":
    create_table()
    print("데이터베이스와 테이블이 생성되었습니다.")
