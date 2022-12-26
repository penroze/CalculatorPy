from tkinter import *

# Calc window

window = Tk()
window.title('Калькулятор')
window.geometry('360x500+540+360')
window.resizable(False, False)

# Varies

point_count = 0
operand1 = ''
operand2 = ''
value1 = ''
value2 = ''
equal = 0
memory = ''

# Main functions

def input_into_entry(symbol):
    if entry.get() == '0' or entry.get() == '':
        entry.delete(0, END)
        entry.insert(END, symbol)
    else:
        entry.insert(END, symbol)


def input_point(symbol):
    global point_count
    if point_count == 0 and entry.get() == '':
        point_count = point_count + 1
        entry.insert(END, '0' + symbol)
    elif point_count == 0:
        point_count = point_count + 1
        entry.insert(END, symbol)

def plus_minus():
    if entry.get() != '0':
        if float(entry.get()) > 0:
            entry.insert(0, '-')
        else:
            entry.delete(0)

def clear():
    global value1
    global value2
    global operand1
    global point_count
    global operand2
    point_count = 0
    value1 = ''
    value2 = ''
    operand1 = ''
    operand2 = ''
    entry.delete(0, END)
    entry.insert(END, 0)

def Operand(symbol):
    global operand1
    global value1
    global point_count
    value1 = entry.get()
    operand1 = symbol
    point_count = 0
    entry.delete(0, END)

def Equal():
    global operand1
    global operand2
    global value1
    global value2
    global equal
    global point_count

    if operand1 != operand2:
        value2 = entry.get()

    if value2 == '':
        value2 = entry.get()

    point_count = 0
    entry.delete(0, END)

    if operand1 == '+':
        equal = float(value1) + float(value2)

    if operand1 == '-':
        equal = float(value1) - float(value2)

    if operand1 == '/':
        if value2 == '0':
            equal = '∞'
        else:
            equal = float(value1) / float(value2)

    if operand1 == '*':
        equal = float(value1) * float(value2)

    operand2 = operand1
    value1 = equal

    if equal % 1 == 0:
        equal = int(equal)
        equal = str(equal)
        entry.insert(END, equal)
    else:
        entry.insert(END, equal)

# Memory

def memory_save():
    global memory
    memory = entry.get()

def memory_read():
    global memory
    entry.delete(0, END)
    entry.insert(END, memory)

def memory_plus():
    global memory
    memory = float(memory) + float(entry.get())

def memory_minus():
    global memory
    memory = float(memory) - float(entry.get())

def memory_clear():
    global memory
    entry.delete(0, END)
    memory = ''
    entry.insert(END, 0)


# interface

entry = Entry(window, width=360, font=('', 48), bg='#202020',fg='#FFFFFF')
entry.place(x=0, y=0, height=90)

entry.insert(END, 0)

# buttons

btn1 = Button(window, bg='#3b3b3b', fg='white', text = '1', command = lambda: input_into_entry('1'))
btn1.place(x=0, y=320, width=90, height=90)

btn2 = Button(window, bg='#3b3b3b', fg='white', text = '2', command = lambda: input_into_entry('2'))
btn2.place(x=90, y=320, width=90, height=90)

btn3 = Button(window, bg='#3b3b3b', fg='white', text = '3', command = lambda: input_into_entry('3'))
btn3.place(x=180, y=320, width=90, height=90)

btn4 = Button(window, bg='#3b3b3b', fg='white', text = '4', command = lambda: input_into_entry('4'))
btn4.place(x=0, y=230, width=90, height=90)

btn5 = Button(window, bg='#3b3b3b', fg='white', text = '5', command = lambda: input_into_entry('5'))
btn5.place(x=90, y=230, width=90, height=90)

btn6 = Button(window, bg='#3b3b3b', fg='white', text = '6', command = lambda: input_into_entry('6'))
btn6.place(x=180, y=230, width=90, height=90)

btn7 = Button(window, bg='#3b3b3b', fg='white', text = '7', command = lambda: input_into_entry('7'))
btn7.place(x=0, y=140, width=90, height=90)

btn8 = Button(window, bg='#3b3b3b', fg='white', text = '8', command = lambda: input_into_entry('8'))
btn8.place(x=90, y=140, width=90, height=90)

btn9 = Button(window, bg='#3b3b3b', fg='white', text = '9', command = lambda: input_into_entry('9'))
btn9.place(x=180, y=140, width=90, height=90)

btn0 = Button(window, bg='#3b3b3b', fg='white', text = '0', command = lambda: input_into_entry('0'))
btn0.place(x=90, y=410, width=90, height=90)

# memory btns

btn_ms = Button(window, bg='#323232', fg='white', text = 'MS', command = memory_save)
btn_ms.place(x=288, y=90, width=72, height=50)

btn_mm = Button(window, bg='#323232', fg='white', text = 'M-', command = memory_minus)
btn_mm.place(x=216, y=90, width=72, height=50)

btn_mp = Button(window, bg='#323232', fg='white', text = 'M+', command = memory_plus)
btn_mp.place(x=144, y=90, width=72, height=50)

btn_mr = Button(window, bg='#323232', fg='white', text = 'MR', command = memory_read)
btn_mr.place(x=72, y=90, width=72, height=50)

btn_mc = Button(window, bg='#323232', fg='white', text = 'MC', command = memory_clear)
btn_mc.place(x=0, y=90, width=72, height=50)

# operand btns

btn_clear = Button(window, bg='#323232', fg='white', text = 'C', command = clear)
btn_clear.place(x=270, y=140, width=90, height=90)

btn_div = Button(window, bg='#323232', fg='white', text = '÷', command = lambda: Operand('/'))
btn_div.place(x=270, y=230, width=90, height=45)

btn_mul = Button(window, bg='#323232', fg='white', text = '×', command = lambda: Operand('*'))
btn_mul.place(x=270, y=275, width=90, height=45)

btn_minus = Button(window, bg='#323232', fg='white', text = '-', command = lambda: Operand('-'))
btn_minus.place(x=270, y=320, width=90, height=45)

btn_plus = Button(window, bg='#323232', fg='white', text = '+', command = lambda: Operand('+'))
btn_plus.place(x=270, y=365, width=90, height=45)

btn_equal = Button(window, bg='#7cd6f5', fg='#233c44', text = '=', command = Equal)
btn_equal.place(x=270, y=410, width=90, height=90)

btn_plusMinus = Button(window, bg='#3b3b3b', fg='white', text = '+/-', command = plus_minus)
btn_plusMinus.place(x=0, y=410, width=90, height=90)

btn_plusMinus = Button(window, bg='#3b3b3b', fg='white', text = '.', command = lambda: input_point('.'))
btn_plusMinus.place(x=180, y=410, width=90, height=90)



window.mainloop()


