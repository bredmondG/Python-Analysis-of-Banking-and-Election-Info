import csv

#from tqdm import tqdm

row_count = 0
candidates = {}

def candidate_count(row):
    if  candidates.get(row[2]) == None:
        candidates[row[2]] = 1
    else:
        candidates[row[2]] += 1

with open("/Users/brendangold/DENVDEN201905DATA4/Homework/3 Python  6-18/PyPoll/Resources/election_data.csv", "r") as f:
    reader = csv.reader(f)
    
    next(reader)
    
    for row in reader:
        candidate_count(row)
        row_count += 1

def winner():
    value = max(list(candidates.values()))
    for key, val in candidates.items():
        if val == value:
            return(key, val)

print("Total Votes:", row_count)
for key, val in candidates.items():
    print(key, ":", val, (round(val / row_count * 100)), "%")
print("Winner:", winner())

