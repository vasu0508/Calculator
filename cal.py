import tkinter as tk

app = tk.Tk()

def clear():
    box.delete(0,tk.END)
def back():
    txt=box.get()
    txt=txt[:len(txt)-1:]
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertadd():
    txt=box.get()
    txt+="+"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertminus():
    txt=box.get()
    txt+="-"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertmult():
    txt=box.get()
    txt+="X"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertdiv():
    txt=box.get()
    txt+="/"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertone():
    txt=box.get()
    txt+="1"
    box.delete(0,tk.END)
    box.insert(0,txt)
def inserttwo():
    txt=box.get()
    txt+="2"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertthree():
    txt=box.get()
    txt+="3"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertfour():
    txt=box.get()
    txt+="4"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertfive():
    txt=box.get()
    txt+="5"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertsix():
    txt=box.get()
    txt+="6"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertseven():
    txt=box.get()
    txt+="7"
    box.delete(0,tk.END)
    box.insert(0,txt)
def inserteight():
    txt=box.get()
    txt+="8"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertnine():
    txt=box.get()
    txt+="9"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertzero():
    txt=box.get()
    txt+="0"
    box.delete(0,tk.END)
    box.insert(0,txt)
def insertdot():
    txt=box.get()
    txt+="."
    box.delete(0,tk.END)
    box.insert(0,txt)

def cal():
    try:
        txt1=box.get()
        l=[]
        m=[]
        n=""
        for x in txt1:
            if x in ['*','X','x','+','-','/']:
                l.append(x)
                m.append(n)
                n=""
            else:
                n+=str(x)
        n=float(n)
        m.append(n)
        print(l)
        print(m)
        if len(l)+1==len(m):
            i=-1
            res=float(m[0])
            for x in l:
                i+=1
                if x in['x','*','X']:
                    res*=float(m[i+1])
                elif x=='+':
                    res+=float(m[i+1])
                elif x=='/':
                    res/=float(m[i+1])
                else:
                    res-=float(m[i+1])
                print(res)
            box.delete(0,tk.END)
            box.insert(0,res)
        else:
            box.delete(0,tk.END)
            box.insert(0,"Invalid Input")
    except:
        print("Invalid")
app.title("CALCULATOR")
app.geometry("300x450")
app.resizable(False,False)

label3 = tk.Label(app, text="___________________________________________________________")
label3.place(x=0,y=23)

label1 =tk.Label(app, text= "INPUT", font= ("DengXian"))
label1.place(x=218,y=40)

label2 = tk.Label(app, text="__________________________________________________________")
label2.place(x=0,y=125)

box = tk.Entry(app,font=('DengXian'))
box.place(x=20,y=70, width= 260, height= 60)

button1 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "C", command= clear)
button1.place(x=19, y=165 , width= 50)

button2 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "=",command=cal)
button2.place(x= 153, y=165, width= 50)

button3 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "/",command=insertdiv)
button3.place(x= 220, y=165, width= 50)

button4 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "X",command=insertmult)
button4.place(x= 220, y=220, width= 50)

button5 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "-",command=insertminus)
button5.place(x= 220, y=275, width= 50)

button6 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "+", command=insertadd)
button6.place(x= 220, y=330, width= 50)

button7 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "9",command=insertnine)
button7.place(x= 153, y=222, width= 50)

button8 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "8",command=inserteight)
button8.place(x= 86, y=222, width= 50)

button9 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "7",command=insertseven)
button9.place(x= 19, y=222, width= 50)

button10 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "4",command=insertfour)
button10.place(x= 19, y=277, width= 50)

button11 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "5",command=insertfive)
button11.place(x= 86, y=277, width= 50)

button12 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "6",command=insertsix)
button12.place(x= 153, y= 277, width= 50)

button13 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "1",command=insertone)
button13.place(x= 19, y=332, width= 50)

button14 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "2",command=inserttwo)
button14.place(x= 86, y=332, width= 50)

button15 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "3",command=insertthree)
button15.place(x= 153, y=332, width= 50)
button16 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = ".",command=insertdot)
button16.place(x= 86, y=165, width= 50)

button17 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "0",command=insertzero)
button17.place(x= 19, y=387, width= 185)
button18 = tk.Button(app, font=('DengXian'), bg = 'light grey', text = "<=",command=back)
button18.place(x= 220, y=387, width= 50)





app.mainloop()