import tkinter
from tkinter import *
import tkinter.scrolledtext as st
from table_connection import init, get_word, LINK
import random

random.seed()
LANG = 'Ru'  # Ru En
STATE = 'Say'  # Write
CURRENT_ROW = 0
SCORE = 0
TOTAL = 0


def lang_switch():
    global LANG
    if LANG == 'Ru':
        b_lang.config(text='En')
        LANG = 'En'
    else:
        b_lang.config(text='Ru')
        LANG = 'Ru'


def next_row(df, erl):
    global CURRENT_ROW, SCORE, TOTAL, LANG, t_translate, t_description, scoreLabel
    CURRENT_ROW = random.randint(0, len(df))

    tmp_erl = random.randint(1, 10)
    if len(erl) != 0 and tmp_erl <= 1 + len(erl):  # we show words from errorlist more often (20%) then others
        ind_erl = random.randint(0, len(erl) - 1)
        CURRENT_ROW = erl[ind_erl]
        del erl[ind_erl]

    if LANG == 'Ru':
        b_main.config(text=get_word(df, CURRENT_ROW)[0])
    else:
        b_main.config(text=get_word(df, CURRENT_ROW)[1])

    t_translate.delete("1.0", "end")
    t_description.delete("1.0", "end")

    SCORE += 1
    TOTAL += 1

    scoreLabel.config(text=f'{SCORE} / {TOTAL}')


def show_word(df):
    global CURRENT_ROW, LANG, t_translate, t_description
    if LANG == 'Ru':
        t_translate.insert(tkinter.INSERT, get_word(df, CURRENT_ROW)[1])

    else:
        t_translate.insert(tkinter.INSERT, get_word(df, CURRENT_ROW)[0])

    t_description.insert(tkinter.INSERT, get_word(df, CURRENT_ROW)[2])


def add_word_to_errorlist(df, erl):
    global CURRENT_ROW, SCORE
    erl += [CURRENT_ROW]
    SCORE -= 1
    next_row(df, erl)



if __name__ == '__main__':
    root = Tk()
    root.geometry("750x400")

    data = init(LINK)

    errorlist = []

    myLabel = Label(root, text='Memorize Words Program')
    myLabel.pack()

    scoreLabel = Label(root, text=f'{SCORE} / {TOTAL}')
    scoreLabel.place(x=600, y=200)

    b_lang = Button(root, text='Ru', command=lang_switch)
    b_lang.place(x=10, y=10)

    b_next = Button(root, text='correct', command=lambda: next_row(data, errorlist), bg='green')
    b_next.place(x=600, y=100)

    b_error = Button(root, text='error', command=lambda: add_word_to_errorlist(data, errorlist), bg='red')
    b_error.place(x=600, y=140)

    b_main = Button(root, text='START', height=7, width=50, command=lambda: show_word(data))
    b_main.place(x=200, y=100)

    l_translate = Label(text='translation')

    l_description = Label(text='description')

    t_translate = st.ScrolledText(root,
                                  width=30,
                                  height=2,
                                  font=("Times New Roman", 20))
    t_translate.place(x=165, y=250)

    t_description = st.ScrolledText(root,
                                    width=30,
                                    height=2,
                                    font=("Times New Roman", 20))
    t_description.place(x=165, y=320)

    root.bind('<Shift_R>', lambda event: show_word(data))
    root.bind('<Right>', lambda event: next_row(data, errorlist))
    root.bind('<Down>', lambda event: add_word_to_errorlist(data, errorlist))

    root.mainloop()
