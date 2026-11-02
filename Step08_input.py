# Step08_input.py

# 콘솔로 부터 사용자 입력을 받을수 있는 input() 함수 
# 사용자가 Enter 키를 치기 전까지 대기한다 
input_msg = input("메세지 입력:")

print(f"입력한 메세지:{input_msg}")


input_name: str = input("이름 입력:")
input_addr: str = input("주소 입력:")

print(f"이름:{input_name} 주소:{input_addr}")

# 문자열로 입력 받은후
input_age: str = input("나이 입력:")
# 숫자로 변경해서 1을 더한값을 얻어낸다.
age:int = int(input_age) + 1

print(f"당신은 내년에 {age} 살 입니다")


'''
      임의의 숫자를 입력 받아서 입력한 수가 양수 이면 "양수 입니다." 를
      출력 하고자 한다면???

      ( if 문 필요 )
''' 

