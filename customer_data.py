import sys
from pyspark.sql import *
from pyspark.sql.functions import *



abc = SparkSession\
        .builder\
        .appName("HelloSpark") \
        .master("local[2]") \
        .getOrCreate()

c_df = abc.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\customer_data.csv')
c_df.show()


c_df.createOrReplaceTempView('customer_table')  # create a temp table
select_query = """select * from {table_name} 
                    where city = 'K'""".format(table_name = 'emp_table')                  # writing a sql query
final_df = abc.sql(select_query)
final_df.show()