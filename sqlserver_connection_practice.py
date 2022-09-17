import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DESKTOP-RI7RJF5'
database = 'Mahesh'
username = 'sa'
password = 'sa123'
connect_obj = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# connect_obj = pyodbc.connect(DSN='sql_conn_11')
cursor_obj = connect_obj.cursor()
select_query = 'select * FROM Mahesh.dbo.TESTADD'
cursor_obj.execute(select_query)

for record in cursor_obj:
    print(record)
print(type(record))
