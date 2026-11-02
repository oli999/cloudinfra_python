# Step04_Str3.py

# yaml 문자열을 다룰때는 외부 모듈을 pip 로 설치를 해서 import 를 해야한다. 
# python 가상환경을 구성하고  pip install  pyyaml  설치후에  yaml 을 다룰수 있다. 
import yaml

# yaml 형식의 문자열 작성해보기
info='''
name: 이정호
addr: 노량진
foods:
  - 맥주
  - 베이컨
isMan: true
body:
  weight: 75
  height: 174
'''

# yaml 형식의 문자열을 로딩해서 dict type 으로 변경하기 
result = yaml.safe_load(info)
print(result)

# dict type 을 다시 yaml 형식의 문자열로 변환하기
result2 = yaml.dump(result, allow_unicode=True, sort_keys=False)

print(result2)

