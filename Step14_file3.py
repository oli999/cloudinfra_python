# Step14_file3.py

import os


if __name__ == "__main__":
    # 1. 읽어올 파일의 경로 설정
    file_path = os.path.join(os.getcwd(), "user_input.txt")

    # 2. 읽기 전용 모드로 파일 열기 
    with open(file_path, "r", encoding="utf-8") as f:
        # 파일의 전체 내용을 한번에 읽어서 변수에 저장 
        content = f.read()
    
    print("--- 저장된 파일 내용 ---")
    print(content)
