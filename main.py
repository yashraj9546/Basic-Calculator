import tkinter as tk
from tkinter import*
calculation =""

def add_to_calculation(symbol):
     global calculation
     calculation += str(symbol)
     text_result.delete(1.0, "end")
     text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"ERROR")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root= tk.Tk()

root.title("CALCULATOR")

text_result = tk.Text(root, height=2 , width=16 , font=("Arial,18") )
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda:add_to_calculation(1), width=5 )
btn_1.grid(row=2, column=0)

btn_2 = tk.Button(root, text="2", command=lambda:add_to_calculation(2), width=5 )
btn_2.grid(row=2, column=1)

btn_3 = tk.Button(root, text="3", command=lambda:add_to_calculation(3),width=5 )
btn_3.grid(row=2, column=2)

btn_4 = tk.Button(root, text="4", command=lambda:add_to_calculation(4),width=5 )
btn_4.grid(row=3, column=0)

btn_5 = tk.Button(root, text="5", command=lambda:add_to_calculation(5),width=5 )
btn_5.grid(row=3, column=1)

btn_6 = tk.Button(root, text="6", command=lambda:add_to_calculation(6),width=5 )
btn_6.grid(row=3, column=2)

btn_7 = tk.Button(root, text="7", command=lambda:add_to_calculation(7),width=5 )
btn_7.grid(row=4, column=0)

btn_8 = tk.Button(root, text="8", command=lambda:add_to_calculation(8),width=5 )
btn_8.grid(row=4, column=1)

btn_9 = tk.Button(root, text="9", command=lambda:add_to_calculation(9),width=5 )
btn_9.grid(row=4, column=2)

btn_0 = tk.Button(root, text="0", command=lambda:add_to_calculation(0),width=5 )
btn_0.grid(row=5, column=1)

btn_plus = tk.Button(root, text="+", command=lambda:add_to_calculation("+"),width=5 )
btn_plus.grid(row=2, column=3)

btn_minus= tk.Button(root, text="-", command=lambda:add_to_calculation("-"),width=5 )
btn_minus.grid(row=3, column=3)

btn_mul= tk.Button(root, text="*", command=lambda:add_to_calculation("*"),width=5 )
btn_mul.grid(row=4, column=3)

btn_div = tk.Button(root, text="/", command=lambda:add_to_calculation("/"),width=5 )
btn_div.grid(row=5, column=3)

btn_eql= tk.Button(root, text="=", command=evaluate_calculation ,width=5 )
btn_eql.grid(row=5, column=2)

btn_clr = tk.Button(root, text="clear", command=clear_field ,width=5 )
btn_clr.grid(row=5, column=0)


root.mainloop()
