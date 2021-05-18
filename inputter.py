import sys,os


initial_data=[]
final_data=[]

def Input_CSV():
    with open(file_address, "r") as file:
        for i in file.readlines():
            initial_data.append(i)

def split_data():
    for i in initial_data:
        final_data.append(i.split(","))
    del final_data[0]
        

Input_CSV()

split_data()
def Search_by_name(name):
    name=name
    counter=0
    for i in final_data:
        #print(i[2])
        if i[2].startswith(name):
            counter=counter+1
    print(counter)

Search_by_name("BenZee")
