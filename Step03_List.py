# list type 에 대해서 알아보자
"""
    - list type
    1. 순서가 있다
    2. 여러 type 의 데이터를 저장할 수 있다
    3. 값 변경 가능
"""

# 대부분 한가지 data type 을 담지만 
nums=[10, 20, 30]
names=["김구라","해골","원숭이"]
# 여러가지 data type 을 섞어서 담을수도 있다. 
datas=[10, "xxx", True]

nums.append(40)

# len() builtin 함수를 이용해서 list 의 길이를 얻어낼수 있다.
nums_len = len(nums)

# 인덱스에 의한 참조
name0 = names[0]

# 인덱스를 이용해서 삭제
del names[0] # 0번 인덱스 삭제 

# 값에 의한 삭제
names.remove("원숭이")

# 맨마지막 index 를 삭제하면서 값을 가져오기
nums.pop()
result = nums.pop()

print("종료 합니다")