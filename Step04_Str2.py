
# import 해야 사용할수 있는 모듈들은 반드시 import 해야 사용할수 있다.
import json


# json 형식의 문자열을 작성하고 python 에서 활용해보자
info = '''
{
    "name":"이정호",
    "addr":"노량진",
    "foods":["맥주","베이컨"]
}
'''

# json 형식의 문자열을 해석해서 dict type 으로 얻어내기 
result = json.loads(info)

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])



# dict 에 저장된 데이터를  json 문자열로 변환
result2 = json.dumps(result)

print("종료합니다")