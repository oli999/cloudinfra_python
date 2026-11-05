# Step14_file.py


import os


if __name__ == "__main__":

    # 현재 작업 경로 얻어내기 
    cwd: str = os.getcwd()
    # 현재 운영체제의 파일 구분자 얻어내기 ( window 는 역슬레시, linux 는 슬레시)
    sep: str = os.sep

    print(f"cwd:{cwd}")
    print(f"sep:{sep}")

    # memo.txt 파일이 위치하는 절대 경로 구성하기
    # .join() 운영체제에 맞는 적절한 파일 구분자를 이용해서 두 경로를 합쳐준다.
    #path: str = os.getcwd()+"\\"+"memo.txt"
    #path: str = os.getcwd()+"/"+"memo.txt"
    #path: str = os.getcwd()+sep+"memo.txt"
    path: str = os.path.join(os.getcwd(), "memo.txt")
    print(f"path:{path}")

    # open 함수를 이용해서 파일을 "r" 읽기전용으로 읽어서 입출력 객체를 얻어내기 
    f = open(path, "r", encoding="utf-8")
    try:
        # 예외가 발생할것을 대비해서 try~except 블럭으로 감싼다 
        result = f.read()
    except Exception as e:
        print(e)
    finally:
        f.close() # 중요한 마무리 작업을 한다

    # 결과 출력하기 
    print(result)

    print("---")

    # 위와 동일한 동작을 with 구문을 이용하면 아래와 같다 
    with open(path, "r", encoding="utf-8") as f2:
        result2 = f2.read()
        print(result2)
        # 들여쓰기가 끝나는 지점에서 자동으로 f2.close() 를 실행해준다 (에러가 나도 실행됨)








