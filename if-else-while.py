# Nathaniel Kickbush
# if-else-while.py
# checking a student name and gpa against qualifiers for deans list or honor roll

import sys

studentRecords = [["Pimento", "Olive" , 2.89] , ["Manage" , "Micro" , 3.54] , ["Feast", "Fancy" , 2.69] , ["Carbuncle" , "Emerald" , 3.95] , ["Jones" , "Davy" , 3.26]]

studentLastNames = ["pimento" , "manage" , "feast" , "carbuncle" , "jones"]

#testName = ["Manage" , "Micro" , 3.54]

def checkGPA():
    
    lastName = getLastName()
    
    if lastName == 'zzz':
        
        print("Exiting...")
        
        sys.exit()
        
    validLast = checkLastName(lastName)
        
    if validLast == False:
            
        print("this name is not on the list")
            
        return
        
    else:
            
        firstName = getFirstName()
            
        if firstName == 'zzz':
            
            print("Exiting...")
    
            sys.exit()
    
    GPA = checkFullName(lastName, firstName)
    
    print(lastName + " " + firstName)
    print(GPA)
    
    if GPA == None:
        
        print("This student does not exist. ")
        

    elif GPA > 3.50:
        
        print(firstName + " " + lastName + " " + "is on the Dean's List. ")
        
    elif GPA > 3.25:
        
        print(firstName + " " + lastName + " " + "is on the Honor Roll. ")
        
    else:
        
        print(firstName + " " + lastName + " " + "is not on either list. ")
        
    return
        
def checkLastName(lastName):
    
    if lastName.lower() in studentLastNames:
        
        return True
    
    else:
        
        return False

def checkFullName(lastName, firstName):
    
    for student in studentRecords:
        
        if student[0] == lastName and student[1] == firstName:
            
            return studentRecords[2]
        
        else:
            
            return None

def getLastName():
    
    lastName = input("input student last name or 'zzz' to quit. ")
    
    return lastName

def getFirstName():
    
    firstName = input("input student first name or 'zzz' to quit. ")
    
    return firstName
    
stop = 0

while stop == 0:
    
    checkGPA()
