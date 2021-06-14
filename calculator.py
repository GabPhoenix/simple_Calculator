''' 
|Powered by Gabriel Carvalho
|Github> https://github.com/GabPhoenix
|instagram> https://www.instagram.com/iamgabc/
'''
#imports
import tkinter as tk
from tkinter import font
from tkinter.constants import ANCHOR, END


class TopLevel:
    def __init__(self):
        # colors and fonts
        grey = '#DBD4D4' #entry
        grey2 = '#A6A6A6' #buttons
        black = '#222020'
        cyan = '#5CE1E6'
        orange = '#FF914D'
        font1 = "-family {Seoge UI} -size 24 -weight bold" #Buttons
        font2 = "-family {Seoge UI} -size 18 -weight bold" #Entry

        self.top = tk.Tk()
        self.top.geometry("350x425+400+150")
        self.top.iconbitmap("icon.ico")
        self.top.resizable(0, 0)
        self.top.title("Calculator")
        self.top.configure(background = black)
        
        self.entry = tk.Entry(self.top)
        self.entry.place(relx=0.01, rely=0.01, width=340, height=85)
        self.entry.configure(
            background=grey,
            justify='right',
            font=font2
        )
        #Linha 1
        
        #button7
        self.button7 = tk.Button(self.top)
        self.button7.place(relx=0.01, rely=0.23, width=80, height=75)
        self.button7.configure(
            background=grey2,
            text='7',
            font=font1,
            command=self.btn7,
            cursor='hand2'
        )
        #button8
        self.button8 = tk.Button(self.top)
        self.button8.place(relx=0.26, rely=0.23, width=80, height=75)
        self.button8.configure(
            background=grey2,
            text='8',
            font=font1,
            command=self.btn8,
            cursor='hand2'
        )
        #button9
        self.button9 = tk.Button(self.top)
        self.button9.place(relx=0.51, rely=0.23, width=80, height=75)
        self.button9.configure(
            background=grey2,
            text='9',
            font=font1,
            command=self.btn9,
            cursor='hand2'
        )
        #buttonclear
        self.buttonc = tk.Button(self.top)
        self.buttonc.place(relx=0.76, rely=0.23, width=80, height=75)
        self.buttonc.configure(
            background=orange,
            text='C',
            font=font1,
            cursor='hand2',
            command=self.btnclear
        )
        
        #Linha 2
        
        #button4
        self.button4 = tk.Button(self.top)
        self.button4.place(relx=0.01, rely=0.42, width=80, height=75)
        self.button4.configure(
            background=grey2,
            text='4',
            font=font1,
            command=self.btn4,
            cursor='hand2'
        )
        #button5
        self.button5 = tk.Button(self.top)
        self.button5.place(relx=0.26, rely=0.42, width=80, height=75)
        self.button5.configure(
            background=grey2,
            text='5',
            font=font1,
            command= self.btn5,
            cursor='hand2'
        )
        #button6
        self.button6 = tk.Button(self.top)
        self.button6.place(relx=0.51, rely=0.42, width=80, height=75)
        self.button6.configure(
            background=grey2,
            text='6',
            font=font1,
            command=self.btn6,
            cursor='hand2'
        )
        #buttonadd
        self.buttonadd = tk.Button(self.top)
        self.buttonadd.place(relx=0.76, rely=0.42, width=80, height=75)
        self.buttonadd.configure(
            background=grey2,
            text='+',
            font=font1,
            cursor='hand2',
            command=self.btnadd
        )
        
        #Linha 3

        #button1
        self.button1 = tk.Button(self.top)
        self.button1.place(relx=0.01, rely=0.615, width=80, height=75)
        self.button1.configure(
            background=grey2,
            text='1',
            font=font1,
            command=self.btn1,
            cursor='hand2'
        )
        #button2
        self.button2 = tk.Button(self.top)
        self.button2.place(relx=0.26, rely=0.615, width=80, height=75)
        self.button2.configure(
            background=grey2,
            text='2',
            font=font1,
            command=self.btn2,
            cursor='hand2'
        )
        #button3
        self.button3 = tk.Button(self.top)
        self.button3.place(relx=0.51, rely=0.615, width=80, height=75)
        self.button3.configure(
            background=grey2,
            text='3',
            font=font1,
            command=self.btn3,
            cursor='hand2'
        )
        #buttonsub
        self.buttonsub = tk.Button(self.top)
        self.buttonsub.place(relx=0.76, rely=0.615, width=80, height=75)
        self.buttonsub.configure(
            background=grey2,
            text='-',
            font=font1,
            cursor='hand2',
            command=self.btnsub
        )
        
        #Linha 4
        
        #button0
        self.button0 = tk.Button(self.top)
        self.button0.place(relx=0.01, rely=0.81, width=80, height=75)
        self.button0.configure(
            background=grey2,
            text='0',
            font=font1,
            command=self.btn0,
            cursor='hand2'
        )
        #buttonmultp
        self.buttonmultp = tk.Button(self.top)
        self.buttonmultp.place(relx=0.26, rely=0.81, width=80, height=75)
        self.buttonmultp.configure(
            background=grey2,
            text='x',
            font=font1,
            cursor='hand2',
            command=self.btnmultp
        )
        #buttondivd
        self.buttondivd = tk.Button(self.top)
        self.buttondivd.place(relx=0.51, rely=0.81, width=80, height=75)
        self.buttondivd.configure(
            background=grey2,
            text='/',
            font=font1,
            cursor='hand2',
            command=self.btndivd
        )
        #buttonsend
        self.buttonsend = tk.Button(self.top)
        self.buttonsend.place(relx=0.76, rely=0.81, width=80, height=75)
        self.buttonsend.configure(
            background=cyan,
            text='=',
            font=font1,
            cursor='hand2',
            command=self.btsend
        )
        
        # self.result = 0
        
        self.top.mainloop()
     

    def btn7(self):
        self.entry.insert(END, 7)
            
            
    def btn8(self):
        self.entry.insert(END, 8)
            
            
    def btn9(self):
        self.entry.insert(END, 9)
            
            
    def btnclear(self):
        self.entry.delete(0, END)
        self.entry.insert(0, '')
            
            
    def btn4(self):
        self.entry.insert(END, 4)
            
            
    def btn5(self):
        self.entry.insert(END, 5)
            
            
    def btn6(self):
        self.entry.insert(END, 6)
            
            
    def btnadd(self):
        self.entry.insert(END, "+")
        

    def btn1(self):
        self.entry.insert(END, 1)
            
            
    def btn2(self):
        self.entry.insert(END, 2)
            
            
    def btn3(self):
        self.entry.insert(END, 3)
            
            
    def btnsub(self):
        self.entry.insert(END, "-")
        
        
    def btn0(self):
        self.entry.insert(END, 0)
            
            
    def btnmultp(self):
        self.entry.insert(END, "*")
        
        
    def btndivd(self):
        self.entry.insert(END, "/")
        
        
    def btsend(self):
        r = self.entry.get() 
        result = str(eval(r)) 
        self.entry.delete(0, END)
        self.entry.insert(0, result)


if __name__ == "__main__":
    TopLevel()
