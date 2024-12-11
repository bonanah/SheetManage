import sqlite3
import os

# SQLite 데이터베이스 연결 함수
def connect_to_db():
    # 현재 파일의 경로를 기준으로 데이터베이스 파일 경로 생성
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '../database/problems.db')
    print(f"Database path: {db_path}")  # 경로 출력
    return sqlite3.connect(db_path)

# 테이블 생성 함수
def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    # 문제 데이터 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            school TEXT,
            grade TEXT,
            semester TEXT,
            term TEXT,
            unit TEXT,
            theme TEXT,
            question TEXT,
            answer TEXT,
            difficulty TEXT,
            image_path TEXT
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("데이터베이스와 테이블이 생성되었습니다.")
