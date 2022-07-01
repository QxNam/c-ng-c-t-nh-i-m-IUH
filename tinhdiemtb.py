#from asyncio.windows_events import NULL
from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tính điểm IUH')
        self.geometry("300x230")
        self.tk1 = StringVar()
        self.tk2 = StringVar()
        self.tk3 = StringVar()
        self.tk4 = StringVar()
        self.th1 = StringVar()
        self.th2 = StringVar()
        self.th3 = StringVar()
        self.gk = StringVar()
        self.ck = StringVar()
        self.tc = StringVar()

        self.create_widgets()

    def create_widgets(self):
        # label
        Label(self, text='Điểm thường kì').grid(row=1, column=1)
        Label(self, text='Điểm thực hành').grid(row=2, column=1)
        Label(self, text='Điểm giữa kì').grid(row=3, column=1)
        Label(self, text='Điểm cuối kì').grid(row=4, column=1)
        Label(self, text='Số tín chỉ').grid(row=5, column=1)
        # Entry
        Entry(self, width=3, textvariable=self.tk1).grid(row=1, column=2)
        Entry(self, width=3, textvariable=self.tk2).grid(row=1, column=3)
        Entry(self, width=3, textvariable=self.tk3).grid(row=1, column=4)
        Entry(self, width=3, textvariable=self.tk4).grid(row=1, column=5)

        Entry(self, width=3, textvariable=self.th1).grid(row=2, column=2)
        Entry(self, width=3, textvariable=self.th2).grid(row=2, column=3)
        Entry(self, width=3, textvariable=self.th3).grid(row=2, column=4)

        Entry(self, width=3, textvariable=self.gk).grid(row=3, column=2)
        Entry(self, width=3, textvariable=self.ck).grid(row=4, column=2)
        Entry(self, width=3, textvariable=self.tc).grid(row=5, column=2)
        # Button
        Button(self, text='Xem điểm', command=self.submit).grid(column=1, row=6)

        Button(self, text='reset', command=self.resetAll).grid(column=2, row=6, columnspan=3)
    def resetAll(self):
        self.tk1.set('')
        self.tk2.set('')
        self.tk3.set('')
        self.tk4.set('')
        self.th1.set('')
        self.th2.set('')
        self.th3.set('')
        self.gk.set('')
        self.ck.set('')
        self.tc.set('')
 
    def diemHe10(self):
        lst_tk = [float(i) for i in [self.tk1.get(), self.tk2.get(), self.tk3.get(), self.tk4.get()] if i!='']
        th = [float(i) for i in [self.th1.get(), self.th2.get(), self.th3.get()] if i!='']
        s = ((sum(lst_tk)/len(lst_tk)*2) + float(self.gk.get())*3 + float(self.ck.get())*5)/10
        if len(th)==0:
            return s
        return (s*(int(self.tc.get())-1)+(sum(th)/len(th)))/int(self.tc.get())
    def xepHang(self):
        xh = list({4: 'A+: Xuất sắc', 3.8: 'A: Giỏi', 3.5: 'B+: Khá', 3: 'B: Khá', 2.5: 'C+: Trung bình', 2: 'C: Trung bình', 1.5: 'D+: Trung bình yếu', 1: 'D: Trung bình yếu', 0: 'F: Kém'}.items())
        diem10 = self.diemHe10()
        lstd10 = [9, 8.5, 8, 7, 6, 5.5, 5, 4, 0]
        for i in range(len(lstd10)):
            if diem10>=lstd10[i]:
                return (xh[i][0], xh[i][1])
    def submit(self):
        Label(self, text='Điểm hệ 10: %.1f'%(self.diemHe10())).grid(row=7, column=1)
        Label(self, text='Điểm hệ 4: %.1f'%(self.xepHang()[0])).grid(row=8, column=1)
        Label(self, text='Điểm chữ/Xếp loại: %s'%(self.xepHang()[1])).grid(row=9, column=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()