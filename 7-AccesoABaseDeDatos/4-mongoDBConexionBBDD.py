from pymongo import MongoClient
#clientDB = MongoClient('mongodb://localhost:27017/')
#clientDB = MongoClient("mongodb+srv://developer:P455wrd.rd@cluster0.khc2b.mongodb.net/?retryWrites=true&w=majority")
clientDB = MongoClient("mongodb+srv://developer:P455wrd.rd@cluster0.khc2b.mongodb.net/test")
db = clientDB.test
resultado = db.command('serverStatus')
print('Host:',resultado['host'])
print('Version:',resultado['version'])
print('Process:',resultado['process'])


