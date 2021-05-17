import csv 

import pandas as pd

arr=[]

def Inpput():
    boston=pd.read_csv('C:/Users/ASUS/Attendance/Koders-Attendance-Calculator/Attendance_Sheet.csv')
    for ind, row in boston.iterrows():
        if ind==0:
            print(row)
            arr.append(row)
Inpput()

