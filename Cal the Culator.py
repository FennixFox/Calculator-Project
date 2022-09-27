from guizero import PushButton, App, Text, Box, warn, Window, TextBox
from math import *

def numPressed(pressed):
    global num1
    num1 += pressed
    answer.value=num1
    
def equalsPressed():
    try:
        global num1
        global Evaluation
        global CarrierPlague
        Evaluation = eval(num1)
        Evaluation = round(Evaluation, 10)
        Evaluation = str(Evaluation)
        EvalList = list(Evaluation)
        NumLen = len(Evaluation)
        NumExcess = NumLen - 8
        Exponent = NumLen - 1
        if NumLen < 15:
            answer.value = Evaluation
            num1 = Evaluation
        else:
            CarrierPlague = Evaluation
            Evaluation = Evaluation[:-NumExcess]
            Evaluation = Evaluation[:1] + '.' + Evaluation[1:]
            Evaluation += "e" + str(Exponent)
            answer.value = Evaluation
            ShowNum.visible = True
            ShowNum.align = "left"
    except:
        warn("Cal Culator Error", "Invalid Syntax, Please check your equation")
        
def RealllyBigNumber():
    BigNum = CarrierPlague
    BigNum = ("\n".join([BigNum[i:i+55] for i in range(0, len(BigNum), 55)]))
    OMEGANUMBER.show()
    BigBoyNumBer.value = BigNum
    ShowNum.visible = False
        
def deletePressed():
    global num1
    num1 = ""
    answer.value = "0"
    
def backPressed():
    global num1
    num1 = num1[:-1]
    answer.value = num1
    
def QuadraticFormula():
    QuadraticWindow.show()
    
def QuadraticSolve():
    try:
        Answer= ((-float(b.value) + sqrt(float(b.value)**2-4*float(a.value)*float(c.value)))/2*float(a.value))
        Answer2= ((-float(b.value) - sqrt(float(b.value)**2-4*float(a.value)*float(c.value)))/2*float(a.value))
        FirstAnswer.value = Answer
        SecondAnswer.value = Answer2
    except:
        warn("Something Went Wrong", "Either you didn't input numbers, or the calculation ended with an Imaginary Number")

def SecondPressed():
    pass
    
    

num1 = ""

app = App(title = "Cal the Culator™", layout="grid", height=630, width=470, bg=(33,33,33))
displayBox = Box(app, grid=[0,0,2,1], align="left", layout="grid")
OMEGACHADBOX = Box(app, layout="grid", grid=[0,1], align="left")
OMEGACHADBOX.bg=(45,45,45)
numpad = Box(OMEGACHADBOX, layout="grid", grid=[0,0])
etcBox = Box(OMEGACHADBOX, layout="grid", grid=[1,0])

answer = Text(displayBox, font="Courier", text="0", width="fill", size=40, color="white", grid=[1,0])
ShowNum = PushButton(displayBox, text="Show\nFull\nNum", command=RealllyBigNumber, width=2, height=2, align="left", grid=[0,0])
ShowNum.text_size=11
ShowNum.text_color="white"
ShowNum.visible = False

seven = PushButton(numpad, text="7", command=numPressed, args=["7"], grid=[0,1], width=6, height=2)
seven.text_size=15
seven.text_color="white"

eight = PushButton(numpad, text="8", command=numPressed, args=["8"], grid=[1,1], width=6, height=2)
eight.text_size=15
eight.text_color="white"

nine = PushButton(numpad, text="9", command=numPressed, args=["9"], grid=[2,1], width=6, height=2)
nine.text_size=15
nine.text_color="white"

four = PushButton(numpad, text="4", command=numPressed, args=["4"], grid=[0,2], width=6, height=2)
four.text_size=15
four.text_color="white"

five = PushButton(numpad, text="5", command=numPressed, args=["5"], grid=[1,2], width=6, height=2)
five.text_size=15
five.text_color="white"

six = PushButton(numpad, text="6", command=numPressed, args=["6"], grid=[2,2], width=6, height=2)
six.text_size=15
six.text_color="white"

one = PushButton(numpad, text="1", command=numPressed, args=["1"], grid=[0,3], width=6, height=2)
one.text_size=15
one.text_color="white"

two = PushButton(numpad, text="2", command=numPressed, args=["2"], grid=[1,3], width=6, height=2)
two.text_size=15
two.text_color="white"

decimal = PushButton(numpad, text=".", command=numPressed, args=["."], grid=[0,4], width=6, height=2)
decimal.text_size=15
decimal.text_color="white"

zero = PushButton(numpad, text="0", command=numPressed, args=["0"], grid=[1,4], width=6, height=2)
zero.text_size=15
zero.text_color="white"

equals = PushButton(etcBox, text="=", command=equalsPressed, grid=[4,6], width=6, height=2)
equals.text_size=15
equals.text_color="white"

three = PushButton(numpad, text="3", command=numPressed, args=["3"], grid=[2,3], width=6, height=2)
three.text_size=15
three.text_color="white"

add = PushButton(etcBox, text="+", command=numPressed, args=["+"], grid=[3,1], width=6, height=2)
add.text_size=15
add.text_color="white"

subtract = PushButton(etcBox, text="-", command=numPressed, args=["-"], grid=[3,2], width=6, height=2)
subtract.text_size=15
subtract.text_color="white"

multiply = PushButton(etcBox, text="x", command=numPressed, args=["*"], grid=[3,3], width=6, height=2)
multiply.text_size=15
multiply.text_color="white"

divide = PushButton(etcBox, text="÷", command=numPressed, args=["/"], grid=[3,4], width=6, height=2)
divide.text_size=15
divide.text_color="white"

clear = PushButton(etcBox, text="Clear", command=deletePressed, grid=[4,1], width=6, height=2)
clear.text_size=15
clear.text_color="white"

backspace = PushButton(etcBox, text="BckSpc", command=backPressed, grid=[4,2], width=6, height=2)
backspace.text_size=15
backspace.text_color="white"

squared = PushButton(etcBox, text="^", command=numPressed, args=["**"], grid=[3,5], width=6, height=2)
squared.text_size=15
squared.text_color="white"

squareroot = PushButton(etcBox, text="√", command=numPressed, args=["sqrt("], grid=[3,6], width=6, height=2)
squareroot.text_size=15
squareroot.text_color="white"

negative = PushButton(numpad, text="(-)", command=numPressed, args=["-"], grid=[2,4], width=6, height=2)
negative.text_size=15
negative.text_color="white"

OpenParentheses = PushButton(etcBox, text="(", command=numPressed, args=["("], grid=[4,3], width=6, height=2)
OpenParentheses.text_size=15
OpenParentheses.text_color="white"

CloseParentheses = PushButton(etcBox, text=")", command=numPressed, args=[")"], grid=[4,4], width=6, height=2)
CloseParentheses.text_size=15
CloseParentheses.text_color="white"

SinNum = PushButton(numpad, text="Sin", command=numPressed, args=["sin("], grid=[0,6], width=6, height=2)
SinNum.text_size=15
SinNum.text_color="white"

CosNum = PushButton(numpad, text="Cos", command=numPressed, args=["cos("], grid=[1,6], width=6, height=2)
CosNum.text_size=15
CosNum.text_color="white"

TanNum = PushButton(numpad, text="Tan", command=numPressed, args=["tan("], grid=[2,6], width=6, height=2)
TanNum.text_size=15
TanNum.text_color="white"

PiNum = PushButton(etcBox, text="π", command=numPressed, args=["3.14159"], grid=[4,5], width=6, height=2)
PiNum.text_size=15
PiNum.text_color="white"

Factorials = PushButton(numpad, text="!", command=numPressed, args=["factorial("], grid=[2,0], width=6, height=2)
Factorials.text_size=15
Factorials.text_color="white"

Quadratic = PushButton(numpad, text="Qdrtc", command=QuadraticFormula, grid=[1,0], width=6, height=2)
Quadratic.text_size=15
Quadratic.text_color="white"

SecondKey = PushButton(numpad, text="2nd", command=SecondPressed, grid=[0,0], width=6, height=2)
SecondKey.text_size=15
SecondKey.text_color="white"

QuadraticWindow = Window(app, title="Quadratic Window", width=300, height=300, bg=(33,33,33), layout="grid")
QuadraticWindow.hide()

Instructions = Text(QuadraticWindow, text="Please input your vars for\n the quadratic formula below:", font="Courier", color="white", grid=[0,0,4,1])

AEquals = Text(QuadraticWindow, text="a=", grid=[0,1], color="white", font="courier")
a = TextBox(QuadraticWindow, grid=[1,1])
a.text_size=15
a.text_color="white"

BEquals = Text(QuadraticWindow, text="b=", grid=[0,2], color="white", font="courier")
b = TextBox(QuadraticWindow, grid=[1,2])
b.text_size=15
b.text_color="white"

CEquals = Text(QuadraticWindow, text="c=", grid=[0,3], color="white", font="courier")
c = TextBox(QuadraticWindow, grid=[1,3])
c.text_size=15
c.text_color="white"

CalculateQE = PushButton(QuadraticWindow, text="Calculate!", command=QuadraticSolve, width=10, height=1, grid=[0,4])
CalculateQE.text_color="white"
CalculateQE.text_size=15

FirstAnswer = Text(QuadraticWindow, grid=[0,5], color="white")
SecondAnswer = Text(QuadraticWindow, grid=[0,6], color="white")

OMEGANUMBER = Window(app, title="Big Number", width = 500, height = 500, bg=(33,33,33))
OMEGANUMBER.hide()

BigBoyNumBer = Text(OMEGANUMBER, width="fill", height="fill")
BigBoyNumBer.font="Courier"
BigBoyNumBer.text_color = "white"
BigBoyNumBer.text_size=11

app.display()