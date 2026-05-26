
import tkinter as tk
import math

try:
    import sympy as sp
    sympy_available = True
except:
    sympy_available = False


window = tk.Tk()

window.title("Ultra Scientific Calculator")

window.geometry("550x750")

window.configure(bg="#1e1e1e")

window.resizable(False, False)



equation = tk.StringVar()

expression = ""



def press(value):

    global expression

    expression += str(value)

    equation.set(expression)

def clear():

    global expression

    expression = ""

    equation.set("")

def backspace():

    global expression

    expression = expression[:-1]

    equation.set(expression)



def calculate():

    global expression

    try:

        expr = expression
        expr = expr.replace("^", "**")
        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("ln", "math.log")
        expr = expr.replace("fact", "math.factorial")
        result = str(eval(expr))
        equation.set(result)
        expression = result

    except ZeroDivisionError:

        equation.set("Cannot divide by zero")

        expression = ""

    except:

        equation.set("Error")

        expression = ""



def derivative():

    global expression

    if not sympy_available:

        equation.set("Install sympy")

        return

    try:

        x = sp.symbols('x')

        expr = sp.sympify(expression.replace("^", "**"))

        result = sp.diff(expr, x)

        equation.set(str(result))

        expression = str(result)

    except:

        equation.set("Derivative Error")

        expression = ""


def integration():

    global expression

    if not sympy_available:

        equation.set("Install sympy")

        return

    try:

        x = sp.symbols('x')

        expr = sp.sympify(expression.replace("^", "**"))

        result = sp.integrate(expr, x)

        equation.set(str(result))

        expression = str(result)

    except:

        equation.set("Integration Error")

        expression = ""



display = tk.Entry(

    window,
    textvariable=equation,
    font=("Arial", 24),
    bd=10,
    relief=tk.FLAT,
    bg="#2d2d2d",
    fg="white",
    justify="right"

)

display.grid(

    row=0,
    column=0,
    columnspan=6,
    ipadx=8,
    ipady=30,
    padx=10,
    pady=20,
    sticky="nsew"

)



number_color = "#d9d9d9"
operator_color = "#3498db"
scientific_color = "#9b59b6"
clear_color = "#e74c3c"
equal_color = "#2ecc71"
button_font = ("Arial", 14, "bold")



buttons = [

    ('7', 1, 0, number_color),
    ('8', 1, 1, number_color),
    ('9', 1, 2, number_color),
    ('/', 1, 3, operator_color),
    ('sin(', 1, 4, scientific_color),
    ('cos(', 1, 5, scientific_color),

    ('4', 2, 0, number_color),
    ('5', 2, 1, number_color),
    ('6', 2, 2, number_color),
    ('*', 2, 3, operator_color),
    ('tan(', 2, 4, scientific_color),
    ('log(', 2, 5, scientific_color),

    ('1', 3, 0, number_color),
    ('2', 3, 1, number_color),
    ('3', 3, 2, number_color),
    ('-', 3, 3, operator_color),
    ('ln(', 3, 4, scientific_color),
    ('√(', 3, 5, scientific_color),

    ('0', 4, 0, number_color),
    ('.', 4, 1, number_color),
    ('%', 4, 2, operator_color),
    ('+', 4, 3, operator_color),
    ('^', 4, 4, operator_color),
    ('π', 4, 5, scientific_color),

    ('(', 5, 0, operator_color),
    (')', 5, 1, operator_color),
    ('x', 5, 2, scientific_color),
    ('fact(', 5, 3, scientific_color),
    ('⌫', 5, 4, clear_color),
    ('AC', 5, 5, clear_color),

]



for (text, row, col, color) in buttons:
    if text == "AC":
        btn = tk.Button(
            window,
            text=text,
            font=button_font,
            bg=color,
            fg="white",
            command=clear
        )

    elif text == "⌫":
        btn = tk.Button(
            window,
            text=text,
            font=button_font,
            bg=color,
            fg="white",
            command=backspace
        )

    else:

        btn = tk.Button(
            window,
            text=text,
            font=button_font,
            bg=color,
            fg="black" if color == number_color else "white",
            command=lambda t=text: press(t)

        )

    btn.grid(
        row=row,
        column=col,
        ipadx=15,
        ipady=20,
        padx=5,
        pady=5,
        sticky="nsew"
    )



equal_button = tk.Button(
    window,
    text="=",
    font=("Arial", 20, "bold"),
    bg=equal_color,
    fg="white",
    command=calculate
)

equal_button.grid(
    row=6,
    column=0,
    columnspan=2,
    ipadx=15,
    ipady=25,
    padx=5,
    pady=10,
    sticky="nsew"
)

derivative_button = tk.Button(
    window,
    text="d/dx",
    font=("Arial", 18, "bold"),
    bg="#f39c12",
    fg="white",
    command=derivative

)

derivative_button.grid(
    row=6,
    column=2,
    columnspan=2,
    ipadx=15,
    ipady=25,
    padx=5,
    pady=10,
    sticky="nsew"

)

integration_button = tk.Button(
    window,
    text="∫",
    font=("Arial", 20, "bold"),
    bg="#16a085",
    fg="white",
    command=integration
)

integration_button.grid(
    row=6,
    column=4,
    columnspan=2,
    ipadx=15,
    ipady=25,
    padx=5,
    pady=10,
    sticky="nsew"
)



for i in range(7):

    window.grid_rowconfigure(i, weight=1)

for j in range(6):

    window.grid_columnconfigure(j, weight=1)

window.mainloop()

