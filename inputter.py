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
dates=[]

def extractDates():
    for i in arr:
        if i['Date'] not in dates:
            dates.append(i['Date'])
    #print(dates)
extractDates()




for i in arr:
    print('Hi')
    print(i['Username'])
    dat='05/10/21'
    if i[f'{dat}'] in final:
        print('Hi')
    else:
        print('hello')

l='''
def dictFinal():
    dat=dates
    
    for i in arr:
        if i['Date'] in dates:
            #print(i['Username'])
            names.append(i['Username'])
    final['{dat}'.format(dat=dat)]=names
    #print(final)
'''



print(dates)

#dictFinal()

print(final)


#dictFinal('05/10/21')