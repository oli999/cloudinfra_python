# gui/binary04.py

ip_addr = input("ip 주소입력:(예:192.168.0.1)")

# . 으로 분리해서 list 에 담아오기 
ip_parts = ip_addr.split(".")

# list 안에 저장된 item 확인
print(ip_parts)

# 빈 배열을 하나 만들고
binary_parts=[]

for item in ip_parts:
    # :08b 는 뒤에서 부터 읽으면 b(2진수) 로 변환하되 총 8자리로 변환하고 빈곳은 0 으로 채움
    print(f"{int(item):08b}")
    # 2 진수 8자리로 구성된 값을 빈배열에 추가(append) 하기
    binary_parts.append(f"{int(item):08b}")

print(binary_parts)