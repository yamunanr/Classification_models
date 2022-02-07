import numpy as np
import pandas as pd
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


def browseFiles():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    print("File has been uploaded!")
    df = pd.read_csv(csv_file_path)
    print(df.head())
    # my_report = sv.analyze(df)
    # my_report.show_html()  # Default arguments will generate to "SWEETVIZ_REPORT.html"
    # profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
    # profile.to_file("eda.html")
    pass


root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set', command=browseFiles).grid(row=1, column=0)
tk.Button(root, text='Close', command=root.destroy).grid(row=1, column=1)
root.mainloop()
