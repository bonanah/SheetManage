# import sqlite3
# import os

# # SQLite 데이터베이스 연결 함수
# def connect_to_db():
#     # 현재 파일의 경로를 기준으로 데이터베이스 파일 경로 생성
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     db_path = os.path.join(base_dir, '../database/problems.db')
#     print(f"Database path: {db_path}")  # 경로 출력
#     return sqlite3.connect(db_path)

# # 테이블 생성 함수
# def create_table():
#     conn = connect_to_db()
#     cursor = conn.cursor()

#     # 문제 데이터 테이블 생성
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS problems (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             school TEXT,
#             year INTEGER,
#             grade TEXT,
#             semester TEXT,
#             term TEXT,
#             unit TEXT,
#             theme TEXT,
#             qNumInTest INTEGER,
#             questionParagraph TEXT,
#             answer TEXT,
#             difficulty TEXT,
#             image_path TEXT
#         )
#     ''')

#     conn.commit()
#     conn.close()

# # 필터 기준으로 문제를 가져오는 함수
# def get_problems_by_filter(chapter=1, difficulty=1):
#     conn = connect_to_db()
#     cursor = conn.cursor()

#     # SQL 쿼리 동적 생성
#     query = "SELECT * FROM problems WHERE 1=1"
#     params = []

#     if chapter:
#         query += " AND unit = ?"
#         params.append(chapter)
    
#     if difficulty:
#         query += " AND difficulty = ?"
#         params.append(difficulty)

#     cursor.execute(query, params)
#     rows = cursor.fetchall()

#     conn.close()

#     # 결과를 딕셔너리 형태로 반환
#     problems = []
#     for row in rows:
#         problems.append({
#             "id": row[0],
#             "school": row[1],
#             "year": row[2],
#             "grade": row[3],
#             "semester": row[4],
#             "term": row[5],
#             "unit": row[6],         # 단원명
#             "theme": row[7],
#             "qNumInTest": row[8],   # 시험지 내에서의 문제제 번호 
#             "problem_text": row[9], # 문제 내용
#             "answer": row[10],  # 정답 
#             "difficulty": row[11], # 난이도 
#             "image_path": row[12] # 문제 관련 이미지 저장 경로 
#         })

#     return problems

# if __name__ == "__main__":
#     create_table()
#     print("데이터베이스와 테이블이 생성되었습니다.")
