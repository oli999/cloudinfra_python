# Step11_class2.py

class MyCar:
    def setName(self, name):
        self.name=name

    def drive(self):
        print(f"{self.name} 이(가) 달려요!")

if __name__ == "__main__":
    c1: MyCar = MyCar()
    c1.setName("소나타")
  
    c2: MyCar = MyCar()
    c2.setName("아반떼")

    c1.drive()
    c2.drive()