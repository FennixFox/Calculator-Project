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
        num1 = answer.value
        num1 = num1.replace("√", "sqrt")
        num1 = num1.replace("^", "**")
        num1 = num1.replace("×", "*")
        num1 = num1.replace("÷", "/")
        num1 = num1.replace("π", "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
        num1 = num1.replace("3.14159", "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
        num1 = num1.replace("e", "2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819")
        num1 = num1.replace("sin⁻¹", "asin")
        num1 = num1.replace("cos⁻¹", "acos")
        num1 = num1.replace("tan⁻¹", "atan")
        num1 = num1.replace("log₁₀", "log10")
        num1 = num1.replace("ln", "log")
        num1 = num1.replace("e^", "exp")
        Evaluation = eval(num1)
        Evaluation = round(Evaluation, 11)
        if len(str(Evaluation)) < 16:
            answer.value = Evaluation
            num1 = Evaluation
        else:
            Evaluation = "{:f}".format(Evaluation)
            CarrierPlague = Evaluation
            Evaluation="{:10e}".format(float(Evaluation))
            answer.value = Evaluation
            ShowNum.visible = True
            ShowNum.align = "left"
    except:
        warn("Cal Culator Error", "Invalid Syntax, Please check your equation")
        
def RealllyBigNumber():
    BigNum = CarrierPlague
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
    if Factorials.visible == True:
        Quadratic.visible = True
        Factorials.visible = False
        
        SinNum.visible = False
        InvSinNum.visible = True
        CosNum.visible = False
        InvCosNum.visible = True
        TanNum.visible = False
        InvTanNum.visible = True
        
        squared.visible = False
        LogE.visible = True
        squareroot.visible = False
        Log10.visible = True
        
        PiNum.visible = False
        PiNum2.visible = True
        
        eNum.visible = False
        eXNum.visible = True
        
    else:
        Quadratic.visible = False
        Factorials.visible = True
        SinNum.visible = True
        InvSinNum.visible = False
        CosNum.visible = True
        InvCosNum.visible = False
        TanNum.visible = True
        InvTanNum.visible = False
        
        squared.visible = True
        LogE.visible = False
        squareroot.visible = True
        Log10.visible = False
        
        PiNum.visible = True
        PiNum2.visible = False
        
        eNum.visible = True
        eXNum.visible = False

num1 = ""

app = App(title = "Cal the Culator™", layout="grid", height=670, width=500, bg=(33,33,33))
displayBox = Box(app, grid=[0,0,2,1], align="left", layout="grid")
OMEGACHADBOX = Box(app, layout="grid", grid=[0,1], align="left")
OMEGACHADBOX.bg=(45,45,45)
numpad = Box(OMEGACHADBOX, layout="grid", grid=[0,0])
etcBox = Box(OMEGACHADBOX, layout="grid", grid=[1,0])

answer = TextBox(displayBox, text="0", width="fill", grid=[1,0])
answer.font="Courier"
answer.text_size=40
answer.text_color="white"

ShowNum = PushButton(displayBox, text="Show\nFull\nNum", command=RealllyBigNumber, width=2, height=2, align="left", grid=[0,0])
ShowNum.text_size=11
ShowNum.text_color="white"
ShowNum.visible = False
ShowNum.font = "Courier"

seven = PushButton(numpad, text="7", command=numPressed, args=["7"], grid=[0,1], width=6, height=3)
seven.text_size=15
seven.text_color="white"
seven.font = "Courier"

eight = PushButton(numpad, text="8", command=numPressed, args=["8"], grid=[1,1], width=6, height=3)
eight.text_size=15
eight.text_color="white"
eight.font = "Courier"

nine = PushButton(numpad, text="9", command=numPressed, args=["9"], grid=[2,1], width=6, height=3)
nine.text_size=15
nine.text_color="white"
nine.font = "Courier"

four = PushButton(numpad, text="4", command=numPressed, args=["4"], grid=[0,2], width=6, height=3)
four.text_size=15
four.text_color="white"
four.font = "Courier"

five = PushButton(numpad, text="5", command=numPressed, args=["5"], grid=[1,2], width=6, height=3)
five.text_size=15
five.text_color="white"
five.font = "Courier"

six = PushButton(numpad, text="6", command=numPressed, args=["6"], grid=[2,2], width=6, height=3)
six.text_size=15
six.text_color="white"
six.font = "Courier"

one = PushButton(numpad, text="1", command=numPressed, args=["1"], grid=[0,3], width=6, height=3)
one.text_size=15
one.text_color="white"
one.font = "Courier"

two = PushButton(numpad, text="2", command=numPressed, args=["2"], grid=[1,3], width=6, height=3)
two.text_size=15
two.text_color="white"
two.font = "Courier"

decimal = PushButton(numpad, text=".", command=numPressed, args=["."], grid=[0,4], width=6, height=3)
decimal.text_size=15
decimal.text_color="white"
decimal.font = "Courier"

zero = PushButton(numpad, text="0", command=numPressed, args=["0"], grid=[1,4], width=6, height=3)
zero.text_size=15
zero.text_color="white"
zero.font = "Courier"

equals = PushButton(numpad, text="=", command=equalsPressed, grid=[2,4], width=6, height=3)
equals.text_size=15
equals.text_color="white"
equals.font = "Courier"

three = PushButton(numpad, text="3", command=numPressed, args=["3"], grid=[2,3], width=6, height=3)
three.text_size=15
three.text_color="white"
three.font = "Courier"

add = PushButton(etcBox, text="+", command=numPressed, args=["+"], grid=[3,1], width=6, height=3)
add.text_size=15
add.text_color="white"
add.font = "Courier"

subtract = PushButton(etcBox, text="-", command=numPressed, args=["-"], grid=[3,2], width=6, height=3)
subtract.text_size=15
subtract.text_color="white"
subtract.font = "Courier"

multiply = PushButton(etcBox, text="×", command=numPressed, args=["×"], grid=[3,3], width=6, height=3)
multiply.text_size=15
multiply.text_color="white"
multiply.font = "Courier"

divide = PushButton(etcBox, text="÷", command=numPressed, args=["÷"], grid=[3,4], width=6, height=3)
divide.text_size=15
divide.text_color="white"
divide.font = "Courier"

clear = PushButton(etcBox, text="Clear", command=deletePressed, grid=[4,1], width=6, height=3)
clear.text_size=15
clear.text_color="white"
clear.font = "Courier"

backspace = PushButton(etcBox, text="BckSpc", command=backPressed, grid=[4,2], width=6, height=3)
backspace.text_size=15
backspace.text_color="white"
backspace.font = "Courier"

squared = PushButton(etcBox, text="^", command=numPressed, args=["^"], grid=[3,5], width=6, height=3)
squared.text_size=15
squared.text_color="white"
squared.font = "Courier"

Log10 = PushButton(etcBox, text="log", command=numPressed, args=["log₁₀("], grid=[3,5], width=6, height=3)
Log10.text_size=15
Log10.text_color="white"
Log10.font = "Courier"
Log10.visible = False

squareroot = PushButton(etcBox, text="√", command=numPressed, args=["√("], grid=[3,6], width=6, height=3)
squareroot.text_size=15
squareroot.text_color="white"
squareroot.font = "Courier"

LogE = PushButton(etcBox, text="ln", command=numPressed, args=["ln("], grid=[3,6], width=6, height=3)
LogE.text_size=15
LogE.text_color="white"
LogE.font = "Courier"
LogE.visible = False

negative = PushButton(numpad, text="Other", command=SecondPressed, grid=[1,0], width=6, height=3)
negative.text_size=15
negative.text_color="white"
negative.font = "Courier"

OpenParentheses = PushButton(etcBox, text=")", command=numPressed, args=[")"], grid=[4,6], width=6, height=3)
OpenParentheses.text_size=15
OpenParentheses.text_color="white"
OpenParentheses.font = "Courier"

CloseParentheses = PushButton(etcBox, text="(", command=numPressed, args=["("], grid=[4,5], width=6, height=3)
CloseParentheses.text_size=15
CloseParentheses.text_color="white"
CloseParentheses.font = "Courier"

SinNum = PushButton(numpad, text="Sin", command=numPressed, args=["sin("], grid=[0,6], width=6, height=3)
SinNum.text_size=15
SinNum.text_color="white"
SinNum.font = "Courier"

InvSinNum = PushButton(numpad, text="Sin⁻¹", command=numPressed, args=["sin⁻¹("], grid=[0,6], width=6, height=3)
InvSinNum.text_size=15
InvSinNum.text_color="white"
InvSinNum.font = "Courier"
InvSinNum.visible = False

CosNum = PushButton(numpad, text="Cos", command=numPressed, args=["cos("], grid=[1,6], width=6, height=3)
CosNum.text_size=15
CosNum.text_color="white"
CosNum.font = "Courier"

InvCosNum = PushButton(numpad, text="Cos⁻¹", command=numPressed, args=["cos⁻¹("], grid=[1,6], width=6, height=3)
InvCosNum.text_size=15
InvCosNum.text_color="white"
InvCosNum.font = "Courier"
InvCosNum.visible = False

TanNum = PushButton(numpad, text="Tan", command=numPressed, args=["tan("], grid=[2,6], width=6, height=3)
TanNum.text_size=15
TanNum.text_color="white"
TanNum.font = "Courier"

InvTanNum = PushButton(numpad, text="Tan⁻¹", command=numPressed, args=["tan⁻¹("], grid=[2,6], width=6, height=3)
InvTanNum.text_size=15
InvTanNum.text_color="white"
InvTanNum.font = "Courier"
InvTanNum.visible = False

PiNum = PushButton(etcBox, text="π", command=numPressed, args=["π"], grid=[4,4], width=6, height=3)
PiNum.text_size=15
PiNum.text_color="white"
PiNum.font = "Courier"

PiNum2 = PushButton(etcBox, text="Pi", command=numPressed, args=["3.14159"], grid=[4,4], width=6, height=3)
PiNum2.text_size=15
PiNum2.text_color="white"
PiNum2.font = "Courier"
PiNum2.visible = False

Factorials = PushButton(numpad, text="!", command=numPressed, args=["factorial("], grid=[2,0], width=6, height=3)
Factorials.text_size=15
Factorials.text_color="white"
Factorials.font = "Courier"

eNum = PushButton(etcBox, text="e", command=numPressed, args=["e"], grid=[4,3], width=6, height=3)
eNum.text_size=15
eNum.text_color="white"
eNum.font = "Courier"

eXNum = PushButton(etcBox, text="e^", command=numPressed, args=["e^("], grid=[4,3], width=6, height=3)
eXNum.text_size=15
eXNum.text_color="white"
eXNum.font = "Courier"
eXNum.visible = False

Quadratic = PushButton(numpad, text="Qdrtc", command=QuadraticFormula, grid=[2,0], width=6, height=3)
Quadratic.text_size=15
Quadratic.text_color="white"
Quadratic.font = "Courier"
Quadratic.visible = False

SecondKey = PushButton(numpad, text="2nd", command=SecondPressed, grid=[0,0], width=6, height=3)
SecondKey.text_size=15
SecondKey.text_color="white"
SecondKey.font = "Courier"

QuadraticWindow = Window(app, title="Quadratic Window", width=300, height=300, bg=(33,33,33), layout="grid")
QuadraticWindow.hide()

Instructions = Text(QuadraticWindow, text="Please input your vars for\n the quadratic formula below:", font="Courier", color="white", grid=[0,0,4,1])

AEquals = Text(QuadraticWindow, text="a=", grid=[0,1], color="white", font="courier")
a = TextBox(QuadraticWindow, grid=[1,1])
a.text_size=15
a.text_color="white"
a.font = "Courier"

BEquals = Text(QuadraticWindow, text="b=", grid=[0,2], color="white", font="courier")
b = TextBox(QuadraticWindow, grid=[1,2])
b.text_size=15
b.text_color="white"
b.font = "Courier"

CEquals = Text(QuadraticWindow, text="c=", grid=[0,3], color="white", font="courier")
c = TextBox(QuadraticWindow, grid=[1,3])
c.text_size=15
c.text_color="white"
c.font = "Courier"

CalculateQE = PushButton(QuadraticWindow, text="Calculate!", command=QuadraticSolve, width=10, height=1, grid=[0,4])
CalculateQE.text_color="white"
CalculateQE.text_size=15
CalculateQE.font = "Courier"

FirstAnswer = Text(QuadraticWindow, grid=[0,5], color="white", font="courier")
SecondAnswer = Text(QuadraticWindow, grid=[0,6], color="white", font="courier")

OMEGANUMBER = Window(app, title="Big Number", width = 500, height = 500, bg=(33,33,33))
OMEGANUMBER.hide()

BigBoyNumBer = TextBox(OMEGANUMBER, width="fill", height="fill", multiline=True)
BigBoyNumBer.font = "Courier"
BigBoyNumBer.text_color = "white"
BigBoyNumBer.text_size=11

app.display()