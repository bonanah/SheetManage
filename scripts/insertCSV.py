# import sqlite3
# import csv
# import os

# # SQLite 데이터베이스 연결 함수
# def connect_to_db():
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     db_path = os.path.join(base_dir, '../database/problems.db')
#     return sqlite3.connect(db_path)

# # CSV 데이터 삽입 함수
# def insert_from_csv(csv_path):
#     conn = connect_to_db()
#     cursor = conn.cursor()

#     with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:  # 'utf-8-sig'로 BOM 제거
#         reader = csv.DictReader(csvfile)

#         # BOM 제거된 헤더 확인
#         print(f"CSV 헤더: {reader.fieldnames}")
        
#         for row in reader:
#             print(f"삽입 중 데이터: {row}")  # 디버깅용 출력
#             cursor.execute('''
#                 INSERT INTO problems (school, grade, semester, term, unit, theme, question, answer, difficulty, image_path)
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#             ''', (
#                 row['school'], row['grade'], row['semester'], row['term'],
#                 row['unit'], row['theme'], row['question'], row['answer'],
#                 row['difficulty'], row['image_path']
#             ))

#     conn.commit()
#     conn.close()

# if __name__ == "__main__":
#     csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../database/problems.csv')
#     insert_from_csv(csv_path)
#     print("CSV 데이터를 데이터베이스에 삽입했습니다.")
