import sys,os
import datetime

#date = datetime.datetime(int(year), int(month), 1)

# GLOBAL VALUES
data=[]
attendance={}

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
            total_counter += 1 # bug here
            if each[2].startswith(name):
                counter=counter+1
        print("Searched name: " + name ,", " + str(counter) + "/" + str(total_counter-1))
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
            attendance[f'{each[0]}']=names
        elif splitter[0]=='15':
            names.append(each[2])
            names=list(set(names))        
            attendance[f'{each[0]}']=names
    #print(attendance)

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
    to_get_dict()
    # search_by_name('BenZee')
    # overall_attendance()
    # weekly_attendance()
    #monthly_attendance()
    # yearly_attendance()
    cli_conversion()

#After reading csv file we moving through graph ploting....!

