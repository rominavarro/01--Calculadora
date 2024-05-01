#import TKinter library

from tkinter import *
from tkinter import ttk
import math

#Make Functions
#Dark Theme Function
def DarkTheme(*args):
    style.configure('mainframe.TFrame', background="#010924")

    style_label1.configure('Label1.TLabel', background="#010924", foreground="white")
    style_label2.configure('Label2.TLabel', background="#010924", foreground="white")

    style_button_num.configure('Button_Num.TButton', background="#00044A", foreground="white")
    style_button_num.map('Button_Num.TButton', background=[('active', '#000AB1')])

    style_button_erase.configure('Button_Eraser.TButton', background="#010924", foreground="white")
    style_button_erase.map('Button_Eraser.TButton', background=[('active', '#000AB1')])

    style_button_left.configure('Button_left.TButton', background="#010924", foreground="white")
    style_button_left.map('Button_left.TButton', background=[('active', '#000AB1')])


#Light Theme Function
def LightTheme(*args):
    style.configure('mainframe.TFrame', background="#DBDBDB", foreground="black")

    style_label1.configure('Label1.TLabel', background="#DBDBDB", foreground="black")
    style_label2.configure('Label2.TLabel', background="#DBDBDB", foreground="black")

    style_button_num.configure('Button_Num.TButton', background="#FFFFFF", foreground="black")
    style_button_num.map('Button_Num.TButton', background=[('active', '#008080')])
    
    style_button_erase.configure('Button_Eraser.TButton', background="#CECECE", foreground="black")
    style_button_erase.map('Button_Eraser.TButton', background=[('active', '#858585')])
    
    style_button_left.configure('Button_left.TButton', background="#CECECE", foreground="black")
    style_button_left.map('Button_left.TButton', background=[('active', '#858585')])

#Input Data Function
def InputData(key):
    if key >= '0' and key <= '9' or key == '(' or key == ')' or key == '.':
        input2.set(input2.get() + key)
    
    if key == '*' or key == '/' or key == '+' or key == '-':
        if key == '*':
            input1.set(input2.get() + '*')
        elif key == '/':
            input1.set(input2.get() + '/')
        elif key == '+':
            input1.set(input2.get() + '+')
        elif key == "-":
            input1.set(input2.get() + '-')
        
        input2.set('')
    
    if key == '=':
        input1.set(input1.get() + input2.get())
        result = eval(input1.get())
        input2.set(result)

#Input Data from Keyboard Function
def InputDataKeyboard(event):
     key = event.char
     print(event)

     if key >= '0' and key <= '9' or key == '(' or key == ')' or key == '.':
        input2.set(input2.get() + key)
    
     if key == '*' or key == '/' or key == '+' or key == '-':
        if key == '*':
            input1.set(input2.get() + '*')
        elif key == '/':
            input1.set(input2.get() + '/')
        elif key == '+':
            input1.set(input2.get() + '+')
        elif key == "-":
            input1.set(input2.get() + '-')
        
        input2.set('')
    
     if key == '=':
        input1.set(input1.get() + input2.get())
        result = eval(input1.get())
        input2.set(result)

#Square Root Function
def SquareRoot():
    input1.set('')
    result = math.sqrt(float(input2.get()))
    input2.set(result)

#Erase Function
def Erase(*args):
    start = 0
    end = len(input2.get())

    input2.set(input2.get()[start:end-1])

#Erase All Function
def EraseAll(*args):
    input1.set('')
    input2.set('')


#Stablish root
root = Tk()
root.title("Romi's Calculator")
root.geometry("+500+80")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#Stablish Style for mainframe, columns and rows
style = ttk.Style()
style.configure('mainframe.TFrame', background="#DBDBDB")
style.theme_use('clam')
style.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

#Style of labels
style_label1 = ttk.Style()
style_label1.configure('Label1.TLabel', font="consolas 15", anchor="E")

style_label2 = ttk.Style()
style_label2.configure('Label2.TLabel', font="consolas 40", anchor="E")

#Style of Buttons
style_button_num = ttk.Style()
style_button_num.configure('Button_Num.TButton', font="consolas 22", width=5, background="#FFFFFF", relief="flat")
style_button_num.map('Button_Num.TButton', background=[('active', '#B9B9B9')])


style_button_erase = ttk.Style()
style_button_erase.configure('Button_Eraser.TButton', font="consolas 22", width=5, background="#CECECE", relief="flat")
style_button_erase.map('Button_Eraser.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

style_button_left = ttk.Style()
style_button_left.configure('Button_left.TButton', font="consolas 22", width=5, background="#CECECE", relief="flat")
style_button_left.map('Button_left.TButton', background=[('active', '#858585')])


#Input Numbers of Calculator
input1 = StringVar()
label_input1 = ttk.Label(mainframe, textvariable=input1, style="Label1.TLabel")
label_input1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

input2 = StringVar()
label_input2 = ttk.Label(mainframe, textvariable=input2, style="Label2.TLabel")
label_input2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))


#Numbers Buttons
button0 = ttk.Button(mainframe, text="0", style="Button_Num.TButton", command=lambda: InputData('0'))
button1 = ttk.Button(mainframe, text="1", style="Button_Num.TButton", command=lambda: InputData('1'))
button2 = ttk.Button(mainframe, text="2", style="Button_Num.TButton", command=lambda: InputData('2'))
button3 = ttk.Button(mainframe, text="3", style="Button_Num.TButton", command=lambda: InputData('3'))
button4 = ttk.Button(mainframe, text="4", style="Button_Num.TButton", command=lambda: InputData('4'))
button5 = ttk.Button(mainframe, text="5", style="Button_Num.TButton", command=lambda: InputData('5'))
button6 = ttk.Button(mainframe, text="6", style="Button_Num.TButton", command=lambda: InputData('6'))
button7 = ttk.Button(mainframe, text="7", style="Button_Num.TButton", command=lambda: InputData('7'))
button8 = ttk.Button(mainframe, text="8", style="Button_Num.TButton", command=lambda: InputData('8'))
button9 = ttk.Button(mainframe, text="9", style="Button_Num.TButton", command=lambda: InputData('9'))

button_erase = ttk.Button(mainframe, text=chr(9003), style="Button_Eraser.TButton", command=lambda: Erase())
button_erase_all = ttk.Button(mainframe, text="C", style="Button_Eraser.TButton", command=lambda: EraseAll())
button_parentheses1 = ttk.Button(mainframe, text="(", style="Button_left.TButton", command=lambda: InputData('('))
button_parentheses2 = ttk.Button(mainframe, text=")", style="Button_left.TButton", command=lambda: InputData(')'))
button_dot = ttk.Button(mainframe, text=".", style="Button_left.TButton", command=lambda: InputData('.'))

#Funcionality Buttons
button_divide = ttk.Button(mainframe, text=chr(247), style="Button_left.TButton", command=lambda: InputData('/')) 
button_multiply = ttk.Button(mainframe, text="*", style="Button_left.TButton", command=lambda: InputData('*'))
button_add = ttk.Button(mainframe, text="+", style="Button_left.TButton", command=lambda: InputData('+'))
button_substract = ttk.Button(mainframe, text="-", style="Button_left.TButton", command=lambda: InputData('-'))
button_equal = ttk.Button(mainframe, text="=", style="Button_left.TButton", command=lambda: InputData('='))
button_squareroot = ttk.Button(mainframe, text="√", style="Button_left.TButton", command=lambda: SquareRoot())

#Put Buttons on Screen
button_parentheses1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentheses2.grid(column=1, row=2, sticky=(W, N, E, S))
button_erase_all.grid(column=2, row=2, sticky=(W, N, E, S))
button_erase.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_divide.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiply.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_add.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_dot.grid(column=2, row=6, sticky=(W, N, E, S))
button_substract.grid(column=3, row=6, sticky=(W, N, E, S))

button_equal.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_squareroot.grid(column=3, row=7, sticky=(W, N, E, S))

#Configuration of Spacing between buttons
for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)


root.bind('<KeyPress-l>', LightTheme)
root.bind('<KeyPress-d>', DarkTheme)
root.bind('<KeyPress-e>', Erase)
root.bind('<KeyPress-r>', EraseAll)
root.bind('<Key>', InputDataKeyboard)


root.mainloop()