# Step10_jinja2.py

'''
    Template 문자열을 정의하고 어떤 데이터를 Template 문자열에 전달해서 
    결과 문자열을 얻어내는 작업을 jinja2 를 이용해서 테스트 해보자 

    python 가상환경 활성화 한다음 설치 후에 사용해야 한다

    pip install jinja2
'''

# pip 로 설치한 jinja2 로 부터 Template 클래스를 import 하기 
from jinja2 import Template

# 테스트용 template 이라고 가정 

my_template = '''
    번호 : {{ num }}
    이름 : {{ name }}
    주소 : {{ addr }}
'''

# template 에 출력할 데이터 라고 가정하자
mem1 = {"num":1, "name":"김구라", "addr":"노량진"}
mem2 = {"num":2, "name":"해골", "addr":"행신동"}

# import 한 클래스를 이용해서 객체 생성
# 클래스로 객체 생성하는 방법 => 클래스명( )
# 객체 생성하면서 객체 내부에서 사용될 값을 전달하는 방법  =>  클래스명(값)
t1: Template = Template(my_template)
# Template 객체의 render() 기능을 호출하면서 dict 를 전달하면 렌더링된 결과가 나온다.
result1: str = t1.render(mem1)
print(result1)

print("---")

result2: str = t1.render(mem2)
print(result2)