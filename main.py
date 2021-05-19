import sys,os
import datetime

file_address=os.path.join(sys.path[0], "Attendance_Sheet.csv")
# GLOBAL VALUES
data=[]
attendance={}

def input_csv():
    with open(file_address, "r") as file:
        for line in file.readlines():
            data.append(line.split(","))
        del data[0]


#todo
# Handle unique values
def search_by_name(name):
    try:
        counter, total_counter = 0,0
        for each in data:
            total_counter += 1
            if each[2].startswith(name):
                counter=counter+1
        print("Searched name: " + name ,", " + counter + "/" + total_counter)
    except Exception as error:
        print("Something went wrong")


def to_get_dict():
    names=[]
    
    #creatung a dictionary for unique items as atendance
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
    except Exception as error:
        print("Something went wrong")
    


def weekly_attendance():
    Current_Date = datetime.date.today()
    attendees={}
    week_dates=[]
    dated=[]
    temp=0
    #to get object of dates of last 7 days
    while temp<7:
        Previous_Date = datetime.date.today() - datetime.timedelta(days=temp)
        week_dates.append(str(Previous_Date))
        temp+=1
    #to convert datetime object into the correct format as required
    for each in week_dates:
        each=each.split('-')
        dated.append(str(each[1]+'/'+each[2]+'/'+each[0][2:]))

    for each in dated:
        try:
            print(str(attendance[f'{each}']))
        except:
            print('Leave')
    
 
def yearly_attendance():
    Current_Date = datetime.date.today()
    attendees={}
    week_dates=[]
    dated=[]
    temp=0
    #to get object of dates of last 365 days
    while temp<365:
        Previous_Date = datetime.date.today() - datetime.timedelta(days=temp)
        week_dates.append(str(Previous_Date))
        temp+=1
    #to convert datetime object into the correct format as required
    for each in week_dates:
        each=each.split('-')
        dated.append(str(each[1]+'/'+each[2]+'/'+each[0][2:]))
    for each in dated:
        try:
            print(str(attendance[f'{each}']))
        except:
            print('Leave')
    

def monthly_attendance():
    Current_Date = datetime.date.today()
    attendees={}
    week_dates=[]
    dated=[]
    temp=0
    #to get object of dates of last 30 days
    while temp<30:
        Previous_Date = datetime.date.today() - datetime.timedelta(days=temp)
        week_dates.append(str(Previous_Date))
        temp+=1
    #to convert datetime object into the correct format as required
    for each in week_dates:
        each=each.split('-')
        dated.append(str(each[1]+'/'+each[2]+'/'+each[0][2:]))    
    for each in dated:
        try:
            print(str(attendance[f'{each}']))
        except:
            print('Leave')
    

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
    overall_attendance()
    weekly_attendance()
    monthly_attendance()
    yearly_attendance()