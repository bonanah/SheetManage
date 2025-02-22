from db_manager import create_tables
from problem_selector import select_problems
from exam_generator import save_exam_paper, save_exam_to_json

if __name__ == "__main__":
    create_tables()

    selected_problems = select_problems(unit=1, difficulty=2, num_questions=5)

    exam_id = save_exam_paper("중간고사 대비 문제지", selected_problems)
    print(f"문제지 ID {exam_id}가 생성되었습니다.")

    file_name = save_exam_to_json("중간고사 대비 문제지", selected_problems)
    print(f"문제지가 {file_name}로 저장되었습니다.")
