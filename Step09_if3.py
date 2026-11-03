# Step09_if3.py

'''
    임의의 숫자를 입력 받아서 입력받은 수가 짝수면  "짝수 입니다"
    홀수면 "홀수 입니다" 를 출력하는 code 를 작성해 보세요.
    힌트)  input_num%2 == 0
'''

input_num: int = int(input("숫자입력:"))

if input_num%2 == 0 :
    print("짝수 입니다")
else:
    print("홀수 입니다")

