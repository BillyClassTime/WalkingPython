#https://medium.com/analytics-vidhya/crud-operations-in-mongodb-using-python-49b7850d627e
#https://www.dev2qa.com/how-to-drop-mongodb-database-and-collection-use-pymongo-in-python/s
#Query and Projection Operators:https://www.mongodb.com/docs/manual/reference/operator/query/
from pymongo.mongo_client import MongoClient

def connectdb():
    #clientDB = MongoClient('mongodb://localhost:27017/')
    uri = "mongodb://atlas-sql-643f1b649f0e864aae69ed54-khc2b.a.query.mongodb.net/Students?ssl=true&authSource=Students" 	
    #uri = "mongodb+srv://billyclasstime:ydyJNnHd1tIRpFAC@cluster0.qlwohwx.mongodb.net/?retryWrites=true&w=majority"
    #uri=   "mongodb+srv://developer:6ZKujh1pm9pW2gl7@cluster0.qlwohwx.mongodb.net/?authSource=admin&retryWrites=true&w=majority"
    #uri=   "mongodb+srv://developer:6ZKujh1pm9pW2gl7@cluster0.qlwohwx.mongodb.net/?retryWrites=true&w=majority"
    clientDB = MongoClient(uri)
    db = clientDB.admin
    resultado = db.command('serverStatus')
    print('Host:',resultado['host'])
    #print('Version:',resultado['version'])
    #print('Process:',resultado['process'])
    #print(clientDB.list_database_names())
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
    result=col.find({}).limit(2)
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
    while 1:
        print('1 - Connect Mongo')
        print('2 - Create Database')
        print('3 - Create a collection')
        print('4 - inserting documents in the collection')
        print('5 - insert multiple documents')
        print('6 - Retrieving the data from the collection')
        print('7 - Retrieving multiple docuemnts from the collection')
        print('8 - Retrieve all the documents')
        print('9 - filtering')
        print('A - update single document')
        print('B - update multiple documents')
        print('C - Deleting single document')
        print('D - Deleting multiple documents')
        print('F - drop collection')
        selection=input('Enter you choise-0-exit()')
        if selection == '1':
            client=connectdb()
        elif selection =='2':    
            db=CreateDB('Students',client)    
        elif selection =='3': 
            col=createCollection('Computer science',db)  
        elif selection =='4':            
            doc={"Name":"Billy",
                "Roll No":  153,
                "Branch": "CSE"}         
            insertDocument(doc,col)
        elif selection =='5':  
            students=[{"Name":"Roshan","Roll No":159,"Branch":"CSE"},{"Name":"Rahim","Roll No":155,"Branch":"CSE"},{"Name":"Ronak","Roll No":156,"Branch":"CSE"}]      
            insertManyDocument(students,col)
        elif selection =='6':            
            query={"Name":"Billy"}
            retrievingDocument(query,col)
        elif selection =='7':            
            query={"Branch":"CSE"}
            retrievingManyDocuments(query,col)
        elif selection =='8':        
            retrieveAllDocuments(col)
        elif selection =='9':            
            query={"Roll No":{"$eq":153}}
            filtering(query,col)
        elif selection =='A':  
            query={"Roll No":{"$eq":153}}
            new_data={'$set':{'Name':'Miguel'}}
            updateSingleDocument(query,new_data,col)
        elif selection =='B':        
            present_data={"Branch":"CSE"}
            new_data={"$set":{"Branch":"ECE"}}   
            updateMultipleDocument(present_data,new_data,col)         
        elif selection =='C':            
            query={"Roll No":153}
            deletingSingleDoc(query,col)
        elif selection =='D':              
            query={"Branch":"ECE"}
            deletingMultipleDocument(query,col)
        elif selection =='F':
            dropColection(col)
        elif selection =='0':     
            break                                                               
        else:
            print('Invalid selection, try again')