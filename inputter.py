import csv 

import pandas as pd

arr=[]


def Inpput():
    boston=pd.read_csv('C:/Users/ASUS/Attendance/Koders-Attendance-Calculator/Attendance_Sheet.csv')
    l=len(boston)
    i=0
    for ind, row in boston.iterrows():
        while i<l:
            #print(row)
            arr.append(row)
            i+=1
Inpput()

def reall():
    l=len(arr)
    c=0
    dat=""
    print(dat)
    
    for i in arr:
        if dat=="":
            dat=i[0]
            print(dat)
            
        

reall()