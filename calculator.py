##Ali Raeisdanaei## 


from tkinter import*
import math


root = Tk()
root.title("Calculator")

result = StringVar()
result.set("0")


output = Entry(root,   width=30, borderwidth=5,
               textvariable=result, font="Courier 15 bold", justify="right", state=DISABLED)
output.grid(row=0, column=0, columnspan=4, padx=10, pady=30)

# variabels that will be used
num1 = "empty"
num2 = "empty"
op = "empty"


def clear():
    print("clear")
    global num1, num2, op
    if(num2 != "empty"):
        num2 = "empty"
        result.set("0")
    elif(num1 == "empty" and op == "empty" and output.get() != ""):
        # can only clear the first int if there is no operation
        num1 = "empty"
        result.set("0")

    print("clear-- num1: " + str(num1) + " num2: " +
          str(num2) + " output: " + output.get())


def allClear():
    print("all clear")
    global num1, num2, op
    num1 = "empty"
    num2 = "empty"
    op = "empty"
    result.set("0")
    print("allClear-- num1: " + str(num1) + " num2: " +
          str(num2) + " output: " + output.get())


def increm_num(digit):
    print("digit: " + str(digit))
    global num1, num2

    if(num1 != "empty" and num2 == "empty"):
        print("here")
        result.set("0")
    if(num1 == "empty"and op != "empty" and digit != "+/-"):
        print("gel")
        # a number is still left on the screen from the previous calculation
        # hence there is still a value for the operation
        # we cannot increment onto the value on the screen except for when there is a sign change request
        result.set("0")

    # adds the numbers to the screen
    if(digit == "+/-"):
        print("change sign" + output.get())
        tmp_float = float(output.get()) * -1.0

        print("tmp_float " + str(tmp_float))

        if(tmp_float % 1 < 0.000000001):
            result.set(str(int(tmp_float)))
        else:
            result.set(str(tmp_float))

    elif(output.get() == "0" and digit != "."):
        result.set(digit)
    else:

        result.set(output.get() + digit)
    if(num1 != "empty"):
        num2 = float(output.get())

    print("increm_num-- num1: " + str(num1) + " num2: " +
          str(num2) + " output: " + output.get())


def setOperation(operation):
    global num1, num2, op

    if(operation == "+"):
        print("add")
        op = "+"
    elif(operation == "-"):
        print("sub")
        op = "-"
    elif(operation == "/"):
        print("div")
        op = "/"
    elif(operation == "*"):
        print("mul")
        op = "*"
    if(operation == "sqrt"):
        print("sqrt")
        op = "sqrt"
        # immediately calculates the sqrt
        calculate()
    if(op != "sqrt"):
        if(num1 == "empty"):
            num1 = float(output.get())
        if(num2 != "empty"):
            calculate()
            setOperation(op)

    print("setOpetaion-- num1: " + str(num1) + " num2: " +
          str(num2) + " output: " + output.get())


def calculate():
    global op, num1, num2
    crnt_result = 0
    if((op != "empty" and num1 != "empty" and num2 != "empty") or op == "sqrt"):
        if(op == "+"):
            print("add equal")
            crnt_result = num1 + num2
        elif(op == "-"):
            print("sub equal")
            crnt_result = num1 - num2
        elif(op == "/"):
            print("div equal")
            crnt_result = num1 / num2
        elif(op == "*"):
            print("mul equal")
            crnt_result = num1 * num2
        elif(op == "sqrt"):
            print("sqrt")
            # will sqrt whatever is on output
            crnt_result = math.sqrt(float(output.get()))

        # sets the result to the least needed decimal places
        if(crnt_result % 1 < 0.000000001):
            result.set(str(int(crnt_result)))
        else:
            result.set(str(crnt_result))

        num1 = "empty"
        num2 = "empty"

    print("calculate-- num1: " + str(num1) + " num2: " +
          str(num2) + " output: " + output.get())


# defining buttons
button_0 = Button(root,  text="0", width=1, padx=40, pady=20,
                  command=lambda: increm_num("0"))
button_1 = Button(root, text="1", width=1, padx=40, pady=20,
                  command=lambda: increm_num("1"))
button_2 = Button(root, text="2", width=1, padx=40, pady=20,
                  command=lambda: increm_num("2"))
button_3 = Button(root, text="3", width=1, padx=40, pady=20,
                  command=lambda: increm_num("3"))
button_4 = Button(root, text="4", width=1, padx=40, pady=20,
                  command=lambda: increm_num("4"))
button_5 = Button(root, text="5", width=1, padx=40, pady=20,
                  command=lambda: increm_num("5"))
button_6 = Button(root, text="6", width=1, padx=40, pady=20,
                  command=lambda: increm_num("6"))
button_7 = Button(root, text="7", width=1, padx=40, pady=20,
                  command=lambda: increm_num("7"))
button_8 = Button(root, text="8", width=1, padx=40, pady=20,
                  command=lambda: increm_num("8"))
button_9 = Button(root, text="9", width=1, padx=40, pady=20,
                  command=lambda: increm_num("9"))

button_deci = Button(root, width=1, text=".", padx=40,
                     pady=20, command=lambda: increm_num("."))
button_sgn = Button(root, width=1, text="+/-", padx=40,
                    pady=20, command=lambda: increm_num("+/-"))

button_add = Button(root, width=1, text="+", padx=40,
                    pady=20, command=lambda: setOperation("+"))
button_sub = Button(root, width=1, text="-", padx=40,
                    pady=20, command=lambda: setOperation("-"))
button_mul = Button(root, width=1, text="*", padx=40,
                    pady=20, command=lambda: setOperation("*"))
button_div = Button(root, width=1, text="/", padx=40,
                    pady=20, command=lambda: setOperation("/"))
button_sqrt = Button(root, width=1, text="sqrt", padx=40,
                     pady=20, command=lambda: setOperation("sqrt"))
button_equ = Button(root, width=1, text="=", padx=40,
                    pady=20, command=calculate)

button_clr = Button(root, fg="red", width=1, text="C",
                    padx=40, pady=20, command=clear)
button_Aclr = Button(root, fg="red", width=1, text="AC",
                     padx=40, pady=20, command=allClear)

# put buttons on screen
# based on the order of normal calculators
button_clr.grid(row=1, column=0)
button_Aclr.grid(row=1, column=1)
button_sqrt.grid(row=1, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_0.grid(row=5, column=0)
button_deci.grid(row=5, column=1)

button_equ.grid(row=5, column=2)

button_sgn.grid(row=1, column=3)
button_div.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_sub.grid(row=4, column=3)
button_add.grid(row=5, column=3)

root.mainloop()
