import sqlite3
import json
import datetime
from db_manager import connect_to_db

def save_exam_paper(title, selected_problems):
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO exam_papers (title) VALUES (?)", (title,))
    exam_id = cursor.lastrowid

    for problem in selected_problems:
        cursor.execute("INSERT INTO exam_questions (exam_id, problem_id) VALUES (?, ?)", (exam_id, problem["id"]))

    conn.commit()
    conn.close()

    return exam_id

def save_exam_to_json(title, selected_problems):
    exam_data = {
        "title": title,
        "created_at": str(datetime.datetime.now()),
        "questions": selected_problems
    }

    file_name = f"../data/generated_exams/{title.replace(' ', '_')}.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(exam_data, f, indent=4, ensure_ascii=False)

    return file_name
