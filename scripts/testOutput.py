import sqlite3
import os

# SQLite 데이터베이스 연결 함수
def connect_to_db():
    # 데이터베이스 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '../database/problems.db')
    return sqlite3.connect(db_path)

# 데이터 출력 함수
def fetch_and_print_problems():
    conn = connect_to_db()
    cursor = conn.cursor()

    # 데이터 조회 쿼리 실행
    cursor.execute('SELECT * FROM problems')
    rows = cursor.fetchall()  # 모든 데이터 가져오기

    # 테이블 헤더 출력
    print("ID | School    | Grade   | Semester | Term    | Unit     | Theme      | Question      | Answer       | Difficulty | Image Path")
    print("-" * 120)

    # 각 행 출력
    for row in rows:
        print(f"{row[0]} | {row[1]:<10} | {row[2]:<8} | {row[3]:<9} | {row[4]:<8} | {row[5]:<10} | {row[6]:<10} | {row[7]:<15} | {row[8]:<12} | {row[9]:<10} | {row[10]}")

    # 연결 종료
    conn.close()

# 실행 코드
if __name__ == "__main__":
    fetch_and_print_problems()
