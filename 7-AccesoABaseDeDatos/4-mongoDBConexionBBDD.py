from pymongo.mongo_client import MongoClient

uri = "mongodb://atlas-sql-643f1b649f0e864aae69ed54-khc2b.a.query.mongodb.net/sample_airbnb?ssl=true&authSource=admin"
# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.admin
    resultado = db.command('serverStatus')
    print('Host:',resultado['host'])

    # Obtener la lista de nombres de bases de datos
    #result = db.command('listDatabases')
    # Imprimir los nombres de las bases de datos
    #print(result)
except Exception as e:
    print(e)


