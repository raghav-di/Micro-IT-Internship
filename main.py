import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.geometry('300x500')

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)


s=""

def calculate(s):
    try:    
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(float(stack.pop() / v))
        
            num, stack, sign = 0, [], "+"
            
            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + float(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)
    
    except:
        return "Error"

li=['2.2','/','2.2']
print(calculate(li))


def show():
    # ans=calculate(txt.get('1.0', 'end-1c'))
    ans=round(eval(txt.get('1.0', 'end-1c')),5)
    lbl.config(height=1,width=40,text=ans)
    print(ans)
def add0():
    global s
    s=s+'0'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
    print(s)
def add1():
    global s
    s=s+'1'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
    print(s)
def add2():
    global s
    s=s+'2'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
    print(s)
def add3():
    global s
    s=s+'3'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
    print(s)
def add4():
    global s
    s=s+'4'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
    print(s)
def add5():
    global s
    s=s+'5'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
    print(s)
def add6():
    global s
    s=s+'6'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
    print(s)
def add7():
    global s
    s=s+'7'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
def add8():
    global s
    s=s+'8'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
def add9():
    global s
    s=s+'9'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
def adddot():
    global s
    s=s+'.'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
def addsub():
    global s
    s=s+'-'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
def addadd():
    global s
    s=s+'+'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
    print(s)
def addmul():
    global s
    s=s+'*'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
def adddiv():
    global s
    s=s+'/'
    txt.delete("1.0","end")
    txt.insert("1.0",s)
def back():
    global s
    if len(s)>0:
        s=s[0:len(s)-1]
        txt.delete("1.0","end")
        txt.insert("1.0",s)
        print(s)


txt=tk.Text(root,height=2,width=20,font=("Ariel",24))
txt.grid(column=0, row=0, columnspan=4)

btn1=tk.Button(root,text='1',command=add1)
btn1.grid(column=0, row=4, sticky=tk.NSEW, padx=5, pady=5)
btn2=tk.Button(root,text='2',command=add2)
btn2.grid(column=1, row=4, sticky=tk.NSEW, padx=5, pady=5)
btn3=tk.Button(root,text='3',command=add3)
btn3.grid(column=2, row=4, sticky=tk.NSEW, padx=5, pady=5)
btn4=tk.Button(root,text='4',command=add4)
btn4.grid(column=0, row=3, sticky=tk.NSEW, padx=5, pady=5)
btn5=tk.Button(root,text='5',command=add5)
btn5.grid(column=1, row=3, sticky=tk.NSEW, padx=5, pady=5)
btn6=tk.Button(root,text='6',command=add6)
btn6.grid(column=2, row=3, sticky=tk.NSEW, padx=5, pady=5)
btn7=tk.Button(root,text='7',command=add7)
btn7.grid(column=0, row=2, sticky=tk.NSEW, padx=5, pady=5)
btn8=tk.Button(root,text='8',command=add8)
btn8.grid(column=1, row=2, sticky=tk.NSEW, padx=5, pady=5)
btn9=tk.Button(root,text='9',command=add9)
btn9.grid(column=2, row=2, sticky=tk.NSEW, padx=5, pady=5)
btndot=tk.Button(root,text='.',command=adddot)
btndot.grid(column=0, row=5, sticky=tk.NSEW, padx=5, pady=5)
btn0=tk.Button(root,text='0',command=add0)
btn0.grid(column=1, row=5, sticky=tk.NSEW, padx=5, pady=5)
btneql=tk.Button(root,text='=',command=show)
btneql.grid(column=3, row=1, sticky=tk.NSEW, padx=5, pady=5)
btnsub=tk.Button(root,text='-',command=addsub)
btnsub.grid(column=3, row=2, sticky=tk.NSEW, padx=5, pady=5)
btnadd=tk.Button(root,text='+',command=addadd)
btnadd.grid(column=3, row=3, sticky=tk.NSEW, padx=5, pady=5)
btndiv=tk.Button(root,text='/',command=adddiv)
btndiv.grid(column=3, row=4, sticky=tk.NSEW, padx=5, pady=5)
btnmul=tk.Button(root,text='x',command=addmul)
btnmul.grid(column=3, row=5, sticky=tk.NSEW, padx=5, pady=5)
btnback=tk.Button(root,text='<<',command=back)
btnback.grid(column=2, row=5, sticky=tk.NSEW, padx=5, pady=5)

lbl=tk.Label(root,text='')
lbl.grid(column=0, row=1, columnspan=3, sticky=tk.NS, padx=5, pady=5)

# root.mainloop()



