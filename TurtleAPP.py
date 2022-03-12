import turtle
from tkinter import *
from tkinter import colorchooser, Menu, messagebox
from tkinter.ttk import *
from turtlefigure import *


# define instruction function
def instruction():
    messagebox.showinfo(title="Step 1", message="Firstly, you can choose a color you like as the screen color.")
    messagebox.showinfo(title="Step 2", message="Secondly, you can choose a type of figures you want to draw.")
    messagebox.showinfo(title="Step 3", message="Thirdly, you can set the speed and thickness of your pen.")
    messagebox.showwarning(title="WARNING", message="Don't forget click <Confirm>.")
    messagebox.showinfo(title="Step 4", message="Fourthly, you can set the order and length of your figure.")
    messagebox.showinfo(title="Step 5", message="Finally, you just need click the <draw> button.")
    messagebox.askquestion(title="Try it", message="Now, are you ready to draw your figures?")

# define restart function
def restart():
    reset()
    clearF()
    screen.bgcolor("#FFB3B3")
    pen.color("blue")

# define screenColor function
def screenColor():
    screen.bgcolor(colorchooser.askcolor()[1])

# define penColor function
def penColor():
    pen.color(colorchooser.askcolor()[1])

# define default function
def reset():
    speedInt.set(0)
    widthEntry.delete(0, END)

# define confirm function
def confirm():
    penSpeed = speedInt.get()
    pen.speed(speedList.index(penSpeed))
    pen.width(widthInt.get())

# define clearF function
def clearF():
    # delete all characters in orderEntry
    orderEntry.delete(0, END)
    # delete all characters in drawEntry
    lengthEntry.delete(0, END)
    # clear the figure
    pen.clear()
    # put pen in the origin
    pen.up()
    pen.home()

# define drawF function
def drawF():
    # get order and length
    length = lengthInt.get()
    order = orderInt.get()
    # get the figure id from OptionMenu
    figure = figureStr.get()
    figureId = figureList.index(figure)

    # if check to see what to draw
    if figureId == 0:  # draw binary tree
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws binary tree
        tree(order, length, pen)
    elif figureId == 1:  # draw quad tree
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws dandelion
        dandelion(order, length, pen)
    elif figureId == 2:  # draw fern
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws fern
        fern(order, length, pen)
    elif figureId == 3:  # draw snow flake
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws snow flake
        flake(order, length, pen)
    elif figureId == 4:  # draw antiflake
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws antiflake
        antiflake(order, length, pen)
    elif figureId == 5:  # draw S-Gasket
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws S-Gasket
        sgasket(order, length, pen)
    elif figureId == 6:  # draw Swiss-Gasket
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws Swiss-Gasket
        swiss(order, length, pen)
    elif figureId == 7:  # draw Pentagon-Gasket
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws Pentagon-Gasket
        pent(order, length, pen)
    elif figureId == 8:  # draw Expanding-Pentagon
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws Expanding-Pentagon
        expanding(order, length, pen)
    else:  # draw Chain-Circle
        # move pen to a better position
        pen.up()
        pen.backward(length)
        pen.down()
        # pen draws Chain-Circle
        chain(order, length, pen)


# create a window called "root"
root = Tk()
root.title("Turtle Application")
root.geometry("900x650+300+100")

# ---------------------make the interface---------------------
# make a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create menus
helpMenu = Menu(menubar)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Instruction", command=instruction)
fileMenu = Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Restart", command=restart)  # restart = reset + clear
fileMenu.add_command(label="Exit", command=quit)

# make the "Turtle Generator" label on the top center of the canvas panel
label = Label(root, text="Turtle Generator", font=("Arial", 25))
label.grid(row=0, column=3)

# make the canvas panel
canvasPanel = LabelFrame(root, text="Canvas Frame")
canvasPanel.grid(row=1, column=1, columnspan=5, rowspan=5)

# make the canvas
canvas = Canvas(canvasPanel, width=500, height=500)
canvas.pack()

# make a button to choose screen color
screenColorButton = Button(canvasPanel, text="Choose Screen Color", command=screenColor)
screenColorButton.pack()

# make a button to choose pen color
penColorButton = Button(canvasPanel, text="Choose Pen Color", command=penColor)
penColorButton.pack()

# get the canvas pen and screen
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("#FFB3B3")
pen = turtle.RawTurtle(screen)
pen.color("blue")

# make the preset panel
presetPanel = LabelFrame(root, text="Preset Frame", width=300, height=200)
presetPanel.grid(row=1, column=6, rowspan=2, columnspan=3)

# make the pen speed label
penSpeedLabel = Label(presetPanel, text="Pen Speed")
penSpeedLabel.grid(row=1, column=1)

# make the speed drop down box
speedList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
speedInt = IntVar()
speedOptionMenu = OptionMenu(presetPanel, speedInt, speedList[0], *speedList)
speedOptionMenu.grid(row=1, column=2)
speedInt.set(0)

# make the pen width label
penWidthLabel = Label(presetPanel, text="Pen Width")
penWidthLabel.grid(row=2, column=1)

widthInt = IntVar()
widthEntry = Entry(presetPanel, textvariable=widthInt)
widthEntry.grid(row=2, column=2, columnspan=2)

# make the reset button
resetButton = Button(presetPanel, text="Reset", command=reset)
resetButton.grid(row=3, column=1)

# make the confirm button
confirmButton = Button(presetPanel, text="Confirm", command=confirm)
confirmButton.grid(row=3, column=2)

# make the control panel
controlPanel = LabelFrame(root, text="Control Frame", width=300, height=200)
controlPanel.grid(row=3, column=6, rowspan=2, columnspan=3)

# make the figure label
figureLabel = Label(controlPanel, text="Figure")
figureLabel.grid(row=4, column=6)

# make the figures drop down box
figureList = ["Binary Tree", "Dandelion", "Fern", "Snow Flake", "Anti Flake", "S-Gasket", "Swiss-Gasket", "Pentagon-Gasket", "Shrunken-Pentagon", "Chain-Circle"]
figureStr = StringVar()
figureOptionMenu = OptionMenu(controlPanel, figureStr, figureList[0], *figureList)
figureOptionMenu.grid(row=4, column=7, columnspan=2)
figureStr.set("Binary Tree")

# make the length widgets
lengthLabel = Label(controlPanel, text="Length")
lengthLabel.grid(row=5, column=6)

lengthInt = IntVar()
lengthEntry = Entry(controlPanel, textvariable=lengthInt)
lengthEntry.grid(row=5, column=7, columnspan=2)

# make the order widgets
orderLabel = Label(controlPanel, text="Order")
orderLabel.grid(row=6, column=6)

orderInt = IntVar()
orderEntry = Entry(controlPanel, textvariable=orderInt)
orderEntry.grid(row=6, column=7, columnspan=2)

# make the clear button
clearButton = Button(controlPanel, text="Clear", command=clearF)
clearButton.grid(row=7, column=7)

# make the draw button
drawButton = Button(controlPanel, text="Draw", command=drawF)
drawButton.grid(row=7, column=8)

root.mainloop()
