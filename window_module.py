import tkinter
from tkinter import *
import tkinter.scrolledtext as st
from table_connection import init, get_word, LINK
import random

random.seed()
LANG = 'Ru'  # Ru En
STATE = 'Say'  # Write
CURRENT_ROW = 0


def lang_switch():
    global LANG
    if LANG == 'Ru':
        b_lang.config(text='En')
        LANG = 'En'
    else:
        b_lang.config(text='Ru')
        LANG = 'Ru'


def next_row(df):
    global CURRENT_ROW
    global LANG
    global t_translate
    global t_description

    CURRENT_ROW = random.randint(0, len(df))

    if LANG == 'Ru':
        b_main.config(text=get_word(df, CURRENT_ROW)[0])
    else:
        b_main.config(text=get_word(df, CURRENT_ROW)[1])

    t_translate.delete("1.0", "end")
    t_description.delete("1.0", "end")


def show_word(df):
    global CURRENT_ROW
    global LANG
    global t_translate
    global t_description

    if LANG == 'Ru':
        t_translate.insert(tkinter.INSERT, get_word(df, CURRENT_ROW)[1])
        # t_translate.config(text=get_word(df, CURRENT_ROW)[1], font=('Arial', 20))
    else:
        t_translate.insert(tkinter.INSERT, get_word(df, CURRENT_ROW)[0])
        # t_translate.config(text=get_word(df, CURRENT_ROW)[0], font=('Arial', 20))

    # t_translate.place(x=200, y=250)

    # l_description.config(text=get_word(df, CURRENT_ROW)[2], font=('Arial', 20))
    # l_description.place(x=200, y=320)
    t_description.insert(tkinter.INSERT, get_word(df, CURRENT_ROW)[2])


if __name__ == '__main__':
    root = Tk()
    root.geometry("750x400")

    data = init(LINK)

    myLabel = Label(root, text='Memorize Words Program')
    myLabel.pack()

    b_lang = Button(root, text='Ru', command=lang_switch)
    b_lang.place(x=10, y=10)

    b_next = Button(root, text='next', command=lambda: next_row(data))
    b_next.place(x=600, y=100)

    b_main = Button(root, text='START', height=7, width=50, command=lambda: show_word(data))
    b_main.place(x=200, y=100)

    l_translate = Label(text='translation')
    # l_translate.place(x=200, y=250)

    l_description = Label(text='description')
    # l_description.place(x=200, y=320)

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

    root.mainloop()
