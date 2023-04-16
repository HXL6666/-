# -*- coding : utf-8 -*-
from tkinter import *
from tkinter import messagebox  # 弹窗库
import numpy as np

l = np.full([15, 15], 0)
s = []
num = 0


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.chessman_black_label = self.__chessman_black_label()
        self.chessman_white_label = self.__chessman_white_label()
        self.restart_button = self.__restart_button()
        self.back_button = self.__back_button()
        self.AI_button = self.__AI_button()
        self.quit_button = self.__quit_button()
        self.w = Canvas(self, width=650, height=650, background="#D2BE96")

    def __win(self):
        self.title("双人五子棋")
        width = 900
        height = 650
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def game_line(self):
        for i in range(0, 15):
            ww = 1
            if (i == 0) or (i == 14):  # 边界加粗
                ww = 2
            self.w.create_line(45, i * 40 + 45, 605, i * 40 + 45, width=ww)  # 15条横线
            self.w.create_text(30, i * 40 + 45, text=i + 1)  # 横坐标
            self.w.create_line(i * 40 + 45, 45, i * 40 + 45, 605, width=ww)  # 15条竖线
            self.w.create_text(i * 40 + 45, 30, text=i + 1)  # 纵坐标

        self.w.create_oval(160, 160, 170, 170, fill='black')  # 棋盘上五个黑点
        self.w.create_oval(480, 160, 490, 170, fill='black')
        self.w.create_oval(160, 480, 170, 490, fill='black')
        self.w.create_oval(480, 480, 490, 490, fill='black')
        self.w.create_oval(320, 320, 330, 330, fill='black')

    def __chessman_black_label(self):
        label2 = Label(self, text="黑棋", font=("宋体", 20), background="#D2BE96")
        label1 = Label(self, background="black")
        label1.place(x=750, y=20, width=60, height=35)
        label2.place(x=820, y=20, width=60, height=35)
        return label1, label2

    def __chessman_white_label(self):
        label2 = Label(self, text="白棋", font=("宋体", 20), background="#D2BE96")
        label1 = Label(self, background="white")
        label1.place(x=750, y=60, width=60, height=35)
        label2.place(x=820, y=60, width=60, height=35)
        return label1, label2

    def __restart_button(self):
        btn = Button(self, text="新 局", font=("宋体", 20))
        btn.place(x=700, y=180, width=150, height=50)
        return btn

    def __back_button(self):
        btn = Button(self, text="悔 棋", font=("宋体", 20))
        btn.place(x=700, y=260, width=150, height=50)
        return btn

    def __AI_button(self):
        btn = Button(self, text="单 机", font=("宋体", 20))
        btn.place(x=700, y=340, width=150, height=50)
        return btn

    def __quit_button(self):
        btn = Button(self, text="退 出", font=("宋体", 20), command=quit)
        btn.place(x=700, y=420, width=150, height=50)
        return btn

    def select_color_label(self):
        label = Label(self, text="-->", font=10, background="#D2BE96")
        if num % 2 == 0:
            label.place(x=680, y=20, width=60, height=35)
        else:
            label.place(x=680, y=60, width=60, height=35)
        return label


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def load(self):  # 通过数组还原棋子布局
        global l
        self.w.delete(ALL)  # 删除画布，重新画线
        self.game_line()
        for i in range(15):
            for j in range(15):
                if l[i][j] == 1:
                    self.w.create_oval(40 * i + 30, 40 * j + 30, 40 * i + 60, 40 * j + 60, fill='black')
                elif l[i][j] == -1:
                    self.w.create_oval(40 * i + 30, 40 * j + 30, 40 * i + 60, 40 * j + 60, fill='white')
                else:
                    continue

    def __event_bind(self):
        self.w.bind("<Button -1>", self.down)
        self.restart_button.bind("<Button -1>", self.restart)
        self.back_button.bind("<Button -1>", self.back)
        self.AI_button.bind("<Button -1>", self.AI)
        # self.w.bind("<Motion>",self.game_rules)


    def restart(self, event):  # 重开新局
        global l
        l = np.full([15, 15], 0)  # 数组归零
        self.load()

    def back(self, event):     # 悔棋
        global s, l
        if len(s) > 0:
            i = s[len(s) - 1][0]
            j = s[len(s) - 1][1]
            l[i][j] = 0
            s.pop(len(s) - 1)
            self.load()

    def AI(self, event):
        messagebox.showinfo("Warning", "功能开发中。。。")
        pass

    def down(self, event):  # 落子
        global num, l, s
        # if (30 <= event.x <= 620) and (30 <= event.y <= 620):  # 边界判断
        for j in range(0, 15):
            for i in range(0, 15):
                if (event.x - 45 - 40 * i) ** 2 + (event.y - 45 - 40 * j) ** 2 <= 800:
                    break
            if (event.x - 45 - 40 * i) ** 2 + (event.y - 45 - 40 * j) ** 2 <= 800:
                break
        if num % 2 == 0 and l[i][j] == 0:  # 黑子先下，走奇数
            self.w.create_oval(40 * i + 30, 40 * j + 30, 40 * i + 60, 40 * j + 60, fill='black')
            l[i][j] = 1
            num += 1
        elif num % 2 != 0 and l[i][j] == 0:  # 白子后下，走偶数
            self.w.create_oval(40 * i + 30, 40 * j + 30, 40 * i + 60, 40 * j + 60, fill='white')
            l[i][j] = -1
            num += 1
        s.append((i, j))   # 悔棋序列
        # print(s)
        self.game_rule(i, j)    # 判断
        # self.after(100,self.select_color_label)

    def game_rule(self, i, j):  # 游戏规则判断输赢
        global l
        count1, count2, result = 0, 0, 0
        m, n = i, j
        # 横向判断
        while (i < 14) and (l[i][j] == l[i + 1][j]):
            i += 1
            count1 += 1
        i, j = m, n
        while (i > 0) and (l[i][j] == l[i - 1][j]):
            i -= 1
            count2 += 1
        if count2 + count1 >= 4:
            result = 1
        else:
            count1, count2 = 0, 0
            i, j = m, n

        # 竖向判断
        while (j < 14) and (l[i][j] == l[i][j + 1]):
            j += 1
            count1 += 1
        i, j = m, n
        while (j > 0) and (l[i][j] == l[i][j - 1]):
            j -= 1
            count2 += 1
        if count2 + count1 >= 4:
            result = 1
        else:
            count1, count2 = 0, 0
            i, j = m, n

        # 正斜向判断\
        while (i < 14) and (j < 14) and (l[i][j] == l[i + 1][j + 1]):
            j += 1
            i += 1
            count1 += 1
        i, j = m, n
        while (i > 0) and (j > 0) and (l[i][j] == l[i - 1][j - 1]):
            j -= 1
            i -= 1
            count2 += 1
        if count2 + count1 >= 4:
            result = 1
        else:
            count1, count2 = 0, 0
            i, j = m, n

        # 反斜向判断/
        while (i < 14) and (j > 0) and (l[i][j] == l[i + 1][j - 1]):
            j -= 1
            i += 1
            count1 += 1
        i, j = m, n
        while (i > 0) and (j < 14) and (l[i][j] == l[i - 1][j + 1]):
            j += 1
            i -= 1
            count2 += 1
        if count2 + count1 >= 4:
            result = 1

        if result == 1:
            if l[m][n] == 1:
                messagebox.showinfo("恭喜", "黑棋获胜")
            else:
                messagebox.showinfo("恭喜", "白棋获胜")
            l = np.full([15, 15], 0)  # 重置
            self.load()


    # def game_rules(self,event):
    #     for i in range(45, 645, 40):
    #         for j in range(45, 645, 40):
    #             l1 = i - 15
    #             l2 = i + 15
    #             r1 = j - 15
    #             r2 = j + 15
    #             if l1 <= event.x <= l2 and r1 <= event.y <= r2:
    #                 self.w.create_rectangle(i - 15, j - 15, i + 15, j + 15, dash=(1, 1), outline="blue")
    #                 self.w.pack()


if __name__ == "__main__":
    win = Win()
    win.config(background="#D2B48C")
    win.game_line()
    win.w.pack(side=LEFT)
    win.mainloop()

