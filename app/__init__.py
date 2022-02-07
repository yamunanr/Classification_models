import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename


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
