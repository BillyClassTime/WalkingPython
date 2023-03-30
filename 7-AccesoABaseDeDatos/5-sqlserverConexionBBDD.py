import pyodbc 

server = '(localdb)\ProjectsV13'
database = 'bikerentdb' 
username = 'developer' 
password = 'P4$$w0rd' 

#Conecction String
driver='DRIVER={ODBC Driver 17 for SQL Server};'
others=f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
connection_string='{}{}'.format(driver,others)

con = pyodbc.connect(connection_string)

cur = con.cursor()
res=cur.execute("SELECT @@VERSION AS 'SQL Server Version Details'")
for r in res:
    print(r[0])