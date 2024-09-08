#Bill Nguyen | 9/3/2024 | Assignment 1 
import csv #Imported the csv and math libraries
import math

def fetchData(): #This function will fetch 
    try: #budget_data.csv data as sales
        with open("PyBank/resources/budget_data.csv", "r") as sales: #Opens the file as sales
            fetch = csv.reader(sales) #It will puts it into a csv reader as fetch
            next(fetch) #Skip header
            data = [] #Created empty list
            for dates in fetch: #the dates in the fetch data is 
                data.append(dates) #appended to the data list
        return data #And it will be returned
    except FileNotFoundError: #If the file is not founder
        print("The file was not found.") #It will print out this error
    except IOError:
        print("An error occurred while reading the file.")

def toFile(): #This function is made to create the new Analytics.txt file
    newFile = open("PyBank/analytics/analytics.txt","w")
    newFile.writelines(f"Financial Analytics\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n") #This is the header line
    newFile.close() #and close it once it has been created
    return newFile

def totalMonths(data): #This function will count up all the total data with in the data list
    months = len(data) #months the total count of each row in data
    print(f"Total Months: {months}")
    newFile = open("PyBank/analytics/analytics.txt","a").writelines(f"Total Months: {months}\n")
    #These will be output to the an output file and terminals then close the file

def netAmount(data):#This will sum up the total amount overall in the data
    amount = [] #an empty amount list
    for dates, values in data: #for each dates, and values in data
        amount.append(int(values)) #THe values will be turned into an integer and be appended to the amount list
        net = sum(amount)#this will be added up as net worth
    print(f"Total Net Amount: {net}")
    open("PyBank/analytics/analytics.txt","a").writelines(f"Total Net Amount: {net}\n")
    #These will be output to the an output file and terminals then close the file

def totalChangeFunction(data): #This functions acts as a change amount function
    totalChanges = [] #an empty totalchange list
    for values in range(1,len(data)): #for each value in range of 1 and the total row amount in data
        changes = int(data[values][1]) - int(data[values-1][1]) #This will subtract the amount from two periods
        totalChanges.append(changes) #then the change will be appended to the empty list
    return totalChanges

def changeAmount(data, totalChanges): #This will find the amount of change throughout each periods
    if totalChanges: #if there is totalchange
        average = sum(totalChanges)/len(totalChanges) #It will sum up the total changes then divide them by the total rows in the total changes lists
    else: #else average would equal 0
        average = 0
    print(f"Average Change: {average:.2f}") 
    open("PyBank/analytics/analytics.txt","a").writelines(f"Average Change: {average:.2f}\n")
    #These will be output to the an output file and terminals then close the file


def greatestIncrease(data, totalChanges): #This measures the greatest increase of change amount
    increase = max(totalChanges) #increase is the maximum value of said list
    index = totalChanges.index(increase) + 1 #this will add to the index of the change list to match the increase
    dateOfIncrease = data[index][0] 
    print(f"Greatest Increase in Profits: {dateOfIncrease}({increase})")
    open("PyBank/analytics/analytics.txt","a").writelines(f"Greatest Increase in Profits: {dateOfIncrease}({increase})\n")
    #These will be output to the an output file and terminals then close the file

def greatestDecrease(data, totalChanges): #This measures the greatest decrease of change amount
    decrease = min(totalChanges) #decrease is the minumum value of said list
    index = totalChanges.index(decrease) + 1 #this will add to the index of the change list to match the decrease
    dateOfdecrease = data[index][0]
    print(f"Greatest Decrease in Profits: {dateOfdecrease}({decrease})")
    newFile = open("PyBank/analytics/analytics.txt","a").writelines(f"Greatest Decrease in Profits: {dateOfdecrease}({decrease})\n")
    #These will be output to the an output file and terminals then close the file

def pyBank(): #This function acts as binding agent in order to avoid calling data and totalChanges multiple times within other functions where it would be necessary
    data = fetchData()
    totalChanges = totalChangeFunction(data)
    toFile()
    totalMonths(data)
    netAmount(data)
    changeAmount(data, totalChanges)
    greatestIncrease(data, totalChanges)
    greatestDecrease(data, totalChanges)
    
def main():
    while True:
        try:
            pyBank() #Calls the binding functions
            repeat = input("Would you like to see it again?(Y|N)").upper() #WILL AUTOMATICALLY MAKE EVERY REPLY TO THIS CAPITALIZE
            if repeat != 'Y':   
                break
        except ValueError: #Will print an ValueError for an exception
            print("ValueError")

       

        except ZeroDivisionError:  #Will print an ZeroDivisionError for an exception
            print("ZeroDivisionError")     


main()
