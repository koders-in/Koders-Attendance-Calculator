import sys,os
import datetime

# GLOBAL VALUES
data=[]
attendance={}

def input_csv():
    with open("./data.csv", "r") as file:
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
            total_counter += 1 # bug here
            if each[2].startswith(name):
                counter=counter+1
        print("Searched name: " + name ,", " + str(counter) + "/" + str(total_counter))
    except Exception as error:
        print("Something went wrong")
        print("Error" + str(error))


def to_get_dict():
    names=[]
    #creating a dictionary for unique items as atendance
    for each in data:
        splitter=each[1].split(':')
        if  splitter[0]=='11':
            names.append(each[2])
            names=list(set(names))
        elif splitter[0]=='15':
            names.append(each[2])
            names=list(set(names))        
        attendance[f'{each[0]}']=names

def overall_attendance():
    temp=0
    attendees={}
    try:
    #creatung a dictionary for unique items as atendance
        to_get_dict()
        keysList = list(attendance.keys())
        #counting each person's attendance and storing in atendees
        for each in keysList:
            temp=0
            legnth=len(attendance.get(each))     
            while temp<legnth:
                names=attendance.get(each)[temp]            
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
    print(dated)
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
    print(dated)
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

    # to get object of dates of last 30 days
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
    print(dated)
    for each in dated:
        try:
            print(attendance[f'{each}'])
        except Exception as error:
            print("Error" + str(error))
    

# TODO
# def visualize_bar

# TODO
# def visualize_pie

# TODO
# Name: Benzee
# Date: 12/05/20
# Shift: 1- Morning, 2- Post Lunch
# Present
# Absent

# TODO
# cli conversion


# search_by_name("BenZee") # For testing

# Driver code
if __name__ == '__main__':
    input_csv()
    to_get_dict()
    # search_by_name('BenZee')
    # overall_attendance()
    weekly_attendance()
    # monthly_attendance()
    # yearly_attendance()


# TODO
#deepak check the to_det_dict function to get the correct output
#check the output by matching with data.csv to see it is showing correct output according to entries on a particular day