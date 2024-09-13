import tkinter as tk
from tkinter import messagebox

class My_calculaotor:
    def __init__(self, root):
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to Quit"):
            self.root.destroy()

calculation = ""

def add_to_calculation(symbol):
    global calculation
    if symbol == "x":
        calculation += "*"
    elif symbol == "÷":
        calculation += "/"
    else:    
        calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try: 
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_feild()  
        text_result.insert(1.0, "Error")

def clear_feild():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title("Calculator")
#root.geometry('400x500')

My_calculaotor = My_calculaotor(root)

text_result = tk.Text(root, height=2, width=16, font=('Arial', 20))
text_result.grid(columnspan=5)

button_bg = "lightblue"
button_fg = "black"
operator_bg = "lightgreen"  #Operator color
#button color bg and fg
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=('Arial', 14),bg=button_bg, fg=button_fg)
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=('Arial', 14), bg=operator_bg, fg=button_fg)
btn_plus.grid(row=2, column=4)
btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=('Arial', 14), bg=operator_bg, fg=button_fg)
btn_subtract.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="x", command=lambda: add_to_calculation("x"), width=5, font=('Arial', 14), bg=operator_bg, fg=button_fg)
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="÷", command=lambda: add_to_calculation("÷"), width=5, font=('Arial', 14), bg=operator_bg, fg=button_fg)
btn_divide.grid(row=5, column=4)

btn_percentage = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_percentage.grid(row=5, column=1)
btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=('Arial', 14), bg=button_bg, fg=button_fg)
btn_decimal.grid(row=5, column=3)

btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=('Arial', 14), bg="orange", fg="black")
btn_equal.grid(row=6, column=3, columnspan=2)
btn_clear = tk.Button(root, text="C", command=clear_feild, width=11, font=('Arial', 14), bg="red", fg="white")
btn_clear.grid(row=6, column=1, columnspan=2)


root.mainloop()