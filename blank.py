import csv
#import matplotlib.pyplot as plt
#import numpy as np

options = ["List the constituencies","List the MPS", "List the parties"]
class Constituency:
    def __init__(self,t):
        self.details = t
    def __str__(self):
        return self.details['CName']+" "+self.details['Party']
    def GetCountry(self):
        return self.details['Country']
    def GetType(self):
        return self.details['CType']
        


constituencies = []
#partyToCount = input("Party code to count, Lab, Con, LD, RUK, IND")
parties = ["Lab","Con","LD","RUK","Green","IND","SNP","PC","DUP","SF","SDLP","UUP","APNI"]
mpCount = []
for p in parties:
    mpCount.append(0)
#mpCount = [0,0,0,0,0,0]
with open('ProjectDataFor2024.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        counter1 = 0
        for party in parties:
            if row['First party'].lower() == party.lower():
                mpCount[counter1] += 1
            counter1 += 1    
        constituency = {'CName':row['Constituency name'],'RName':row['Region name'],'Country':row['Country name'],'CType':row['Constituency type'],'Party':row['First party']}
        con = Constituency(constituency)
        constituencies.append(con)
    counter1 = 0
    for party in parties:
        print(party, " got ",mpCount[counter1], " mps")
        counter1 += 1
for con in constituencies:
    print(con)
'''plt.bar(parties,mpCount)
plt.show()
next =input()
plt.pie(mpCount)
plt.show()'''

"""        
for con in constituencies:
    c = con.GetCountry()
    t = con.GetType()
    if c.lower() == "wales":
        print(con," is in ",c, " and is a ",t)


def PrintMenuAndGetResponse():
    choice = -1
    
    while choice < 0 or choice >= len(options):
        print("Welcome to the Election Analysis App")
        print("Choose your option - use the number")
        print("Option Number\tOption")
        optionNumber = 0
        for option in options:
            print(optionNumber,":\t\t",option)
            optionNumber += 1
        try:
            choice = int(input("Enter your choice: "))
        except:           
            choice = -1
        if choice < 0 or choice >= len(options):
            print("Not a valid choice")
    return choice

LoadFile()

c = PrintMenuAndGetResponse()
print("you chose ",options[c])
"""                   
