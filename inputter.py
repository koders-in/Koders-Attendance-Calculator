import csv 

import pandas as pd

arr=[]


def Inpput():
    boston=pd.read_csv('C:/Users/ASUS/Attendance/Koders-Attendance-Calculator/Attendance_Sheet.csv')
    l=len(boston)
    i=0
    for ind, row in boston.iterrows():
        arr.append(row)
            
Inpput()
print(arr)

def reall():
    l=len(arr)
    c=0
    dat=""
    #print(arr[2])
        

reall()