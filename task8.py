import csv

def read_csv_file (filename):  
    with open(filename,"r") as file:
     reader = csv.DictReader(file)
    
     for row in reader:
        print(row)
        
read_csv_file(".vscode/py/file.csv")
        
