from tkinter import *
from pynput import keyboard
from PIL import Image, ImageTk
import math

# Some useful variables
font = ('Arial', 27, 'bold')
btnfont = ('Arial', 24, 'bold')
btnfont1 = ('Arial', 14, 'bold', 'italic')

# function for keyboard input
def on_press(key):
    try:
        if key.char.isdigit():
            textfield.insert(END, key.char)
        elif key.char in "+-*/.%":
            textfield.insert(END, key.char)
        elif key.char == '=':
            try:
                ex = textfield.get()
                answer = eval(ex)
                textfield.delete(0, END)
                textfield.insert(END, answer)
            except:
                textfield.delete(0, END)
                textfield.insert(END, "Error")
    except AttributeError:
        if key == keyboard.Key.enter:
            try:
                ex = textfield.get()
                answer = eval(ex)
                textfield.delete(0, END)
                textfield.insert(END, answer)
            except:
                textfield.delete(0, END)
                textfield.insert(END, "Error")
        elif key == keyboard.Key.backspace:
            current = textfield.get()
            textfield.delete(0, END)
            textfield.insert(END, current[:-1])
            
listener = keyboard.Listener(on_press=on_press)
listener.start()

# functions
def clear():
    ex = textfield.get()
    ex = ex[0:len(ex)-1]
    textfield.delete(0,END)
    textfield.insert(0, ex)
    
def all_clear():
    textfield.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    btn = event.widget
    text = btn['text']
    print(text)
    
    if text == '÷':
        textfield.insert(END,"÷")
    elif text == 'x':
        textfield.insert(END,"x")
    elif text == '=':
        try:
            ex = textfield.get()
            ex = ex.replace("÷", "/")
            ex = ex.replace("x", "*")
            answer = eval(ex)
            textfield.delete(0, END)
            textfield.insert(0, answer)
        except:
            answer = "Error"
            textfield.delete(0, END)
            textfield.insert(0, answer)
    elif text == 'sin':
        ex = textfield.get()
        answer = math.sin(math.radians(float(ex)))
        textfield.delete(0, END)
        textfield.insert(0, answer)
    elif text == 'cos':
        ex = textfield.get()
        answer = math.cos(math.radians(float(ex)))
        textfield.delete(0, END)
        textfield.insert(0, answer)
    elif text == 'tan':
        ex = textfield.get()
        answer = math.tan(math.radians(float(ex)))
        textfield.delete(0, END)
        textfield.insert(0, answer)
    elif text == 'x⁻¹':
        ex = textfield.get()
        answer = 1 / float(ex)
        textfield.delete(0, END)
        textfield.insert(0, answer)
    elif text == 'x²':
        ex = textfield.get()
        answer = float(ex) ** 2
        textfield.delete(0, END)
        textfield.insert(0, answer)
    elif text == 'x³':
        ex = textfield.get()
        answer = float(ex) ** 3
        textfield.delete(0, END)
        textfield.insert(0, answer)
    elif text == '+/-':
        ex = textfield.get()
        if ex.startswith('-'):
            answer = ex[1:]
        else:
            answer = '-' + ex
        textfield.delete(0, END)
        textfield.insert(0, answer)
    elif text == '√':
        ex = textfield.get()
        answer = math.sqrt(float(ex))
        textfield.delete(0, END)
        textfield.insert(0, answer)
    elif text == '%':
        a = textfield.get()
        a = a.replace("x", "*")
        p = eval(a)/100
        textfield.delete(0, END)
        textfield.insert(0, p)
    else:
        textfield.insert(END, text)
    
# Creating a window
window=Tk()
window.title('Scientific Calculator')
window.geometry('329x566')
window.configure(bd=15, relief="ridge", bg="#033E3E", highlightthickness=4)
window.resizable(False, False)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (329/2)
y = (screen_height/2) - (566/2)
window.geometry(f'329x566+{int(x)}+{int(y)}')

# Image load 
image = Image.open("main.png")
photo = ImageTk.PhotoImage(image)

# Label & image set
label = Label(window, image=photo)
label.image = photo
label.place(x=0, y=0, relwidth=1, relheight=1)

# Textfield
textfield = Entry(window, font=font, bd= 10, justify='right', relief="sunken", background='#93917C', foreground='black')
textfield.pack(side=TOP, pady=10, fill= 'x', padx=10,)

# Images for Buttons
image = PhotoImage(file="buttonpng.png")
image1 = PhotoImage(file="buttonequal.png")
image2 = PhotoImage(file="buttonsci.png")
imageC = PhotoImage(file="buttonC.png")

# Buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=BOTTOM, pady=(0, 4))

# Button frame background image
frame_image1 = Image.open("main.png")
frame_photo1 = ImageTk.PhotoImage(frame_image1)
frame_label1 = Label(buttonFrame, image=frame_photo1)
frame_label1.image = frame_photo1  # Image ko retain karne ke liye
frame_label1.place(x=0, y=0, relwidth=1, relheight=1)

# Buttons sci
buttonFrame1 = Frame(window)
buttonFrame1.pack(side=TOP, padx=5,pady=8)

# Button frame1 background image
frame_image2 = Image.open("main.png")
frame_photo2 = ImageTk.PhotoImage(frame_image2)
frame_label2 = Label(buttonFrame1, image=frame_photo2)
frame_label2.image = frame_photo2  # Image ko retain karne ke liye
frame_label2.place(x=0, y=0, relwidth=1, relheight=1)

# Adding Buttons
Seven = Button(buttonFrame, image=image, text="7", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Seven.image = image
Seven.place(x=0, y=0, width=60, height=60)
Seven.grid(row=1, column=0,padx=1, pady=1)
Seven.bind('<Button-1>', click_btn_function)

Eight = Button(buttonFrame, image=image, text="8", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Eight.image = image
Eight.place(x=0, y=0, width=60, height=60)
Eight.grid(row=1, column=1,padx=1, pady=1)
Eight.bind('<Button-1>', click_btn_function)

Nine = Button(buttonFrame, image=image, text="9", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Nine.image = image
Nine.place(x=0, y=0, width=60, height=60)
Nine.grid(row=1, column=2,padx=1, pady=1)
Nine.bind('<Button-1>', click_btn_function)

Four = Button(buttonFrame, image=image, text="4", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Four.image = image
Four.place(x=0, y=0, width=60, height=60)
Four.grid(row=2, column=0,padx=1, pady=1)
Four.bind('<Button-1>', click_btn_function)

Five = Button(buttonFrame, image=image, text="5", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Five.image = image
Five.place(x=0, y=0, width=60, height=60)
Five.grid(row=2, column=1,padx=1, pady=1)
Five.bind('<Button-1>', click_btn_function)

Six = Button(buttonFrame, image=image, text="6", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Six.image = image
Six.place(x=0, y=0, width=60, height=60)
Six.grid(row=2, column=2,padx=1, pady=1)
Six.bind('<Button-1>', click_btn_function)

One = Button(buttonFrame, image=image, text="1", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
One.image = image
One.place(x=0, y=0, width=60, height=60)
One.grid(row=3, column=0,padx=1, pady=1)
One.bind('<Button-1>', click_btn_function)

Two = Button(buttonFrame, image=image, text="2", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Two.image = image
Two.place(x=0, y=0, width=60, height=60)
Two.grid(row=3, column=1,padx=1, pady=1)
Two.bind('<Button-1>', click_btn_function)

Three = Button(buttonFrame, image=image, text="3", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Three.image = image
Three.place(x=0, y=0, width=60, height=60)
Three.grid(row=3, column=2,padx=1, pady=1)
Three.bind('<Button-1>', click_btn_function)

Zero = Button(buttonFrame, image=image, text="0", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Zero.image = image
Zero.place(x=0, y=0, width=60, height=60)
Zero.grid(row=4, column=0,padx=1, pady=1)
Zero.bind('<Button-1>', click_btn_function)

##########################################################################################################################################################################################################

Backbtn = Button(buttonFrame, image=image, text="⌫", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, command=clear, activebackground='#3B3131')
Backbtn.image = image
Backbtn.place(x=0, y=0, width=60, height=60)
Backbtn.grid(row=0, column=1,padx=1, pady=1)

Dotbtn = Button(buttonFrame, image=image, text=".", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Dotbtn.image = image
Dotbtn.place(x=0, y=0, width=60, height=60)
Dotbtn.grid(row=4, column=1,padx=1, pady=1)
Dotbtn.bind('<Button-1>', click_btn_function)

Clearbtn = Button(buttonFrame, image=imageC, text="C", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, command=all_clear, activebackground='#3B3131')
Clearbtn.image = image
Clearbtn.place(x=0, y=0, width=60, height=60)
Clearbtn.grid(row=0, column=0,padx=1, pady=1 )

Percentbtn = Button(buttonFrame, image=image, text="%", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Percentbtn.image = image
Percentbtn.place(x=0, y=0, width=60, height=60)
Percentbtn.grid(row=4, column=2,padx=1, pady=1)
Percentbtn.bind('<Button-1>', click_btn_function)

Divbtn = Button(buttonFrame, image=image, text="÷", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Divbtn.image = image
Divbtn.place(x=0, y=0, width=60, height=60)
Divbtn.grid(row=0, column=2,padx=1, pady=1)
Divbtn.bind('<Button-1>', click_btn_function)

Multibtn = Button(buttonFrame, image=image, text="x", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Multibtn.image = image
Multibtn.place(x=0, y=0, width=60, height=60)
Multibtn.grid(row=0, column=3,padx=1, pady=1)
Multibtn.bind('<Button-1>', click_btn_function)

Minusbtn = Button(buttonFrame, image=image, text="-", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Minusbtn.image = image
Minusbtn.place(x=0, y=0, width=60, height=60)
Minusbtn.grid(row=1, column=3,padx=1, pady=1)
Minusbtn.bind('<Button-1>', click_btn_function)

Plusbtn = Button(buttonFrame, image=image, text="+", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Plusbtn.image = image
Plusbtn.place(x=0, y=0, width=60, height=60)
Plusbtn.grid(row=2, column=3, padx=1, pady=1)
Plusbtn.bind('<Button-1>', click_btn_function)

Equalbtn = Button(buttonFrame, image=image1, text="=", font=btnfont, compound="center", background='#3B3131', foreground='white',borderwidth=0, highlightthickness=0, activebackground='#3B3131')
Equalbtn.image = image
Equalbtn.place(x=0, y=0, width=60, height=60)
Equalbtn.grid(row=3, column=3, rowspan=2,)
Equalbtn.bind('<Button-1>', click_btn_function)

##########################################################################################################################################################################################################

sinbtn = Button(buttonFrame1, image=image2, text="sin", font=btnfont1, compound="center", background='#3B3131', foreground='white', borderwidth=0, highlightthickness=0, activebackground='#3B3131')
sinbtn.image = image
sinbtn.place(x=0, y=0, width=60, height=60)
sinbtn.grid(row=5, column=0, padx=(2, 4), pady=(2, 4))
sinbtn.bind('<Button-1>', click_btn_function)

cosbtn = Button(buttonFrame1, image=image2, text="cos", font=btnfont1, compound="center", background='#3B3131', foreground='white', borderwidth=0, highlightthickness=0, activebackground='#3B3131')
cosbtn.image = image
cosbtn.place(x=0, y=0, width=60, height=60)
cosbtn.grid(row=5, column=1, padx=(2, 4), pady=(2, 4))
cosbtn.bind('<Button-1>', click_btn_function)

tanbtn = Button(buttonFrame1, image=image2, text="tan", font=btnfont1, compound="center", background='#3B3131', foreground='white', borderwidth=0, highlightthickness=0, activebackground='#3B3131')
tanbtn.image = image
tanbtn.place(x=0, y=0, width=60, height=60)
tanbtn.grid(row=5, column=2, padx=(2, 4), pady=(2, 4))
tanbtn.bind('<Button-1>', click_btn_function)

btn = Button(buttonFrame1, image=image2, text="x⁻¹", font=btnfont1, compound="center", background='#3B3131', foreground='white', borderwidth=0, highlightthickness=0, activebackground='#3B3131')
btn.image = image
btn.place(x=0, y=0, width=60, height=60)
btn.grid(row=5, column=3, padx=(2, 4), pady=(2, 4))
btn.bind('<Button-1>', click_btn_function)

btn = Button(buttonFrame1, image=image2, text="x²", font=btnfont1, compound="center", background='#3B3131', foreground='white', borderwidth=0, highlightthickness=0, activebackground='#3B3131')
btn.image = image
btn.place(x=0, y=0, width=60, height=60)
btn.grid(row=6, column=0, padx=(2, 4), pady=(2, 4))
btn.bind('<Button-1>', click_btn_function)

btn = Button(buttonFrame1, image=image2, text="x³", font=btnfont1, compound="center", background='#3B3131', foreground='white', borderwidth=0, highlightthickness=0, activebackground='#3B3131')
btn.image = image
btn.place(x=0, y=0, width=60, height=60)
btn.grid(row=6, column=1, padx=(2, 4), pady=(2, 4))
btn.bind('<Button-1>', click_btn_function)

btn = Button(buttonFrame1, image=image2, text="+/-", font=btnfont1, compound="center", background='#3B3131', foreground='white', borderwidth=0, highlightthickness=0, activebackground='#3B3131')
btn.image = image
btn.place(x=0, y=0, width=60, height=60)
btn.grid(row=6, column=2, padx=(2, 4), pady=(2, 4))
btn.bind('<Button-1>', click_btn_function)

btn = Button(buttonFrame1, image=image2, text="√", font=btnfont1, compound="center", background='#3B3131', foreground='white', borderwidth=0, highlightthickness=0, activebackground='#3B3131')
btn.image = image
btn.place(x=0, y=0, width=60, height=60)
btn.grid(row=6, column=3, padx=(2, 4), pady=(2, 4))
btn.bind('<Button-1>', click_btn_function)

window.mainloop()
