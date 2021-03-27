#Bryan Price

import csv

def readData():
    fields = ("name", "toll", "date")
    f = open("toll-records.txt", "r")
    tolls = []
    dReader = csv.DictReader(f, fieldnames=fields, delimiter="\t")

    for row in dReader:
        tolls.append(row)

    f.close()
    return tolls

def displayData(trips):
    fs= "%-8s %-10s %7s"
    print(fs % ("Name", "Toll", "Date"))
    for t in trips:
        fs = "%-8s %-10s %6s"
        print(fs % (t['name'], t['toll'], t['date']))

def calcToll(trips):
    drv = input("Enter user's name: ")

    for name in trips:
        if name == alice:
            totaltoll = 
    
    
    print("%s made %s trips. Paid %d in total tolls." % (drv, totaltoll, fine))
    
    return(fine)

    

def addToll(trips):
    nom = input("Enter your name: ")
    paid = input("Enter amount of toll paid: ")
    day = input("Enter date of toll in mm/dd/yyyy fromat: ")
    record = {'name': nom, 'toll': paid, 'date': day}
    trips.append(record)
    return trips

def storeData(trips):
    fields = ("name", "toll", "date")
    f = open("toll-records.txt", "w")
    dWriter = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    dWriter.writerows(trips)

    f.close()

def main():

    toll_log = readData()

    while True:
        print("""
        Menu options.  Choose 1,2, 3, or 4
            1.Display all user data
            2.Calculate user tolls
            3.Add a toll
            4.Save and exit

        """)

        opt = input("   Enter your choice, 1, 2, 3, or 4: ")

        if opt == "1":
            print()
            displayData(toll_log)
        elif opt == "2":
            calcToll(toll_log)
            
        elif opt == "3":
            toll_log = addToll(toll_log)
        elif opt == "4":
            storeData(toll_log)
            print("Goodbye")
            print()
            break
        else:
            print("Invalid entry, please re-enter your choice")
            print()

main()
    
                
                    


