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

final={}
dates=[]

def extractDates():
    for i in arr:
        if i['Date'] not in dates:
            dates.append(i['Date'])
    #print(dates)
extractDates()


def ToDict():
    c=0
    r=0
    for j in dates:
        names=[]
        for i in arr:
            
            #j='05/10/21'
            if i['Date'] == j:
                names.append(i['Username'])
            c+=1
            final[f'{j}']=names
            if(r<len(dates)-1):
                r=r+1

ToDict()
    
#print(c)
#print(names)
#i='05/10/21'

#final[f'{i}']="daksh"

#print(f'{i}')

#print(i['Username'])

#print(dates)

#dictFinal()

print(final)


#dictFinal('05/10/21')