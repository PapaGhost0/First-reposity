import tkinter as tk


def add_digit(digit):                        #функция для ввода числе
    value = calc.get()
    if value[0] == "0" and len(value)==1:
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)
def add_operation(operation):               #функция для замены оперций
    value = calc.get()
    if value[-1] in "+-/*":
             value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value + operation)
def calculate():                            #функция для арифметических вычислений(eval)
    value = calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,eval(value))
def clear():                                #функция для очистки строки ввода
    calc.delete(0,tk.END)
    calc.insert(0,0)


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Times New Roman", 14), command=lambda: add_digit(digit))              #функция настройки кнопок цифр(1234)
def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("Times New Roman", 14), command=lambda: add_operation(operation))  #функция настройки кнопок операций(+-*/)
def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Times New Roman", 14), command=calculate)                         #функция настройки кнопки "="
def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Times New Roman", 14), command=clear)                             #функция настройки кнопи "C"


win = tk.Tk()                    #создание окна для калькулятора
win.geometry(f"180x250+100+200") #задаем размер окна
win["bg"] = "grey"               #задаем цвет фона
win.title("Калькулятор")         #задаем имя заоловока


calc = tk.Entry(win, justify=tk.RIGHT, font=("Times New Roman", 14),width=14) #ввод значения justify(ввод с одной из сторон), font(настройка шрифта)
calc.insert(0,"0")                                                            #начало работы с "0"
calc.grid(row=0, column=0, columnspan=4, stick="we")                          #задаем значения row(столбец), column(строке), сolumnspam(макс.колич.строк), stick(ввод данных с востока на запад)


make_digit_button("1").grid(row=1, column = 0, stick="wens", padx=5, pady=5)  #задаем значение кнопкам цифр
make_digit_button("2").grid(row=1, column = 1, stick="wens", padx=5, pady=5)
make_digit_button("3").grid(row=1, column = 2, stick="wens", padx=5, pady=5)
make_digit_button("4").grid(row=2, column = 0, stick="wens", padx=5, pady=5)
make_digit_button("5").grid(row=2, column = 1, stick="wens", padx=5, pady=5)
make_digit_button("6").grid(row=2, column = 2, stick="wens", padx=5, pady=5)
make_digit_button("7").grid(row=3, column = 0, stick="wens", padx=5, pady=5)
make_digit_button("8").grid(row=3, column = 1, stick="wens", padx=5, pady=5)
make_digit_button("9").grid(row=3, column = 2, stick="wens", padx=5, pady=5)
make_digit_button("0").grid(row=4, column = 0, stick="wens", padx=5, pady=5)

make_operation_button("+").grid(row=1, column = 3, stick="wens", padx=5, pady=5) #задаем значения кнопкам операций
make_operation_button("-").grid(row=2, column = 3, stick="wens", padx=5, pady=5)
make_operation_button("*").grid(row=3, column = 3, stick="wens", padx=5, pady=5)
make_operation_button("/").grid(row=4, column = 3, stick="wens", padx=5, pady=5)

make_calc_button("=").grid(row=4, column = 2, stick="wens", padx=5, pady=5)      #задаем значения кнопкам "=", "C"
make_clear_button("C").grid(row=4, column = 1, stick="wens", padx=5, pady=5)

win.mainloop()
