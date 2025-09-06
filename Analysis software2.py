"""Voting Analysis software
This program analyzes voting data from a CSV file to provide constituency information, party statistics, 
and MP details. It calculates totals votes of parties, percentages, and writes results to a text file for reporting.
"""
import csv


#this constituency class take in attribute such as names, regions etc and store them in the __init__ meathod, 
#then return them so they can be called 
class Constituency:
    def __init__(self, name, region, country, types, register_vote):
        
        self.name = name
        self.region = region
        self.country = country
        self.types = types
        self.register_vote = register_vote
    def GetCountry(self):
        return self.country
    def GetRegion(self):
        return self.region
    def GetType(self): 
        return self.types
    def GetName(self):
         return self.name  
    def display_info(self):
        return(f"Constituency name: {self.name}\n" 
               f"Constituency region:{self.region}\n"
               f"Constituency country: {self.country}\n"
               f"Constituency type: {self.types}\n"
               f"Total registed voter: {self.register_vote}")

#The class provides methods to display party names, calculate total votes, and determine vote percentages for a chosen party.
class Party:
    def __init__(self, votes):
        self.name = {1: 'Lab', 2: 'Con', 3 : 'LD', 4: 'RUK', 5: 'Green', 6: 'SNP', 7: 'PC', 8: 'DUP', 9: 'SF', 10 : 'SDLP', 11: 'UUP', 12: 'APNI', 13 : 'Other Party' } 
        self.MP = []
        self.votes = votes
        self.totalVotes = 0
    #this meathod iterate thorough the dictionary using the item() function recommended by google 
    def display_pName(self):
        for key, value in self.name.items():
            print(f'{key}: {value}')
    # this meathod get another input from the user in a form of integer, then calculate the sum and percentage
    # I used co-poilt as a learning tool to help clarify concepts and guide me through structuring parts of this code
    def more_info(self, info):
        self.info = info 
        choice = input(f'Pick a number from the options above to get the sum and percetage of the chosen party: ')
        #party_totalVote = all_vote(info)
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(self.name):  
                Chosen_party = self.name.get(choice, None)
                if not Chosen_party:
                    print("Invalid option. Try again!")
                    return
            else:
                print("Invalid option. Try again!")
                return
        else:
            print("Invalid input. Please enter a number.")
            return

        print(f'\nData for {Chosen_party}:') 

        # Calculate total votes for the chosen party
        all_totalVotes = 0
        for row in info:
            try:
                votes = int(row[Chosen_party])
            except ValueError:
                votes = 0
            all_totalVotes += votes

        party_totalVote = 100000000000
        for row in info:
            for party in self.name.values():
                try:
                    votes = int(row[party])
                except ValueError:
                    votes = 0
                party_totalVote += votes

        # Calculate percentage
        if party_totalVote == 100000000000:
            Vote_percent = (all_totalVotes / party_totalVote) * 100
        else:
           Vote_percent = 0

        print(f'You picked {Chosen_party}')   
        print(f'Total votes for {Chosen_party}: {all_totalVotes}')
        print(f'All party votes: {party_totalVote}')
        print(f'Percentage of votes for {Chosen_party}: as been wrinting to the txt files')
        
        write_info_Tofile(Chosen_party, all_totalVotes, Vote_percent)

#Represents details of an MP (Member of Parliament) including their name, gender,constituency, party, and votes received.
class MP:
    def __init__(self, first_name,sur_name, gender, constituency, party, Receive_vote, ):
        self.first_name = first_name
        self.sur_name = sur_name
        self.gender = gender
        self.constituency = constituency
        self.party = party
        self.Rvote = Receive_vote

    def display_MP_info(self):
        return f"MP Name: {self.first_name}' '{self.sur_name}, Gender: {self.gender}, Mp Party is:{self.party}, Constituency {self.constituency},Vote receieved: {self.Rvote}  "
#this fuction write to a txt file the information of the party chosen including their name, their totla vote and percentage
# i use a youtube vidoe as a guide to help this is the link https://www.youtube.com/watch?v=6jsCbjQB3y0
def write_info_Tofile(partyName, totalVotes, percentage):
        with open('Result.txt', 'w') as file:
               file.write(f'Party: {partyName}\n')
               file.write(f'Total vote: {totalVotes}\n')
               file.write(f'Percentage: {percentage: 2f}%\n')
        print('Successfully write to the file')
#this fuction call the constituecy class object, takes variable that store the csv file as it attribute 
def confunction(data): 
    for char in data:
        con_info = Constituency(char['Constituency name'], char['Region name'], char['Country name'], char['Constituency type'], char['Electorate'])        
        print(con_info.display_info( ))
        print('-'*30)
#this fuction calls the party class object, takes variable that store the csv file as it attribute 
def partyFUnction(data):
    for char in data:
        party_info = Party('Lab')
        party_info.display_pName()
        party_info.more_info(data)
#this fuction calls the mp class object, takes variable that store the csv file as it attribute, process a list of dictionaries then append it 
def mpfunction(data):
    mp_list = []
    for char in data:
        mp_info = MP(char['Member first name'], char['Member surname'],char['Member gender'],char['Constituency name'],char['First party'], char['Valid votes'])
        mp_list.append(mp_info)
        print(mp_info.display_MP_info())
#This function print the welccoming screen, then prompts the user to select an option from a list and also handle situation where there input is invalid
def get_choice(options): 
    while True:
        print('Welcome: I am here to help you. Please pick from this option:')
        for idx, i in enumerate(options, start=1):
            print(idx,i)
        user_input = input(f'please pick a number: ').strip()
        try:
            user_input = int(user_input)
            if 1 <=user_input <= len(options):
                return user_input
            else:
                print('Invalid option, please pick a number') 
        except ValueError:
            print('Not a number, please pick a number')
#this is suppose to read the valid and invaild column
def all_vote(data):
    all_partyVote = 0
    for char in data:
        validVote = float(char['Valid votes'])
        invaildVote = float(char['Invalid votes'])
        all_partyVote += validVote + invaildVote
    return all_partyVote
# this function is use for the main where the options is presented and check the user input with if statement
def menu():
    options = ['Constituency info','Party info','List of MP', 'exit']
    while True:
        user_choice = get_choice(options)
        print(f'User choice:{user_choice}')
        if user_choice == 4:
            print('Exiting the program. Goodbye')
            break
        with open("EditedData.csv", 'r' ,newline='') as csvfile:
            data = csv.DictReader(csvfile)  
            all_total_votes = all_vote(data)
            print('successfully load')
            
            if user_choice == 1:
                print('call function')
                csvfile.seek(0)# this seek function is used to reset the loop and i got this idea with the help of co-pilot
                confunction(data)   
                               
            elif user_choice == 2:
                csvfile.seek(0) # this seek function is used to reset the loop and i got this idea with the help of co-pilot:
                partyFUnction(data)
                        
            elif user_choice == 3:
                csvfile.seek(0)# this seek function is used to reset the loop and i got this idea with the help of co-pilot:
                mpfunction(data)
menu()


  

 