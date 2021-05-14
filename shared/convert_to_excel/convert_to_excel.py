import pandas as pd
import os

def convert_csv_to_excel():
    path = os.path.dirname(os.path.realpath('__file__'))
    print(path)
    folder = os.path.join(path,'data_collected\\records\\')
    print(folder)
    read_file = pd.read_csv (folder+'records.csv')
    read_file.to_excel (folder+'records.xlsx', index = None, header=True)