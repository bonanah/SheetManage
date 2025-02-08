# from docx import Document
# import os

# def extract_from_docx(file_path, output_folder):
#     doc = Document(file_path)
#     base_name = os.path.splitext(os.path.basename(file_path))[0]

#     text_data = []
#     image_counter = 1

#     for idx, para in enumerate(doc.paragraphs):
#         if para.text.strip():
#             text_data.append(f"문제 {idx+1}: {para.text.strip()}")

#     # 이미지 추출
#     for rel in doc.part.rels.values():
#         if "image" in rel.target_ref:
#             img_data = rel.target_part.blob
#             img_path = os.path.join(output_folder, f"{base_name}_img{image_counter}.png")
#             with open(img_path, "wb") as img_file:
#                 img_file.write(img_data)
#             image_counter += 1

#     return text_data

# if __name__ == "__main__":
#     input_folder = "../data/problems"
#     output_folder = "../data/images"
#     output_csv = "../output/problems.csv"

#     all_data = []

#     for file_name in os.listdir(input_folder):
#         if file_name.endswith(".docx"):
#             file_path = os.path.join(input_folder, file_name)
#             print(f"Processing {file_name}...")
#             data = extract_from_docx(file_path, output_folder)
#             all_data.extend(data)

#     # Save to CSV
#     with open(output_csv, "w", encoding="utf-8") as csv_file:
#         csv_file.write("문제 텍스트\n")
#         for item in all_data:
#             csv_file.write(item + "\n")
#     print("Extraction complete!")
