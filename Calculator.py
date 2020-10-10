from tkinter import *

root=Tk()

root.title("Calculator")
e=Entry(root, width=35, border=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


# 0=add
# 1=subtract
# 2=multiply
# 3=divide



def myclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))


def button_clear_func():
    e.delete(0, END)


def button_add_func():
    num1= e.get()
    global f_num
    global operation
    operation = 0
    f_num =int(num1)
    e.delete(0,END)
    
def button_equal_fun():
    num2=e.get()
    e.delete(0, END)

    if operation==0:
         e.insert(0, f_num+int(num2))
    
    if operation==1:
         e.insert(0, f_num-int(num2))
    
    if operation==2:
         e.insert(0, f_num*int(num2))
    
    if operation==3:
         e.insert(0, f_num/int(num2))
   


def button_subtract_func():
    num1= e.get()
    global f_num
    global operation
    operation = 1
    f_num =int(num1)
    e.delete(0,END)

def button_multiply_func():
    num1= e.get()
    global f_num
    global operation
    operation = 2
    f_num =int(num1)
    e.delete(0,END)


def button_divide_func():
    num1= e.get()
    global f_num
    global operation
    operation = 3
    f_num =int(num1)
    e.delete(0,END)

# Buttons

Button1 = Button(root, text="7", padx=40, pady=20, command=lambda: myclick(7) )
Button1.grid()

Button2 = Button(root, text="8", padx=40, pady=20, command=lambda: myclick(8))
Button2.grid(row=1,column=1)

Button3 = Button(root, text="9", padx=40, pady=20, command=lambda: myclick(9))
Button3.grid(row=1, column=2)

Button4 = Button(root, text="4", padx=40, pady=20 , command=lambda: myclick(4))
Button4.grid(row=2, column=0)

Button5 = Button(root, text="5", padx=40, pady=20, command=lambda: myclick(5))
Button5.grid(row=2, column=1)

Button6 = Button(root, text="6", padx=40, pady=20, command=lambda: myclick(6))
Button6.grid(row=2, column=2)

Button7 = Button(root, text="1", padx=40, pady=20, command=lambda: myclick(1))
Button7.grid(row=3, column=0)

Button8 = Button(root, text="2", padx=40, pady=20, command=lambda: myclick(2))
Button8.grid(row=3, column=1)

Button9 = Button(root, text="3", padx=40, pady=20, command=lambda: myclick(3))
Button9.grid(row=3, column=2)

Button10 = Button(root, text="0", padx=40, pady=20, command=lambda: myclick(0))
Button10.grid(row=4, column=0)

button_Add = Button(root, text="+" , padx=39, pady=20, command=button_add_func)
button_Add.grid(row=5, column=0)


button_multiply=Button(root, text="*", padx=88, pady=20, command=button_multiply_func)
button_multiply.grid(row=5, column=1 , columnspan=2)


button_clear = Button(root, text="Clear", padx=77, pady=20, command=button_clear_func)
button_clear.grid(row=4, column=1, columnspan=2)


button_divide =Button(root, text="/ " , padx=40, pady=20, command=button_divide_func)
button_divide.grid(row=1, column=3)

button_subtract = Button(root, text="- ", padx=40, pady=20, command=button_subtract_func)
button_subtract.grid(row=2,column=3)

button_equal = Button(root, text="=", padx=39, pady=85, command=button_equal_fun)
button_equal.grid(row=3,column=3, rowspan=3)






root.mainloop()









