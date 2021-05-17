import csv 
import json  
import pandas as pd
import sys,os

file_address=os.path.join(sys.path[0], "Attendance_Sheet.csv")
# print(file_address)

final={}
dates=[]

def input():
    boston=pd.read_csv(file_address)
    l=len(boston)
    for ind, row in boston.iterrows():
        arr.append(row)

def extract_Dates():
    for i in arr:
        if i['Date'] not in dates:
            dates.append(i['Date'])
    

def to_dict():
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
to_dict()

attendance={}
def attend():
    for i in dates:
        j=0
        l=len(final.get(i))
        
        while j<l:
            n=final.get(i)[j]
            j+=1
            if n not in attendance:
                attendance[f'{n}']=1
            else:
                attendance[f'{n}']+=1
    print(attendance)

input()
extract_Dates()
attend()
