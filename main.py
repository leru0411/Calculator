from tkinter import *
cal = Tk()

def add_num(num):
    value = fild.get()
    if value[0] == '0':
        value = value[1:]
    fild.delete(0, END)
    fild.insert(0, value + num)

def add_operation(op):
    value = fild.get()
    if value[-1] in '+-/*.C()CE':
        value = value[:-1]
    fild.delete(0, END)
    fild.insert(0, value + op)

def calculate():
    value = fild.get()
    fild.delete(0, END)
    fild.insert(0, eval(value))

def delete_1_num():
    value = len(fild.get())-1
    count = len(str(fild.get()))
    while count > 0:
        fild.delete(value, END)
        count -= 1
        return delete_1_num
    fild.insert(0,0)

def delete_num():
    fild.delete(0, END)
    fild.insert(0,0)

def press_digit(num):
    return Button(text = num, bg = '#0A0A0A', fg = 'white', command=lambda: add_num(num), font=('Arial', 20))

def press_operation(op):
    return Button(text = op, bg = '#2A2A2A', fg = 'white',command=lambda: add_operation(op), font=('Arial', 20))

def press_calc(op):
    return Button(text = op, bg = '#950042', fg = 'white',command=calculate, font=('Arial', 20))

def delete_symb(op):
    return Button(text = op, bg = '#950042', fg = 'white',command=delete_num, font=('Arial', 20))

def delete_1_symb(op):
    return Button(text = op, bg = '#2A2A2A', fg = 'white',command=delete_1_num, font=('Arial', 20))

cal.title('Калькулятор')
cal.geometry('405x530')


fild = Entry(width=50, justify=RIGHT, font=('Arial', 11, 'bold'), fg='white', bg='#505050')
fild.grid(row=0, columnspan=4, stick='we')
fild.insert(0,'0')


delete_symb("CE").grid(row=1, column=0, stick='wens', padx='0.1',pady='0.1')
press_operation("(").grid(row=1, column=1, stick='wens', padx='0.1',pady='0.1')
press_operation(")").grid(row=1, column=2, stick='wens', padx='0.1',pady='0.1')
delete_1_symb("C").grid(row=1, column=3, stick='wens', padx='0.1',pady='0.1')

press_digit('1').grid(row=2, column=0, stick='wens', padx='0.1',pady='0.1')
press_digit('2').grid(row=2, column=1, stick='wens', padx='0.1',pady='0.1')
press_digit('3').grid(row=2, column=2, stick='wens', padx='0.1',pady='0.1')
press_digit('4').grid(row=3, column=0, stick='wens', padx='0.1',pady='0.1')
press_digit('5').grid(row=3, column=1, stick='wens', padx='0.1',pady='0.1')
press_digit('6').grid(row=3, column=2, stick='wens', padx='0.1',pady='0.1')
press_digit('7').grid(row=4, column=0, stick='wens', padx='0.1',pady='0.1')
press_digit('8').grid(row=4, column=1, stick='wens', padx='0.1',pady='0.1')
press_digit('9').grid(row=4, column=2, stick='wens', padx='0.1',pady='0.1')
press_digit('0').grid(row=5, column=1, stick='wens', padx='0.1',pady='0.1')
press_operation("+").grid(row=2, column=3, stick='wens', padx='0.1',pady='0.1')
press_operation("-").grid(row=3, column=3, stick='wens', padx='0.1',pady='0.1')
press_operation("*").grid(row=4, column=3, stick='wens', padx='0.1',pady='0.1')
press_operation("/").grid(row=5, column=3, stick='wens', padx='0.1',pady='0.1')
press_operation(".").grid(row=5, column=0, stick='wens', padx='0.1',pady='0.1')
press_calc("=").grid(row=5, column=2, stick='wens', padx='0.1',pady='0.1')


cal.grid_columnconfigure(0, minsize=100)
cal.grid_columnconfigure(1, minsize=100)
cal.grid_columnconfigure(2, minsize=100)
cal.grid_columnconfigure(3, minsize=100)
cal.grid_columnconfigure(4, minsize=100)

cal.grid_rowconfigure(1, minsize=100)
cal.grid_rowconfigure(2, minsize=100)
cal.grid_rowconfigure(3, minsize=100)
cal.grid_rowconfigure(4, minsize=100)
cal.grid_rowconfigure(5, minsize=100)

cal.mainloop()
