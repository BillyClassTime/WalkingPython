#https://medium.com/analytics-vidhya/crud-operations-in-mongodb-using-python-49b7850d627e
#https://www.dev2qa.com/how-to-drop-mongodb-database-and-collection-use-pymongo-in-python/s
#Query and Projection Operators:https://www.mongodb.com/docs/manual/reference/operator/query/
from pymongo.mongo_client import MongoClient
import os
import platform
def connectdb():
    clientDB = MongoClient('mongodb://localhost:27017/')
    db = clientDB.admin
    resultado = db.command('serverStatus')
    print('Host:',resultado['host'])
    print('Version:',resultado['version'])
    print('Process:',resultado['process'])
    print(clientDB.list_database_names())
    return clientDB

#Create a database
def CreateDB(name,clientDb):
    database_name=name #'Students'
    db=clientDb[database_name]
    return db

#Create a collection
def createCollection(name,db):
    collection_name=name #'computer science'
    collection=db[collection_name]
    #print(db.list_collection_names())
    return collection

#inserting documents in the collection
def insertDocument(document,col):
    doc= document 
    col.insert_one(document)

#insert multiple documents
def insertManyDocument(list,col):
    documents=list
    col.insert_many(documents)

#Retrieving the data from the collection
def retrievingDocument(query,col):
    print(col.find_one(query))

#Retrieving multiple docuemnts from the collection
def retrievingManyDocuments(query,col):
    result=col.find(query)
    for i in result:
        print(i)

#Retrieve all the documents
def retrieveAllDocuments(col):
    #asyncronia y multihilo
    result=col.find({}).limit(200)
    for i in result:
        print(i)
#filtering
def filtering(query,col):
    print("filtering")
    print(col.find_one(query))

#update
#single document
def updateSingleDocument(query,new_data,col):
    present_data=col.find_one(query)
    if present_data!=None:
        col.update_one(present_data,new_data)

#multiple documents
def updateMultipleDocument(present_data,new_data,col):

    col.update_many(present_data,new_data)

#Deleting documents
#single
def deletingSingleDoc(query,col):
    col.delete_one(query)

#multiple
def deletingMultipleDocument(query,col):
    col.delete_many(query)

def dropColection(col):  
    #drop collection
    col.drop()

if __name__ == '__main__':
    client=None
    db=None
    col=None
    client=connectdb()
    db=CreateDB('Students',client)    
    col=createCollection('Computer science',db)  

    while 1:
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin":
            os.system("clear")
        elif platform.system() == "Linux":
            os.system("clear")        
        #print('1 - Connect Mongo')
        #print('2 - Create Database (if it not exits)')
        #print('3 - Create a collection (if it not exits)')
        print('1 - inserting documents in the collection')
        print('2 - insert multiple documents')
        print('3 - Retrieving the data from the collection')
        print('4 - Retrieving multiple documents from the collection')
        print('5 - Retrieve all the documents')
        print('6 - filtering')
        print('7 - update single document')
        print('8 - update multiple documents')
        print('9 - Deleting single document')
        print('A - Deleting multiple documents')
        print('B - drop collection')
        selection=input('Enter you choise-0-exit()')
        #if selection == '1':
        #    client=connectdb()
        # elif selection =='2':    
        #     db=CreateDB('Students',client)    
        # elif selection =='3': 
        #     col=createCollection('Computer science',db)  
        if selection =='1':    
            name=input("Name:")
            rollNumber=input("Roll number:")        
            branch=input("Branch:")
            doc={"Name":name,
                "Roll No":rollNumber,
                "Branch": branch}         
            insertDocument(doc,col)
        elif selection =='2': 
            students=[] 
            while True:
                name=input("Name:")
                rollNumber=input("Roll number:")        
                branch=input("Branch:")
                students.append({"Name":name,"Roll No":rollNumber,"Branch":branch})
                follow=input("¿Do you want to insert another studend?(Y/N):")
                if follow.upper()!="Y":
                    break
            insertManyDocument(students,col)
        elif selection =='3':   
            name = input("Enter a student's name, to retrieve his data:")         
            query={"Name":name}
            retrievingDocument(query,col)
        elif selection =='4': 
            branch=input("Enter students's branch, to retrieve many documents:")           
            query={"Branch":branch}
            retrievingManyDocuments(query,col)
        elif selection =='5':        
            retrieveAllDocuments(col)
        elif selection =='6':     
            rollNumber = input("Enter filter roll number:")       
            query={"Roll No":{"$eq":rollNumber}}
            filtering(query,col)
        elif selection =='7':  
            rollNumber=input("Roll number:")
            new_name=input("Enter new name for a student:")
            query={"Roll No":{"$eq":rollNumber}}
            new_data={'$set':{'Name':new_name}}
            updateSingleDocument(query,new_data,col)
        elif selection =='8':        
            oldBranch=input("Enter old branch:")
            newBranch=input("Enter new branch:")
            present_data={"Branch":oldBranch}
            new_data={"$set":{"Branch":newBranch}}   
            updateMultipleDocument(present_data,new_data,col)         
        elif selection =='9':    
            rollNumber=input("Enter roll number:")        
            query={"Roll No":{"$eq":rollNumber}}
            deletingSingleDoc(query,col)
        elif selection =='A': 
            branch=input("Enter branch:")             
            query={"Branch":branch}
            deletingMultipleDocument(query,col)
        elif selection =='B':
            dropColection(col)
        elif selection =='0':     
            break                                                               
        else:
            print('Invalid selection, try again')
        follow=input("Pres any key to continue...")