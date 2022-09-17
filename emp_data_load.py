import sys
import time

from pyspark.sql import *
from pyspark.sql import functions as F
from lib.sql_connection import SQLServerConnection
from lib.audit_utils import get_audit_insert_qry,get_audit_updt_qry


spark = SparkSession.builder.appName("Mahesh").master("local[2]").getOrCreate()

sqlServerObj = SQLServerConnection()

query = get_audit_insert_qry(1,'EMP_LOAD')
print(query)
result = sqlServerObj.execute_query(query)


raw_df = spark.read.option("header",True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table.csv')

raw_df = raw_df.withColumn('e_dob',F.regexp_replace('e_dob','-','/')).withColumn('e_doj',F.regexp_replace('e_doj','/','-'))

raw_df2 = raw_df.withColumn('e_dob',F.to_date('e_dob','dd/MM/yyyy'))\
                .withColumn('e_doj',F.to_date('e_doj','dd-MM-yyyy'))\
                .withColumn('today_dt',F.current_date())
raw_df2.show()
time.sleep(60)


query1 = get_audit_updt_qry(1,'SUCCESS')

result1 = sqlServerObj.execute_query(query1)

