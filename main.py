import sys,os
import datetime
from typing import Counter



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

def to_get_dates():
    for each in data:
        if each[0] not in dates:
            dates.append(each[0])

def to_get_names():
    
    for each in data:
        if each[2] not in names:
            name=each[2]
            name=name.split('#')[0]
            name=name.lower()
            names.append(name)





def to_get_dict():
    
    
    for eachh in dates:
        legnth_of_data_set=len(data)
        names1=[]
        names2=[]
        temp=0
        while temp<legnth_of_data_set:
            if eachh==data[temp][0] and data[temp][1].startswith('11'):
                name=data[temp][2]
                name=name.split('#')[0]
                name=name.lower()
                names1.append(name)
                names1=list(set(names1))
            elif eachh==data[temp][0] and data[temp][1].startswith('15'):
                name=data[temp][2]
                name=name.split('#')[0]
                name=name.lower()
                names2.append(name)
                names2=list(set(names2))
            temp+=1
        attendance[f'{eachh}']=[names1,names2]      
    
    return(attendance)

def search_by_name(name):
    try:
        name=name.lower()
        counter, total_counter = 0, len(dates*2)
        for each in dates:
            for eachh in attendance[f'{each}']:
                for eachhh in eachh:
                    if name in eachhh:
                        counter+=1
                
            
        
        return counter
    except Exception as error:
        print("Something went wrong")
        print("Error" + str(error))


        




def overall_attendance():
     
    try:
        for each in names:
            count=0
            count=search_by_name(each)
            attendees[f'{each}']=count
        return attendees
    except Exception as error:
        print("Something went wrong")

def weekly_attendance():
    current_date = datetime.datetime.today()
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
            print("No data Found for ->   " + str(error))
    return dated

def yearly_attendance():
    current_date = datetime.datetime.today()
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
            print("No data Found for ->   " + str(error))
    return(dated)

def monthly_attendance():
    current_date = datetime.datetime.today()
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
            print("No data Found for ->   " + str(error))
    return(dated)


def visualize_bar_overall_attendance():
    x=[]
    y=[]
    for each in names:
        count=search_by_name(each)
        y.append(count)
        x.append(each)
    y.append((len(dates)*2))
    x.append('Total shifts')
    plt.barh(x, y)
    plt.show()

def visualize_pie_graph_search_by_name(name):
    count=search_by_name(name)
    print(count)
    y = [len(dates*2),count]
    mylabels = [f"{name} {count}",f"overall attendance {len(dates*2)}"]

    plt.pie(y, labels = mylabels,  startangle = 0)
    plt.show() 


def compare(names_to_compare):
    x,y=[],[]
    for name in names_to_compare:
        name=name.lower()
        counter=search_by_name(name)
        x.append(name)
        y.append(counter)
    x.append('Total dates')
    y.append(len(dates)*2)
    plt.barh(x,y)
    plt.show()

def pie_compare(namess):
    y=[]
    mylabels=[]
    for name in namess:
        name=name.lower()
        count=search_by_name(name)
        print(count)
        y.append(count)
        mylabels.append(f"{name} {count}")

    plt.pie(y, labels = mylabels,  startangle = 0)
    plt.show() 


def weeklY_bar():
    weekly_attendees={}
    
    dated=weekly_attendance()
    #print(dated)
    
    for each in dated:
        
        for name in names:
            counter=0
            for eachh in attendance[f'{each}']:
                
                for eachhh in eachh:
                    
                    if name in eachhh:
                        counter+=1
                    weekly_attendees[f'{name}']=counter

    y =list(weekly_attendees.values())

    x =list(weekly_attendees.keys())
    
    plt.barh(x,y)
    plt.show()


future_featur='''
def monthly_bar():
    monthly_attendees={}
    
    dated=monthly_attendance()
    for each in dated:
        
        for name in names:
            counter=0
            for eachh in attendance[f'{each}']:
                
                for eachhh in eachh:
                    
                    if name in eachhh:
                        counter+=1
                monthly_attendees[f'{name}']=counter

    y =list(monthly_attendees.values())

    x =list(monthly_attendees.keys())
    

    plt.barh(x,y)
    plt.show()
'''

def cli_conversion():
    while True:
        print('Do you want to continue: Y/N')
        print("For Attendance by name press 1")
        print("For total attendance press 2")
        print("For weekly attendance press 3")
        print("For monthly attendance press 4")
        print('For yearly attendance press 5')
        print('For overall attenadce graph press 6')
        print('For pie graph for person press 7')
        print('For weekly bar graph of week press 8')
        print('For bar graph of comparision press 9')
        print('For pie graph of comparision press 10')

        choice=int(input('Enter:  '))

        if choice ==1:
            name=input('Enter name:   ')
            counter=search_by_name(name)
            print("Searched name: " + name ,", " + str(counter) + "/" + str(len(dates)*2))
        elif choice ==2:
            print(overall_attendance())
        elif choice ==3:
            weekly_attendance()
        elif choice ==4:
            monthly_attendance()
        elif choice ==5:
            yearly_attendance()
        elif choice ==6:
            visualize_bar_overall_attendance()
        elif choice ==7:
            visualize_pie_graph_search_by_name(input('Enter name:   '))
        elif choice ==8:
            weeklY_bar()
        elif choice ==9:
            names_to_compare=input('Enter name you want to compare seperated by a (,)   ->     ')
            names_to_compare=names_to_compare.split(',')
            compare(names_to_compare)
        elif choice ==10:
            names_to_compare=input('Enter name you want to compare seperated by a (,)   ->     ')
            names_to_compare=names_to_compare.split(',')
            pie_compare(names_to_compare)
        else:
            print('wrong input')

        print('Do you want to continue: Y/N')
        to_continue=input('Enter:   ').capitalize()
        if to_continue=='N':
            break



# Driver code
if __name__ == '__main__':
    input_csv()
    to_get_dates()
    to_get_names()
    to_get_dict()
    # search_by_name('Ritesh')
    # overall_attendance()
    # weekly_attendance()
    # visualize_bar_weekly_attendance()
    # monthly_attendance()
    # yearly_attendance()
    cli_conversion()
    # visualize_bar_overall_attendance()
    # visualize_pie_graph_search_by_name('XHunter')
    # weeklY_bar()
    #monthly_bar()
    #compare('Ritesh','BenZee')


