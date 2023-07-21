import pandas as pd
from tkinter import *

test = excel = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vSxkQ0HG2Mc1LSeRpLR4RNZQbcJFnoOP6deJEYIoTGYlOYDoiUIds03tAjF_z4Co2O0fYP9E5wFlwXX/pub?output=xlsx')
print(test.head(4))

root = Tk()
root.geometry("500x200")

myLabel = Label(root, text='Hello')
myLabel.pack()

root.mainloop()



