from tkinter import *
import tkinter as tk


window=tk.Tk()

window.title("Calculator")
window.geometry("360x340")
window.maxsize(340,340)
window.minsize(340,340)
window.configure(bg="#171717")

ent = Entry(window, width=48, borderwidth=10, relief=RIDGE)
ent.grid(pady=10,row=0,sticky="W",padx=15)

def delete():
    a = ent.get()
    ent.delete(first=len(a)-1,last="end")
    
def fresult():
    if ent.get() =="":
        pass
    elif ent.get()[0] =="0":
        ent.delete(0,"end")
        
    else:
        c_res = ent.get()
        c_res = eval(c_res)
        clearf()
        ent.insert("end",c_res)
        
def clearf():
    ent.delete(0,"end")
    

Char_seven = Button(window, text="7", width=7,command=lambda : ent.insert("end","7"),borderwidth=10,relief=RIDGE)
Char_seven.grid(row=1,sticky="W", padx=15)
Char_eight = Button(window, text="8", width=7,command=lambda : ent.insert("end","8"),borderwidth=10,relief=RIDGE)
Char_eight.grid(row=1,sticky="W", padx=93)
Char_nine = Button(window,text="9",width=7,command=lambda : ent.insert("end","9"),borderwidth=10,relief=RIDGE)
Char_nine.grid(row=1,sticky="w",padx=171)
clean = Button(window,text="C", width=7,command=clearf, bg="green", fg="white",borderwidth=10, relief=RIDGE)
clean.grid(row=1,sticky="W",padx=250)
Char_four = Button(window, text="4", width=7,command=lambda : ent.insert("end","4"),borderwidth=10,relief=RIDGE)
Char_four.grid(row=2,sticky="W", padx=15, pady=5)
Char_five = Button(window, text="5", width=7,command=lambda : ent.insert("end","5"),borderwidth=10,relief=RIDGE)
Char_five.grid(row=2,sticky="W", padx=93, pady=5)
Char_six = Button(window,text="6",width=7,command=lambda : ent.insert("end","6"),borderwidth=10,relief=RIDGE)
Char_six.grid(row=2,sticky="w",padx=171, pady=5)
Char_plus = Button(window,text="+",width=7,command=lambda : ent.insert("end","+"),borderwidth=10,relief=RIDGE)
Char_plus.grid(row=2,sticky="e",padx=250, pady=5)
Char_one = Button(window, text="1", width=7,command=lambda : ent.insert("end","1"),borderwidth=10,relief=RIDGE)
Char_one.grid(row=3,sticky="W", padx=15, pady=5)
Char_two = Button(window, text="2", width=7,command=lambda : ent.insert("end","2"),borderwidth=10,relief=RIDGE)
Char_two.grid(row=3,sticky="W", padx=93, pady=5)
Char_three = Button(window,text="3",width=7,command=lambda : ent.insert("end","3"),borderwidth=10,relief=RIDGE)
Char_three.grid(row=3,sticky="w",padx=171, pady=5)
Char_minus = Button(window,text="-",width=7,command=lambda : ent.insert("end","-"),borderwidth=10,relief=RIDGE)
Char_minus.grid(row=3,sticky="e",padx=250, pady=5)
Char_zero = Button(window, text="0", width=7,command=lambda : ent.insert("end","0"),borderwidth=10,relief=RIDGE)
Char_zero.grid(row=4,sticky="W", padx=15, pady=5)
Char_doublezero = Button(window, text="00", width=7,command=lambda : ent.insert("end","00"),borderwidth=10,relief=RIDGE)
Char_doublezero.grid(row=4,sticky="W", padx=93, pady=5)
Char_dot = Button(window,text=".",width=7,command=lambda : ent.insert("end","."),borderwidth=10,relief=RIDGE)
Char_dot.grid(row=4,sticky="w",padx=171, pady=5)
Char_divide = Button(window,text="/",width=7,command=lambda : ent.insert("end","/"),borderwidth=10,relief=RIDGE)
Char_divide.grid(row=4,sticky="e",padx=250, pady=5)

result = Button(window,text="=",width=18,command=fresult,bg="grey",borderwidth=10,relief=RIDGE)
result.grid(row=5,sticky="w",padx=15, pady=5)
Char_modulus = Button(window,text="%",width=7,command=lambda : ent.insert("end","%"),borderwidth=10,relief=RIDGE)
Char_modulus.grid(row=5,sticky="w",padx=171)

delete = Button(window,text="del",width=7,command=delete,borderwidth=10,relief=RIDGE)
delete.grid(row=5,sticky="e",padx=250, pady=5)

window.mainloop()