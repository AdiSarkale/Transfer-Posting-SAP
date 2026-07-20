import pandas as pd
import openpyxl
def readFile(file):
    df = pd.read_csv(file)
    # print(df.head())
    r = df.to_dict()
    return r
