import datetime
import matplotlib.pyplot as plt
import time
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
    for each in dates:
        legnth_of_data_set=len(data)
        names1=[]
        names2=[]
        temp=0
        while temp<legnth_of_data_set:
            if each==data[temp][0] and data[temp][1].startswith('11'):
                name=data[temp][2]
                name=name.split('#')[0]
                name=name.lower()
                names1.append(name)
                names1=list(set(names1))
            elif each==data[temp][0] and data[temp][1].startswith('15'):
                name=data[temp][2]
                name=name.split('#')[0]
                name=name.lower()
                names2.append(name)
                names2=list(set(names2))
            temp+=1
        attendance[f'{each}']=[names1,names2]      
    return(attendance)

def initialize():
    input_csv()
    to_get_dates()
    to_get_names()
    to_get_dict()


def search_by_name(name):
    try:
        name=name.lower()
        counter, total_counter = 0, len(dates*2)
        for date in dates:
            for each_attendance in attendance[f'{date}']:
                for each in each_attendance:
                    if name in each:
                        counter+=1
        return counter
    except Exception as error:
        print("Something went wrong in search_by_name")

def overall_attendance():
    try:
        for each in names:
            count=0
            count=search_by_name(each)
            attendees[f'{each}']=count
        return attendees
    except Exception as error:
        print("Something went wrong in overall attendance")

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
    x, y = [],[]
    for each in names:
        count=search_by_name(each)
        y.append(count)
        x.append(each)
    y.append((len(dates)*2))
    x.append('Total shifts')
    plt.title('Overall attendance in Bar Chart')
    plt.barh(x, y, color ='green')
    plt.show()

def visualize_pie_graph_search_by_name(name):
    count=search_by_name(name)
    y = [len(dates*2),count]
    mylabels = [f"{name} {count}",f"overall attendance {len(dates*2)}"]
    plt.title('Employee attendance in Pie Chart')
    plt.pie(y, labels = mylabels,  startangle = 0)
    plt.show() 


def compare(names_to_compare):
    x,y = [],[]
    for name in names_to_compare:
        name=name.lower()
        counter=search_by_name(name)
        x.append(name)
        y.append(counter)
    x.append('Total dates')
    y.append(len(dates)*2)
    plt.title('Comparision of attendance in bar Chart')
    plt.barh(x,y,color ='Red')
    plt.show()

def pie_compare(namess):
    y,mylabels=[],[]
    for name in namess:
        name=name.lower()
        count=search_by_name(name)
        print(count)
        y.append(count)
        mylabels.append(f"{name} {count}")
    plt.title('Comparision of attendance in Pie Chart')
    plt.pie(y, labels = mylabels,  startangle = 0)
    plt.show() 

def weekly_bar():
    weekly_attendees={}
    weekly_name=[]
    
    dated=weekly_attendance()
    for date in dated:
        for each_attendance in attendance[f'{date}']:
            for each in each_attendance:
                weekly_name.append(each)
    
    for each in names:
        counter=0
        counter=weekly_name.count(each)
        weekly_attendees[f'{each}']=counter
    y =list(weekly_attendees.values())

    x =list(weekly_attendees.keys())

    y.append(10)
    x.append('Total attendance')
    plt.barh(x,y, color='brown')
    plt.title('Total Weekly Attendance')
    plt.show()



def cli_conversion():
    choice = None
    while choice != 0:
        try:
            time.sleep(.5)
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
            print('For exiting press 0') 
            choice = int(input("Enter selection: "))
        except Exception as error:
            print("Wrong input enter. Please try again")
        

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
            weekly_bar()
        elif choice ==9:
            names_to_compare=input('Enter name you want to compare seperated by a (,)   ->     ')
            names_to_compare=names_to_compare.split(',')
            compare(names_to_compare)
        elif choice ==10:
            names_to_compare=input('Enter name you want to compare seperated by a (,)   ->     ')
            names_to_compare=names_to_compare.split(',')
            pie_compare(names_to_compare)
        elif choice ==0:
            exit(0)
        else:
            print('wrong input. Please try again')

# Driver code
if __name__ == '__main__':
    initialize()
    cli_conversion()
