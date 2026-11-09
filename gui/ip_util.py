import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress

class SubnetCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Subnet Calculator Pro")
        self.root.geometry("520x450")
        
        # 현재 정상 계산된 네트워크 객체를 저장할 변수
        self.current_network = None

        # 1. 안내 문구 및 입력창
        tk.Label(root, text="네트워크 대역 입력 (예: 172.16.8.0/25)", font=("Arial", 12)).pack(pady=(15, 5))
        
        self.entry = tk.Entry(root, font=("Courier", 16), justify='center')
        self.entry.pack(pady=5, padx=30, fill='x')
        self.entry.bind("<KeyRelease>", self.calculate_subnet)

        self.status_label = tk.Label(root, text="IP 및 서브넷(CIDR)을 입력하세요", fg="gray", font=("Arial", 10))
        self.status_label.pack(pady=(0, 15))

        # 2. 결과 출력 영역 (Grid)
        info_frame = tk.Frame(root)
        info_frame.pack(pady=10)

        lbl_font, val_font = ("Arial", 11, "bold"), ("Courier", 11, "bold")
        labels = ["네트워크 주소 :", "서브넷 마스크 :", "사용 가능 IP 범위 :", "브로드캐스트 :", "총 가용 IP 수 :"]
        self.result_vars = {} # 결과 라벨들을 딕셔너리로 관리

        for i, text in enumerate(labels):
            tk.Label(info_frame, text=text, font=lbl_font).grid(row=i, column=0, sticky='e', pady=6, padx=10)
            val_label = tk.Label(info_frame, text="-", font=val_font, fg="blue")
            val_label.grid(row=i, column=1, sticky='w')
            self.result_vars[i] = val_label

        # 3. 모든 서브넷 범위 보기 버튼 (초기에는 비활성화)
        self.btn_show_all = ttk.Button(root, text="이 대역의 모든 서브넷 범위 보기", state=tk.DISABLED, command=self.show_all_subnets)
        self.btn_show_all.pack(pady=15)

        self.entry.focus()

    def calculate_subnet(self, event=None):
        ip_str = self.entry.get().strip()
        
        if not ip_str:
            self.status_label.config(text="IP 및 서브넷(CIDR)을 입력하세요", fg="gray")
            self.clear_outputs()
            return

        try:
            network = ipaddress.IPv4Network(ip_str, strict=False)
            self.current_network = network  # 성공 시 객체 저장
            
            # 정보 추출
            net_address = str(network.network_address)
            net_mask = str(network.netmask)
            broadcast = str(network.broadcast_address)
            
            if network.prefixlen >= 31:
                first_ip = net_address
                last_ip = broadcast if network.prefixlen == 31 else net_address
                usable_count = 2 if network.prefixlen == 31 else 1
            else:
                first_ip = str(network.network_address + 1)
                last_ip = str(network.broadcast_address - 1)
                usable_count = network.num_addresses - 2

            # 화면 갱신
            self.status_label.config(text="✓ 정상적으로 계산되었습니다.", fg="green")
            self.result_vars[0].config(text=net_address)
            self.result_vars[1].config(text=f"{net_mask} (/{network.prefixlen})")
            self.result_vars[2].config(text=f"{first_ip} ~ {last_ip}")
            self.result_vars[3].config(text=broadcast)
            self.result_vars[4].config(text=f"{usable_count:,} 개")
            
            # 버튼 활성화
            self.btn_show_all.config(state=tk.NORMAL)

        except ValueError:
            self.status_label.config(text="올바른 형식(CIDR)이 아닙니다. (예: 172.16.8.0/25)", fg="red")
            self.clear_outputs()

    def clear_outputs(self):
        self.current_network = None
        self.btn_show_all.config(state=tk.DISABLED)
        for label in self.result_vars.values():
            label.config(text="-")

    # 새 창을 띄워 전체 서브넷을 계산하고 표(Treeview)로 보여주는 함수
    def show_all_subnets(self):
        if not self.current_network:
            return
            
        prefix = self.current_network.prefixlen
        
        # 기준 부모 대역 설정 (입력값이 /25면 부모는 /24 클래스 C 대역이 됨)
        if prefix >= 24:
            parent_prefix = 24
        elif prefix >= 16:
            parent_prefix = 16
        else:
            parent_prefix = 8
            
        # 부모 대역폭을 기준으로 현재 prefix 크기로 모두 쪼개기(subnets)
        parent_net = ipaddress.IPv4Network(f"{self.current_network.network_address}/{parent_prefix}", strict=False)
        subnets = list(parent_net.subnets(new_prefix=prefix))

        # 1. 새 창(Toplevel) 생성
        sub_win = tk.Toplevel(self.root)
        sub_win.title(f"/{prefix} 서브넷 전체 목록 (기준: /{parent_prefix})")
        sub_win.geometry("650x350")
        
        # 2. 표(Treeview) 및 스크롤바 프레임
        frame = tk.Frame(sub_win)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        columns = ("net", "range", "brd")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        
        tree.heading("net", text="네트워크 주소")
        tree.heading("range", text="사용 가능 IP 범위")
        tree.heading("brd", text="브로드캐스트")
        
        tree.column("net", width=120, anchor="center")
        tree.column("range", width=250, anchor="center")
        tree.column("brd", width=120, anchor="center")
        
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)
        
        # 3. 쪼개진 서브넷 데이터를 표에 삽입
        for sn in subnets:
            if sn.prefixlen >= 31:
                ip_range = f"{sn.network_address} ~ {sn.broadcast_address}"
            else:
                ip_range = f"{sn.network_address + 1} ~ {sn.broadcast_address - 1}"
                
            # 현재 선택한 네트워크와 일치하는 줄은 알아보기 쉽게 표시
            values = (str(sn.network_address), ip_range, str(sn.broadcast_address))
            if sn == self.current_network:
                tree.insert("", tk.END, values=values, tags=('current',))
            else:
                tree.insert("", tk.END, values=values)
                
        # 현재 입력한 대역에 색상 하이라이트 적용
        tree.tag_configure('current', background='#e6f2ff')

if __name__ == "__main__":
    root = tk.Tk()
    app = SubnetCalculatorApp(root)
    root.mainloop()