import os
import csv

election_csv = os.path.join( "..", "Resources", "election_data.csv")


total_vote = 0
Khan_vote = 0
Li_vote = 0
Correy_vote = 0
OToole_vote = 0
with open (election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)


    for row in csvreader:
        total_vote +=1
        if row[2]  == "Khan":
            Khan_vote +=1
        elif row[2] == "Li":
            Li_vote +=1
        elif row[2] == "Correy":
            Correy_vote +=1
        else:
            OToole_vote += 1   
              
    print(total_vote)
    print(f"Khan Vote: % {(Khan_vote/total_vote)*100}")
    print(f"Li Vote: % {(Li_vote/total_vote)*100}")
    print(f"Correy Vote: % {(Correy_vote/total_vote)*100}")
    print(f"O'Toole Vote: % {(OToole_vote/total_vote)*100}")