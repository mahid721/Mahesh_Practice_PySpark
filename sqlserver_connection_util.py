class SQLServerConnection:
    def __init__(self,server,database,username,password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection_str = 'DRIVER={ODBC Driver 11 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password
    def get_cursor_obj(self):
        conn_obj = pyodbc.connect(self.connection_str)
        cursor_obj = conn_obj.cursor()
        return cursor_obj
    def execute_query(self,query,cursor_obj):
        cursor_obj.execute(query)





import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DESKTOP-RI7RJF5'
database = 'mahesh'
username = 'sa'
password = 'sa123'
connect_obj = pyodbc.connect(
    'DRIVER={ODBC Driver 11 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
