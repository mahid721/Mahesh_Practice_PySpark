from lib.audit_utils import get_audit_insert_qry, get_audit_updt_qry
from lib.sql_connection import SQLServerConnection

print('START')

sqlServerObj = SQLServerConnection()
query = get_audit_insert_qry(2,'error practice')
result = sqlServerObj.execute_query(query)

try:
    f = open('C:\\Test_Mahesh\\Emp_table2.csv1', "r")
    print(f.read())
    print('Try END')
except Exception as e :
    print('Error occured : ' + str(e))
    query1 = get_audit_updt_qry(2, 'FAILED', str(e).replace("'",''))
    result1 = sqlServerObj.execute_query(query1)
    raise Exception
print('END')

query1 = get_audit_updt_qry(1,'SUCCESS')
result1 = sqlServerObj.execute_query(query1)


