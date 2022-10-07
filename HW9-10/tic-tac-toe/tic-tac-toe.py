from tkinter import *

turn = 1

def player_turn():
    global turn
    turn += 1

def b1_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=40, y=50, anchor=NW)
    value = int(b1["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8, 10]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def b2_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=150, y=50, anchor=NW)
    value = int(b2["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)        
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def b3_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=260, y=50, anchor=NW)
    value = int(b3["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def b4_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=40, y=160, anchor=NW)
    value = int(b4["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def b5_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=150, y=160, anchor=NW)
    value = int(b5["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def b6_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=260, y=160, anchor=NW)
    value = int(b6["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def b7_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=40, y=270, anchor=NW)
    value = int(b7["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def b8_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=150, y=270, anchor=NW)
    value = int(b8["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def b9_click():
    c1 = Canvas(width=100, height=100, bg='white', bd='1', highlightbackground='black')
    c1.place(x=260, y=270, anchor=NW)
    value = int(b9["text"])
    if turn in [1, 3, 5, 7, 9]:
        x_list.append(value)
        c1.create_line(10, 10, 90, 90, width=5)
        c1.create_line(10, 90, 90, 10, width=5)
    if turn in [2, 4, 6, 8]:
        o_list.append(value)
        c1.create_oval(10, 10, 90, 90, width=5)
        c1.create_oval(10, 90, 90, 10, width=5)
    game()

def end_game():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()
    b8.destroy()
    b9.destroy()

x_list = []
o_list = []

def game():
    win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    global turn
    if turn == 9: 
        l_text['text']='У Вас ничья!'
        end_game()
    for i in win_list:
        a = set(i).issubset(x_list)
        b = set(i).issubset(o_list)
        match (a, b):
            case (True, False): 
                l_text['text']='Победил крестик!'
                end_game()
            case (False, True): 
                l_text['text']='Победил нолик!'
                end_game()
    player_turn()


window = Tk()
window.title("Крестики-Нолики")

window.geometry(f'400x450')
window.resizable(False, False)

window_back_img = PhotoImage(file=r'HW9-10/tic-tac-toe/tic-tac-toe-back1.png')
lbl_back = Label(window, image=window_back_img)

pixel = PhotoImage(width=1, height=1)

l_text = Label(text="Начало игры", width=20, height=2, bg='white')

b1 = Button(text="1", image=pixel, width=100, height=100, bg='white', command=b1_click)
b2 = Button(text="2", image=pixel, width=100, height=100, bg='white', command=b2_click)
b3 = Button(text="3", image=pixel, width=100, height=100, bg='white', command=b3_click)

b4 = Button(text="4", image=pixel, width=100, height=100, bg='white', command=b4_click)
b5 = Button(text="5", image=pixel, width=100, height=100, bg='white', command=b5_click)
b6 = Button(text="6", image=pixel, width=100, height=100, bg='white', command=b6_click)

b7 = Button(text="7", image=pixel, width=100, height=100, bg='white', command=b7_click)
b8 = Button(text="8", image=pixel, width=100, height=100, bg='white', command=b8_click)
b9 = Button(text="9", image=pixel, width=100, height=100, bg='white', command=b9_click)

b_exit = Button(text="Выход", width=11, height=2, bg='white', command=window.quit)

lbl_back.grid(row=0, column=0)

b1.place(x=40, y=50, anchor=NW)
b2.place(x=150, y=50, anchor=NW)
b3.place(x=260, y=50, anchor=NW)

b4.place(x=40, y=160, anchor=NW)
b5.place(x=150, y=160, anchor=NW)
b6.place(x=260, y=160, anchor=NW)

b7.place(x=40, y=270, anchor=NW)
b8.place(x=150, y=270, anchor=NW)
b9.place(x=260, y=270, anchor=NW)

l_text.place(x=200, y=20, anchor=CENTER)

b_exit.place(x=200, y=410, anchor=CENTER)

window.mainloop()