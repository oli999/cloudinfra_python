# gui/test01.py

import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    
    # 입력창 
    entry = tk.Entry(root)
    entry.pack(pady=10)

    root.mainloop()