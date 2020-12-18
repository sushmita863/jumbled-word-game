from tkinter import *
import random
#import messsagebox to display the message
from tkinter import messagebox

answers=['python', 'india', 'motherboard', 'landon', 'java', 'education','CPU', 'pen']
words=['hptony', 'iiand', 'aoeohtmrrbd', 'onlnda', 'vaaj',  'noteiudac', 'UCP', 'enp']
num=random.randrange(0,8,1)

def res():
    global words,answers,num
    num=random.randrange(0,7,1)
    lb1.config(text=words[num])
    e1.delete(0,END)

def default():
    global words, answers, num
    lb1.config(text=words[num])

def  checkans():
    global words, answers,num
    var=e1.get()
    if var==answers[num]:
        messagebox.showinfo("Success","This is correct")
        res()
    else:
        messagebox.showinfo("oops!","this is wrong answer")
        e1.delete(0,END)

root=Tk()
root.resizable(False,False)
root.title('Jumbled game')
root.configure(background="Black")

lb1=Label(root, text="your here", font=("verdana,20"), bg='white', fg='blue')
lb1.pack(ipadx=10, ipady=10)

ans1=StringVar()
e1=Entry(root, font=("verdana,18"), textvariable=ans1)
e1.pack(ipadx=5,ipady=5)

b1 = Button(root, text ="check", font = ("verdana,18"), width = 10, bg = "gray", fg = 'blue',command = checkans)
b1.pack(ipady=10)

b2 = Button(root, text = "Change", font = ("verdana 18"), width = 18, bg = "gray", fg = "blue", command = res)
b2.pack()
default()

root.mainloop()
