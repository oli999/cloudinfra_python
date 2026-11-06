
import tkinter as tk


if __name__ == "__main__":
    # root 창 생성
    root = tk.Tk()
    # 제목 설정 
    root.title("나의 App")
    # 창의 크기
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text="안녕하세요! python GUI 입니다")
    # pady => padding y => y축 padding => 위아래 padding
    label.pack(pady=20)

    # 입력창 
    name_entry = tk.Entry(root, font=("Arial", 12))
    name_entry.pack(pady=5)
    name_entry.focus() # 포커스 주기

    label2 = tk.Label(root, text="결과...")
    label2.pack(pady=20)

    def clicked():
        # print("버튼을 눌렀네?")
        # Entry(입력창) 에 입력한 문자열 읽어오기
        name = name_entry.get()
        # label text 수정하기
        label2.config(text=f"입력한 이름:{name}")
        # 입력창 초기화
        name_entry.delete(0, tk.END)

    # 버튼
    btn = tk.Button(root, text="전송", width=10, bg="lightgray", command=clicked)
    btn.pack(pady=15)

    root.mainloop()
