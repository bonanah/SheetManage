import sqlite3
import random
from db_manager import connect_to_db

def select_problems(school = None, year = None, grade = None, semester = None, term = None, unit=None, theme = None, difficulty=None, Quantity = None):
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "SELECT * FROM problems WHERE 1=1"
    params = []

    if school is not None:
        query += " AND school = ?"
        params.append(school)

    if year is not None:
        query += " AND year = ?"
        params.append(year)

    if grade is not None:
        query += "AND grade = ?"
        params.append(grade)

    if semester is not None:
        query += " AND semester = ?"
        params.append(semester)
    
    if term is not None:
        query += " AND term = ?"
        params.append(term)

    if unit is not None:
        query += " AND unit = ?"
        params.append(unit)

    if theme is not None:
        query += "AND theme = ?"
        params.append(theme)
    
    if difficulty is not None:
        query += " AND difficulty = ?"
        params.append(difficulty)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    selected_problems = random.sample(rows, min(Quantity, len(rows)))

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
