#Bill Nguyen | 9/3/2024 | Assignment 1 
import csv #Imported the csv library

def fetchData(): #This function will fetch the data from the election_data csv file
    try: #It will try to 
        with open("PyPoll/resources/election_data.csv", "r") as results: #Open the election_Data file as Results
            fetch = csv.reader(results) #Which will be fetched
            next(fetch) #and Skip the first line since it's a header line
            data = [] #I have create an empty list to
            for values in fetch: #make each value in our fetched data to
                data.append(values) #be appended to the empty list and
        return data #return the data 
    except FileNotFoundError: #If the file is not founder
        print("FileNotFound") #It will print out this error
    except IOError:
        print("An error occurred while reading the file.")

def createFile(): #This function is made to create the new Analytics.txt file
    newFile = open("PyPoll/analytics/analytics.txt", "w") 
    newFile.writelines(f"Election Results\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n") #This is the header line
    newFile.close()
    return newFile

def totalVotes(data): #This function gathers the total votes overall in the list
    totalVotes = len(data) #The total amount of votes is the lens of the data
    print(f"Election Results\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nTotal Votes: {totalVotes}\n")
    newFile = open("PyPoll/analytics/analytics.txt", "a").writelines(f"Total Votes: {totalVotes}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    #Both with make an output to a file and terminals
    return totalVotes #return the total amount of votes 

def listOfCandidates(data):
    candidates = [] #Creating an empty list to house each candidates
    for values in data: #for the value in data 
        candidate = values[2] #candidate is equal to whoever is in the values 3rd column
        if candidate not in candidates: #if the candidate is not already in candidates list
            candidates.append(candidate) #then it will appended it and
    return candidates #return the data


def votePercentage(data, total, candidates): #This function calculates the vote percentages among the candidates
    topThree = {}
    counts = {candidate: 0 for candidate in candidates} #count is candidates: for each candidate in candidates
    for values in data: #for each value in the data
        candidates = values[2] #each candidate is equal to candidates
        counts[candidates] += 1 #As it will count each vote
    for candidate, votes in counts.items(): #for each candidates and votes in the count dictionary
        percentage = (votes/total)*100 # it will divide the votes by the total votes and multiply it by 100 to get the percentage
        topThree.update({candidate:percentage})
        print(f"{candidate}: {percentage:.3f}% ({votes})\n")
    

        newFile = open("PyPoll/analytics/analytics.txt", "a").writelines(f"{candidate}: {percentage:.3f}% ({votes})\n")
    winner = max(zip(topThree.values(), topThree.keys()))[1]
    print(f"Winner: {winner}")   
    newFile = open("PyPoll/analytics/analytics.txt", "a").writelines(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWinner: {winner}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        #These were used to output each candidates and their voting amount & percentages




def pyPoll(): #This functions acts like a binding agent for the other functions in order to have the data
              #move in one call along with passing their most important values to each other.
    createFile()
    data = fetchData()
    total = totalVotes(data)
    candidates = listOfCandidates(data)    
    votePercentage(data, total, candidates)

def main():
    while True: #While True
        try:
            pyPoll() #Main will try to call the PyPoll function
            repeat = input("Would you like to see it again?(Y|N)").upper() #WILL AUTOMATICALLY MAKE EVERY REPLY TO THIS CAPITALIZE
            if repeat != 'Y':   
                break
        except ValueError: #Will print an ValueError for an exception
            print("ValueError")
        except ZeroDivisionError:  #Will print an ZeroDivisionError for an exception
            print("ZeroDivisionError")     
main()

    