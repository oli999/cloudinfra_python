# gui/binary01.py

# python 에서 2진수 다루기

# 2진수는 숫자를 만들때 prefix 로 0b 
num1 = 0b1010 # 10진수 10

result = num1 + 5
print(result) # 15 가 출력된다

num2 = 150
# 150 의 2진수에 해당하는 문자열이 나온다
result2: str = bin(num2)
print(result2)


line = "abcde12345"

result3 = line[5:10] # 5번 인덱스 이상, 10번 인덱스 미만 인덱스의 문자열 얻어내기
result4 = result2[2:] # 2번 인덱스 이상의 문자열 얻어내기 

print(f"result3:{result3}")
print(f"result4:{result4}")
