#Packages required to build the framework for the application
from bottle import route, run, template, request
import csv
import shutil
#Import operations file to make use of the AVL tree operations
import operations

#Create object for the avlTree class in the operations file
tree = operations.avlTree()

'''
#Function to load the train details into AVL Tree  
#Input: None
#Output: None 
'''
def load_data():
    with open('IndianRailwaysInfo.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            inputValue = [int(row['Train No']), row['Train name'], row['Source Station'], row['Destination Station']]
            tree.insertEntryInTree(inputValue)
        csvfile.close()
    
    tree.display(None, 0)

'''
#This is the default route, our home page  
#Input: None
#Output: None 
'''
@route('/')
def homePage():
    load_data()    
    return template('index')

'''
#This is the route to redirect to Search page, once user entered train number to search in the system.  
#Input: None
#Output: None 
'''
@route('/trainNo', method='POST')
def displayTrainDetails():
        trainNo = request.forms.get("trainNo")
    
        trainList = tree.searchEntryInTree(int(trainNo))
        if (trainList):
            return template('search', dict(train = trainList))
        else:
            return template('empty')

'''
#This is the route to redirect to Deletion page, once user entered train number to delete from the system.  
#Input: None
#Output: None 
'''
@route('/deleteTrainNo', method='POST')
def deleteTrainDetails():
        trainNo = request.forms.get("trainNo")
        isEntryFound = []
        tree.deleteEntryInTree(int(trainNo), isEntryFound)

        file = open("IndianRailwaysInfo.csv", "r")
        rows = csv.reader(file)
        
        file2 = open("indian.csv", "w", newline='')
        writer = csv.writer(file2)
        check = False
        for row in rows:            
            if (not row[0].isdigit()):
                writer.writerow(row)
            else:
                check = True
                if(int(row[0]) == int(trainNo)):
                    continue
                writer.writerow(row)

        file.close()
        file2.close()
        
        if (check == True):
            shutil.copyfile("indian.csv", "IndianRailwaysInfo.csv")
        
        for values in isEntryFound:
            if (values == True):
                print ("success")
                return template('deleteSuccess')
        if (len(isEntryFound) == 0):
            print ("empty")
            return template('empty')

'''
#This is the route to redirect to Insertion page, once user entered train details to update the system  
#Input: None
#Output: None 
'''
@route('/insert', method='POST')
def insertTrainDetails():
        trainNo = request.forms.get("trainNo")
        trainName = request.forms.get("trainName")
        srcStn = request.forms.get("srcStn")
        dstStn = request.forms.get("dstStn")

        inputValue = [int(trainNo), trainName, srcStn, dstStn]
        tree.insertEntryInTree(inputValue)

        with open('IndianRailwaysInfo.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(inputValue)
            csvfile.close()
            
        return template('success')

'''
#This is the route to redirect to Display Records page which displays all the records of the system as AVL Tree structure  
#Input: None
#Output: None 
'''
@route('/show', method='POST')
def displayAllTrainRecords(filename='result.txt'):
    tree.display()  
    with open(filename) as file:
        content = file.read()
        
    return template('show', content=content)

#Define host and port number and call run method to execute the application      
run(host='localhost', port=8050) 