import csv 
import json  
import pandas as pd

import sys,os
file_address=os.path.join(sys.path[0], "Attendance_Sheet.csv")

print(file_address)

arr=[]

#'C:/Users/ASUS/Attendance/Koders-Attendance-Calculator/Attendance_Sheet.csv'
def Inpput():
    boston=pd.read_csv(file_address)
    l=len(boston)
    i=0
    for ind, row in boston.iterrows():
        arr.append(row)
            
Inpput()

final={}
dates=[]

def extract_Dates():
    for i in arr:
        if i['Date'] not in dates:
            dates.append(i['Date'])
    
extract_Dates()


def To_Dict():
    c=0
    r=0
    for j in dates:
        names=[]
        for i in arr:
            
            
            if i['Date'] == j:
                names.append(i['Username'])
            c+=1
            final[f'{j}']=names
            if(r<len(dates)-1):
                r=r+1

To_Dict()
    

attenden={}

def attend():
    
    for i in dates:
        j=0
        l=len(final.get(i))
        
        while j<l:
            n=final.get(i)[j]
            j+=1
            
            if n not in attenden:
                attenden[f'{n}']=1
            else:
                attenden[f'{n}']+=1
    print(attenden)


    
    
attend()
