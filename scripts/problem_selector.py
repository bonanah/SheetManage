import sqlite3
import random
from db_manager import connect_to_db

def select_problems(unit=None, difficulty=None, num_questions=5):
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "SELECT * FROM problems WHERE 1=1"
    params = []

    if unit is not None:
        query += " AND unit = ?"
        params.append(unit)
    
    if difficulty is not None:
        query += " AND difficulty = ?"
        params.append(difficulty)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    selected_problems = random.sample(rows, min(num_questions, len(rows)))

    problems = []
    for row in selected_problems:
        problems.append({
            "id": row[0],
            "school": row[1],
            "year": row[2],
            "grade": row[3],
            "semester": row[4],
            "term": row[5],
            "unit": row[6],
            "theme": row[7],
            "qNumInTest": row[8],
            "problem_text": row[9],
            "answer": row[10],
            "difficulty": row[11],
            "image_path": row[12]
        })

    return problems
