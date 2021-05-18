import sys,os

# GLOBAL VALUES
data=[]

def input_csv():
    with open(file_address, "r") as file:
        for line in file.readlines():
            data.append(line.split(","))


# TODO
# Handle unique values
def search_by_name(name):
    try:
        counter, total_counter = 0,0
        for each in data:
            total_counter += 1
            if each[2].startswith(name):
                counter=counter+1
        print("Searched name: " + name ", " + counter + "/" + total_counter)
    except Exception as error:
        print("Something went wrong")


# TODO
# def overall attendance
# Usage: dictionary, set
# split(":")[0] - 11, 3

# TODO
# def weekly_attendance

# TODO
# def yearly_attendance

# TODO
# def monthly_attendance

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
