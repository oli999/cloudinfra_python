import tkinter as tk
from tkinter import ttk
import ipaddress

class SubnetCalculatorApp:
    # 생성자 
    def __init__(self, root):
        self.root = root
        self.root.title("Subnet Calculator Pro (with Binary)")
        self.root.geometry("900x550")
        
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
        self.result_vars = {} 

        for i, text in enumerate(labels):
            tk.Label(info_frame, text=text, font=lbl_font).grid(row=i, column=0, sticky='ne', pady=12, padx=10)
            val_label = tk.Label(info_frame, text="-", font=val_font, fg="blue", justify='left')
            val_label.grid(row=i, column=1, sticky='w')
            self.result_vars[i] = val_label

        # 3. 모든 서브넷 범위 보기 버튼
        self.btn_show_all = ttk.Button(root, text="이 대역의 모든 서브넷 범위 보기", state=tk.DISABLED, command=self.show_all_subnets)
        self.btn_show_all.pack(pady=15)

        self.entry.focus()

    def ip_to_bin(self, ip_str):
        """IPv4 주소를 8비트 2진수 문자열로 변환해주는 함수"""
        return ".".join(f"{int(x):08b}" for x in str(ip_str).split('.'))

    def calculate_subnet(self, event=None):
        ip_str = self.entry.get().strip()
        
        if not ip_str:
            self.status_label.config(text="IP 및 서브넷(CIDR)을 입력하세요", fg="gray")
            self.clear_outputs()
            return

        try:
            network = ipaddress.IPv4Network(ip_str, strict=False)
            self.current_network = network  
            
            # 10진수 추출
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

            # 2진수 변환
            net_bin = self.ip_to_bin(net_address)
            mask_bin = self.ip_to_bin(net_mask)
            first_bin = self.ip_to_bin(first_ip)
            last_bin = self.ip_to_bin(last_ip)
            brd_bin = self.ip_to_bin(broadcast)

            # 화면 갱신
            self.status_label.config(text="✓ 정상적으로 계산되었습니다.", fg="green")
            self.result_vars[0].config(text=f"{net_address}\n{net_bin}")
            self.result_vars[1].config(text=f"{net_mask} (/{network.prefixlen})\n{mask_bin}")
            self.result_vars[2].config(text=f"{first_ip} ~ {last_ip}\n{first_bin} ~ {last_bin}")
            self.result_vars[3].config(text=f"{broadcast}\n{brd_bin}")
            self.result_vars[4].config(text=f"{usable_count:,} 개\n")
            
            self.btn_show_all.config(state=tk.NORMAL)

        except ValueError:
            self.status_label.config(text="올바른 형식(CIDR)이 아닙니다. (예: 172.16.8.0/25)", fg="red")
            self.clear_outputs()

    def clear_outputs(self):
        self.current_network = None
        self.btn_show_all.config(state=tk.DISABLED)
        for label in self.result_vars.values():
            label.config(text="-")

    # =================================================================
    # 팝업창: 표 형식으로 10진수와 2진수를 번갈아가며 출력하도록 수정된 부분
    # =================================================================
    def show_all_subnets(self):
        if not self.current_network:
            return
            
        prefix = self.current_network.prefixlen
        
        if prefix >= 24: parent_prefix = 24
        elif prefix >= 16: parent_prefix = 16
        else: parent_prefix = 8
            
        parent_net = ipaddress.IPv4Network(f"{self.current_network.network_address}/{parent_prefix}", strict=False)
        subnets = list(parent_net.subnets(new_prefix=prefix))

        sub_win = tk.Toplevel(self.root)
        sub_win.title(f"/{prefix} 서브넷 전체 목록 (기준: /{parent_prefix})")
        # 2진수 범위가 한 화면에 최대한 보이도록 창 너비 대폭 확대
        sub_win.geometry("1200x450")
        
        frame = tk.Frame(sub_win)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 가로/세로 스크롤바 추가
        y_scroll = ttk.Scrollbar(frame, orient="vertical")
        x_scroll = ttk.Scrollbar(frame, orient="horizontal")
        
        columns = ("net", "range", "brd")
        tree = ttk.Treeview(frame, columns=columns, show="headings", 
                            yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        
        y_scroll.config(command=tree.yview)
        x_scroll.config(command=tree.xview)
        
        tree.heading("net", text="네트워크 주소")
        tree.heading("range", text="사용 가능 IP 범위")
        tree.heading("brd", text="브로드캐스트")
        
        # 2진수 길이에 맞춰 컬럼 너비 넉넉하게 설정
        tree.column("net", width=280, anchor="center")
        tree.column("range", width=560, anchor="center")
        tree.column("brd", width=280, anchor="center")
        
        y_scroll.pack(side="right", fill="y")
        x_scroll.pack(side="bottom", fill="x")
        tree.pack(side="left", fill="both", expand=True)
        
        # 표 데이터 삽입 (1서브넷 당 10진수 1줄, 2진수 1줄씩 쌍으로 삽입)
        for sn in subnets:
            # 10진수 데이터 준비
            if sn.prefixlen >= 31:
                dec_range = f"{sn.network_address} ~ {sn.broadcast_address}"
                bin_range = f"{self.ip_to_bin(sn.network_address)} ~ {self.ip_to_bin(sn.broadcast_address)}"
            else:
                dec_range = f"{sn.network_address + 1} ~ {sn.broadcast_address - 1}"
                bin_range = f"{self.ip_to_bin(sn.network_address + 1)} ~ {self.ip_to_bin(sn.broadcast_address - 1)}"
                
            dec_net = str(sn.network_address)
            dec_brd = str(sn.broadcast_address)
            
            # 2진수 데이터 준비
            bin_net = self.ip_to_bin(sn.network_address)
            bin_brd = self.ip_to_bin(sn.broadcast_address)

            # 현재 입력된 네트워크 대역인 경우 배경색 하이라이트용 태그 설정
            if sn == self.current_network:
                tag_dec = ('current_dec',)
                tag_bin = ('current_bin',)
            else:
                tag_dec = ('dec',)
                tag_bin = ('bin',)
                
            # 10진수 행 삽입
            tree.insert("", tk.END, values=(dec_net, dec_range, dec_brd), tags=tag_dec)
            # 바로 밑에 2진수 행 삽입
            tree.insert("", tk.END, values=(bin_net, bin_range, bin_brd), tags=tag_bin)

        # 태그(Tag)를 이용해 텍스트 색상 및 배경색 디자인 적용
        tree.tag_configure('dec', foreground='black')
        tree.tag_configure('bin', foreground='gray') # 2진수는 회색으로 처리해 시각적 분리
        tree.tag_configure('current_dec', background='#e6f2ff', foreground='black')
        tree.tag_configure('current_bin', background='#e6f2ff', foreground='#668cff')

if __name__ == "__main__":
    root = tk.Tk()
    app = SubnetCalculatorApp(root)
    root.mainloop()