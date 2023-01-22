# Import Modules
from math import *
from tkinter import *
import tkinter.messagebox as mbx

# Add something to the entry box
def do(something):
    current = box.get()
    box.delete(0, END)
    box.insert(0, (current + something))

# Add to the expression when a number is pressed
def press(number):
    global expression, ratioused, ratioval, inverse
    do(number)
    # What if the number is in a trigonometry ratio? These are the conditions to avoid errors
    if ratioused == True and number == ')':
        expression += f"{radians(float(ratioval))}"
        ratioused = False
    elif inverse == True and number == ')':
        expression += f"asin({float(ratioval)})"
        inverse = False
    if ratioused == True or inverse == True and number != ')':
        ratioval += number
    if ratioused == False or inverse == True:
        expression += number

# Shift the purpose of some buttons
def shifter():
    global shift_state
    if shift_state == False:
        sine.config(text='sin⁻¹', command=lambda: sincostan('sin⁻¹('))
        cosine.config(text='cos⁻¹', command=lambda: sincostan('cos⁻¹('))
        tangent.config(text='tan⁻¹', command=lambda: sincostan('tan⁻¹('))
        exponential.config(text='\u221A', command=lambda: operators('\u221A('))
        shift_state = True
    else:
        sine.config(text='sin \u03B8', command=lambda: sincostan('sin('))
        cosine.config(text='cos \u03B8', command=lambda: sincostan('cos('))
        tangent.config(text='tan \u03B8', command=lambda: sincostan('tan('))
        exponential.config(text='^', command=lambda: operators('^'))
        shift_state = False

# Runs when the user wants to do trigonometry
def sincostan(ratio):
    global expression, ratioused, inverse
    do(ratio)

    # These conditions are not necessarry but useful in order to look like a proper calculator
    if expression == '' or expression[-1] == ' + ' or expression[-1] == ' - ' or expression[-1] == '/' or expression[-1] == '(' or expression[-1] == '*':
        if ratio == 'sin(' or ratio == 'cos(' or ratio == 'tan(':
            ratioused = True
            expression += ratio
        elif ratio == 'sin⁻¹(' or ratio == 'cos⁻¹(' or ratio == 'tan⁻¹(':
            inverse = True
            expression += 'degrees('
    else:
        if ratio == 'sin(' or ratio == 'cos(' or ratio == 'tan(':
            ratioused = True
            expression += f"*{ratio}"
        elif ratio == 'sin⁻¹(' or ratio == 'cos⁻¹(' or ratio == 'tan⁻¹(':
            inverse = True
            expression += '*degrees('

# Function used to add the appropriate syntax for the expression of the operators
def operators(operator):
    global expression
    do(str(operator))
    if operator != 'π':
        expression += operator_dict[operator]
    elif expression == '' or expression[-1] == ' + ' or expression[-1] == ' - ' or expression[-1] == '/' or expression[-1] == '(' or expression[-1] == '*':
        expression += 'pi'
    else:
        expression += '*pi'

# CLear the entry box and the other variables
def clear():
    global expression, ratioval

    box.delete(0, END)
    expression = ''
    ratioval = ''

# delete the last character in the expression
def backspace():
    global expression, ratioval

    del_output = box.get()[:-1]
    box.delete(0, END)
    box.insert(0, del_output)
    expression = expression[:-1]
    if len(ratioval) > 0:
        ratioval = ratioval[:-1]

# Evaluate the expression
def solve():
    global expression
    # If the user made a mistake it doesn't solve
    try:
        print(expression)
        ans = eval(expression)
        box.delete(0, END)
        box.insert(0, ans)
        expression = str(ans)
        f = open('answers.txt', 'w')
        f.write(expression)
        f.close()
    except Exception:
        mbx.showerror('ERROR', 'Error: Please check what you typed on the calculator')

# Create tkinter window
root = Tk()
root.title("Calculator")
root.geometry("600x450+300+100")
root.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
root.columnconfigure((0, 1, 2, 3, 4), weight=1)

# Create important variables
expression = ''
ratioval = ''
ratioused = False
inverse = False
shift_state = False

# Specific Characters that need to go in the expression
operator_dict = {' + ' : ' + ', ' - ': ' - ', ' x ': '*', ' ÷ ': '/', '^': '**', '\u221A(': 'sqrt('}

# Create buttons
box = Entry(root, font=('Calibri', 20))
box.grid(row=0, column=0, columnspan=4, sticky=NSEW, pady=10, padx=5)
ac = Button(root, text='AC', command=clear, font=('Calibri', 15)).grid(row=0, column=4, sticky=NSEW)
delete = Button(root, text='DEL', font=('Calibri', 15), command=backspace).grid(row=1, column=4, sticky=NSEW)
shift = Button(root, text='SHIFT', font=('Calibri', 15), command=shifter).grid(row=1, column=0, sticky=NSEW)

# Create number buttons
n0 = Button(root, text=0, font=('Calibri', 15), command=lambda: press('0')).grid(row=5, column=0, sticky=NSEW)
n1 = Button(root, text=1, font=('Calibri', 15), command=lambda: press('1')).grid(row=4, column=0, sticky=NSEW)
n2 = Button(root, text=2, font=('Calibri', 15), command=lambda: press('2')).grid(row=4, column=1, sticky=NSEW)
n3 = Button(root, text=3, font=('Calibri', 15), command=lambda: press('3')).grid(row=4, column=2, sticky=NSEW)
n4 = Button(root, text=4, font=('Calibri', 15), command=lambda: press('4')).grid(row=3, column=0, sticky=NSEW)
n5 = Button(root, text=5, font=('Calibri', 15), command=lambda: press('5')).grid(row=3, column=1, sticky=NSEW)
n6 = Button(root, text=6, font=('Calibri', 15), command=lambda: press('6')).grid(row=3, column=2, sticky=NSEW)
n7 = Button(root, text=7, font=('Calibri', 15), command=lambda: press('7')).grid(row=2, column=0, sticky=NSEW)
n8 = Button(root, text=8, font=('Calibri', 15), command=lambda: press('8')).grid(row=2, column=1, sticky=NSEW)
n9 = Button(root, text=9, font=('Calibri', 15), command=lambda: press('9')).grid(row=2, column=2, sticky=NSEW)

# Create other Buttons
point = Button(root, text='.', font=('Calibri', 15), command=lambda: press('.')).grid(row=5, column=1, sticky=NSEW)
openBracket = Button(root, text='(', font=('Calibri', 15), command=lambda: press('(')).grid(row=3, column=4, sticky=NSEW)
closeBracket = Button(root, text=')', font=('Calibri', 15), command=lambda: press(')')).grid(row=4, column=4, sticky=NSEW)

# Create buttons for trigonometry
sine = Button(root, text='sin \u03B8', font=('Calibri', 15), command=lambda: sincostan('sin('))
sine.grid(row=1, column=1, sticky=NSEW)
cosine = Button(root, text='cos \u03B8', font=('Calibri', 15), command=lambda: sincostan('cos('))
cosine.grid(row=1, column=2, sticky=NSEW)
tangent = Button(root, text='tan \u03B8', font=('Calibri', 15), command=lambda: sincostan('tan('))
tangent.grid(row=1, column=3, sticky=NSEW)

# Create buttons for math operators
exponential = Button(root, text='^', font=('Calibri', 15), command=lambda: operators('^'))
exponential.grid(row=2, column=4, sticky=NSEW)
π = Button(root, text='π', font=('Calibri', 15), command=lambda: operators('π')).grid(row=5, column=2, sticky=NSEW)
divide = Button(root, text='÷', font=('Calibri', 15), command=lambda: operators(' ÷ ')).grid(row=2, column=3, sticky=NSEW)
multiply = Button(root, text='x', font=('Calibri', 15), command=lambda: operators(' x ')).grid(row=3, column=3, sticky=NSEW)
subtract = Button(root, text='-', font=('Calibri', 15), command=lambda: operators(' - ')).grid(row=4, column=3, sticky=NSEW)
add = Button(root, text='+', font=('Calibri', 15), command=lambda: operators(' + ')).grid(row=5, column=3, sticky=NSEW)

# A button to solve
equal = Button(root, text='=', font=('Calibri', 15), command=solve).grid(row=5, column=4, sticky=NSEW)

file = open('answers.txt', 'r')
box.insert(0, file.readlines(-1))

# The whileloop of tkinter which keeps the window open until the user quits
root.mainloop()
