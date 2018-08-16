import random
from tkinter import *

def generate(event):
    try:
        n = int(e.get())
    except ValueError:
        blink(False)
        l1['text'] = 'Incorrect value!'
        return
    else:
        blink(True)
        
    if n >= 1000:
        blink(False)
        l1['text'] = 'Password is too long!'
        return
    elif n <= 0:
        blink(False)
        l1['text'] = 'Incorrect value!'
        return
    
    alphabet = []
    if use_upper.get() == True:
        alphabet.extend(list(map(chr, range(65, 91))))
    if use_lower.get() == True:
        alphabet.extend(list(map(chr, range(97, 123))))
    if use_digits.get():
        alphabet.extend(list(map(str, range(0, 10))))
    if alphabet == []:
        blink(False)
        l1['text'] = 'You must select at least one checkbutton!'
        return
    
    random.shuffle(alphabet)
    password = ''.join([random.choice(alphabet) for x in range(n)])
    
    l1['text'] = ' '.join(password)
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update() # now it stays on the clipboard after the window is closed
    
    l2 = Label(root, text='The password has been copied into your clipboard!', font=('Arial', 12), width=40)
    l2.pack(expand=1, fill=BOTH)
    l2.after(3000, lambda: l2.destroy()) # after 2000ms
    
def blink(flag):
    if flag:
        col = 'green'
    else:
        col = 'red'
    e.config(bg=col)
    e.after(500, lambda: e.config(bg='white')) # after 500ms

root = Tk()
root.title("Passwords generator")
root.geometry('500x300')

Label(root, text='Input a number of length of password (from 1 to 999):', font=('Arial', 12, 'bold'), width=30).pack(expand=1, fill=BOTH)

e = Entry(root, width=20)
e.pack(pady=5, expand=1, fill=BOTH)

f_cvar = Frame(root)
f_cvar.pack()

use_upper = BooleanVar()
use_upper_checkbutton = Checkbutton(f_cvar, text="Use upper case", variable=use_upper, onvalue=True, offvalue=False)
use_upper_checkbutton.select()
use_upper_checkbutton.pack(anchor=W)
 
use_lower = BooleanVar()
use_lower_checkbutton = Checkbutton(f_cvar, text="Use lower case", variable=use_lower, onvalue=True, offvalue=False)
use_lower_checkbutton.select()
use_lower_checkbutton.pack(anchor=W)

use_digits = BooleanVar()
use_digits_checkbutton = Checkbutton(f_cvar, text="Use digits", variable=use_digits, onvalue=True, offvalue=False)
use_digits_checkbutton.select()
use_digits_checkbutton.pack(anchor=W)

b = Button(root, text='Generate', activeforeground='#ffffff', activebackground='#555555', font=('Arial', 12, 'bold'))
b.bind('<Button-1>', generate)
b.pack(pady=10, expand=1, fill=BOTH)

l1 = Label(root, bg='black', fg='white', font=('Arial', 14), width=20)
l1.pack(expand=1, fill=BOTH)

root.mainloop()