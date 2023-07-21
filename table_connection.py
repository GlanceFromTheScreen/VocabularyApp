import pandas as pd

LINK = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSxkQ0HG2Mc1LSeRpLR4RNZQbcJFnoOP6deJEYIoTGYlOYDoiUIds03tAjF_z4Co2O0fYP9E5wFlwXX/pub?output=xlsx'


def init(link):
    df = pd.read_excel(link)
    return df.fillna('')


def get_word(df, index):
    return df.loc[index][0], df.loc[index][1], df.loc[index][2]


