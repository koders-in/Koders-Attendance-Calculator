import sys,os
import datetime

import pandas as pd

import matplotlib.pyplot as plt

#date = datetime.datetime(int(year), int(month), 1)

# GLOBAL VALUES
data=[]
dates=[]
names=[]
attendance={}
attendees={}

def input_csv():
    with open("data.csv", "r") as file:
        for line in file.readlines():
            data.append(line.split(","))
        del data[0]

# TODO
# Handle unique values

def search_by_name(name):
    try:
        name=name
        counter, total_counter = 0,0
        for each in data:
            total_counter += 1
            if each[2].startswith(name):
                counter=counter+1
        print("Searched name: " + name ,", " + str(counter) + "/" + str(total_counter-1))
    except Exception as error:
        print("Something went wrong")
        print("Error" + str(error))

def to_get_dates():
    for each in data:
        if each[0] not in dates:
            dates.append(each[0])

def to_get_names():

    for each in data:
        if each[2] not in names:
            names.append(each[2])
        


def to_get_dict():
    
    
    for eachh in dates:
        legnth_of_data_set=len(data)
        names1=[]
        names2=[]
        morning_shift={}
        evening_shift={}
        temp=0
        while temp<legnth_of_data_set:
            if eachh==data[temp][0] and data[temp][1].startswith('11'):
                names1.append(data[temp][2])
                names1=list(set(names1))
            elif eachh==data[temp][0] and data[temp][1].startswith('15'):
                names2.append(data[temp][2])
                names2=list(set(names2))
            temp+=1
        morning_shift['Morning Shift']=names1
        evening_shift['Evening Shift']=names2
        attendance[f'{eachh}']=[morning_shift,evening_shift]      
    #print(attendance)


def overall_attendance():
    temp=0
    
    try:
    #creatung a dictionary for unique items as atendance
        to_get_dict()
        
        for each in data:
            legnth=len(names)
            while temp<legnth:
                if each[2]==names[temp]:            
                    if names not in attendees:
                        attendees[f'{names}']=1
                    else:
                        attendees[f'{names}']+=1
                temp+=1
        print(attendees)
    except Exception as error:
        print("Something went wrong")

def weekly_attendance():
    current_date = datetime.datetime.today()
    attendees = {}
    week_dates = []
    dated = []
    temp = 0

    # to get object of dates of last 7 days
    while temp < 7:
        previous_date = current_date - datetime.timedelta(days=temp)
        week_dates.append(previous_date)
        temp+=1

    #to convert datetime object into the correct format as required
    for each in week_dates:
        day = each.strftime("%A")
        if day != "Sunday" and day != "Saturday":
            formatted_time = each.strftime("%m/%d/%y")
            dated.append(str(formatted_time))
    
    for each in dated:
        try:
            print(attendance[f'{each}'])
        except Exception as error:
            print("Error" + str(error))

def yearly_attendance():
    current_date = datetime.datetime.today()
    attendees = {}
    week_dates = []
    dated = []
    temp = 0

    # to get object of dates of last 365 days
    while temp < 365:
        previous_date = current_date - datetime.timedelta(days=temp)
        week_dates.append(previous_date)
        temp+=1

    #to convert datetime object into the correct format as required
    for each in week_dates:
        day = each.strftime("%A")
        if day != "Sunday" and day != "Saturday":
            formatted_time = each.strftime("%m/%d/%y")
            dated.append(str(formatted_time))
    
    for each in dated:
        try:
            print(attendance[f'{each}'])
        except Exception as error:
            print("Error" + str(error))


def monthly_attendance():
    current_date = datetime.datetime.today()
    attendees = {}
    week_dates = []
    dated = []
    temp = 0

    # to get object of dates of last 7 days
    while temp < 30:
        previous_date = current_date - datetime.timedelta(days=temp)
        week_dates.append(previous_date)
        temp+=1

    #to convert datetime object into the correct format as required
    for each in week_dates:
        day = each.strftime("%A")
        if day != "Sunday" and day != "Saturday":
            formatted_time = each.strftime("%m/%d/%y")
            dated.append(str(formatted_time))
    
    for each in dated:
        try:
            print(attendance[f'{each}'])
        except Exception as error:
            print("Error" + str(error))


# TODO


# TODO
# def visualize_pie



# TODO
def cli_conversion():
    while True:
        print('Do you want to continue: Y/N')
        print("For Attendance by name press 1")
        print("For total attendance press 2")
        print("For weekly attendance press 3")
        print("For monthly attendance press 4")
        print('For yearly attendance press 5')
        choice=int(input('Enter:  '))

        if choice ==1:
            search_by_name(input('Enter name:   '))
        elif choice ==2:
            overall_attendance()
        elif choice ==3:
            weekly_attendance()
        elif choice ==4:
            monthly_attendance()
        elif choice ==5:
            yearly_attendance()
        else:
            print('wrong input')

        print('Do you want to continue: Y/N')
        to_continue=input('Enter:   ').capitalize()
        if to_continue=='N':
            break

# search_by_name("BenZee") # For testing

# Driver code
if __name__ == '__main__':
    input_csv()
    to_get_dates()
    to_get_names()
    to_get_dict()
    # search_by_name('BenZee')
    #overall_attendance()
    # weekly_attendance()
    # monthly_attendance()
    # yearly_attendance()
    cli_conversion()
    

#After reading csv file we moving through graph ploting....!



