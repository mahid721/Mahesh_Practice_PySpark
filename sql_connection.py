import pyodbc


class SQLServerConnection:
    def __init__(self, server = 'DESKTOP-RI7RJF5', database = 'mahesh', username = 'sa', password = 'sa123'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection_str = 'DRIVER={ODBC Driver 11 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password

    def init_cursor_obj(self):
        self.conn_obj = pyodbc.connect(self.connection_str)
        self.cursor_obj = self.conn_obj.cursor()

    def execute_query(self, query):
        self.init_cursor_obj()
        self.cursor_obj.execute(query)
        self.cursor_obj.commit()
        return self.cursor_obj



