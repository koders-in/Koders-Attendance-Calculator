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
#print(arr[10]['Username'])
names=[]
final={}





dat="05/10/21"
for i in arr:
    if dat== i['Date']:
        #print(i['Username'])
        names.append(i['Username'])
    final['dat']=names
print(final['dat'])