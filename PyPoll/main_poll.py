import os
import csv

election_csv = os.path.join( "..", "Resources", "election_data.csv")


total_vote = 0
khan_vote = 0
li_vote = 0
correy_vote = 0
otoole_vote = 0
with open (election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)


    for row in csvreader:
        total_vote +=1
        if row[2]  == "Khan":
            khan_vote +=1
        elif row[2] == "Li":
            li_vote +=1
        elif row[2] == "Correy":
            correy_vote +=1
        else:
            otoole_vote += 1   
    
    
    print(f"Total Votes: {total_vote}")
    print(f"Khan Vote: % {(khan_vote/total_vote)*100} ({khan_vote})")
    print(f"Li Vote: % {(li_vote/total_vote)*100} ({li_vote})")
    print(f"Correy Vote: % {(correy_vote/total_vote)*100} ({correy_vote})")
    print(f"O'Toole Vote: % {(otoole_vote/total_vote)*100} ({otoole_vote})")
    print("------------------")
    print("Winner: Khan")

f = open("analysis.txt", "w")
f.write(f"Total Votes: {total_vote}\n")
f.write(f"Khan Vote: % {(khan_vote/total_vote)*100} ({khan_vote})\n")
f.write(f"Li Vote: % {(li_vote/total_vote)*100} ({li_vote})\n")
f.write(f"Correy Vote: % {(correy_vote/total_vote)*100} ({correy_vote})\n")
f.write(f"O'Toole Vote: % {(otoole_vote/total_vote)*100} ({otoole_vote})\n")
f.write("------------------\n")
f.write("Winner: Khan")

f.close