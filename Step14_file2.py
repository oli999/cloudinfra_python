# Step14_file2.py

import os


if __name__ == "__main__":

    # 새로운 파일을 만들어서 문자열을 파일에 출력하기

    letter_path = os.path.join(os.getcwd(), "letter.txt")

    # "w" 는 없으면 새로 파일을 만들고 write, 있으면 기존 내용을 덮어쓰기 
    with open(letter_path, "w", encoding="utf-8") as f:
        f.write("To my Friend \n")
        f.write("Hello \n")
        f.write("Bye \n")

    letter_path2 = os.path.join(os.getcwd(), "letter2.txt")
    
    # "a" 는 추가하기 모드 (기존 내용 유지) 
    with open(letter_path2, "a", encoding="utf-8") as f:
        f.write("To my Friend \n")
        f.write("Hello \n")
        f.write("Bye \n")

    # [quiz]  input() 함수를 이용해서 입력받은 문자열을 txt 파일에 저장하는 프로그래밍을 해보세요.