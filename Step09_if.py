# Step09_if.py


'''
      임의의 숫자를 입력 받아서 입력한 수가 양수 이면 "양수 입니다." 를
      출력 하고자 한다면???

      ( if 문 필요 )
''' 

input_num: int = int(input("임의의 숫자입력:"))

# 만일 input_num 이 0 보다 크다면 ...
if(input_num > 0):
    print(f"입력한 숫자 {input_num} 은 양수 입니다.")

print("종료 됩니다")