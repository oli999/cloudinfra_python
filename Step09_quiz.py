# Step09_quiz.py

'''
    비밀번호를 입력받아서 입력한 비밀 번호가 8 자 이상이면 
    
    "사용가능한 비밀 번호 입니다"
    
    그렇지 않으면 

    "사용 불가 입니다"

    를 출력하는 간단한 프로그래밍을 해 보세요.
    - hint : len()
'''

# 무한 루프를 활용할수도 있다 (ctrl+c 로 탈출)
while True:
    input_pwd: str = input("비밀번호 입력:")

    if len(input_pwd) >= 8 :
        print("사용 가능한 비밀번호 입니다")
    else:
        print("사용 불가 입니다")