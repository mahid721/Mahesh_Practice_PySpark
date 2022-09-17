import sys
from pyspark.sql import *
from lib.logger import Log4j
from lib.utils import *




sparkSession = SparkSession \
    .builder \
    .appName("HelloSpark") \
    .master("local[2]") \
    .getOrCreate()


raw_df = sparkSession.read.csv('C:\\Test_Mahesh\\New_Test.csv')  #show() # dataframe method returns none
raw_df.show()
raw_df.printSchema()

raw_df1 = sparkSession.read.option('header',True).csv('C:\\Test_Mahesh\\New_Test.csv')
raw_df1.show()
raw_df1.printSchema()

raw_df2 = sparkSession.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\New_Test.csv')     # assighning result to one object
raw_df2.show()   # to display the result
raw_df2.printSchema()  # to know the datatype



raw_df2.createOrReplaceTempView('emp_table')  # create a temp table
select_query = """select * from {table_name} 
                    where city = 'K'""".format(table_name = 'emp_table')                  # writing a sql query
final_df = sparkSession.sql(select_query)
final_df.show()
#final_df.write.csv("C:\\Test_Mahesh_OUT\\New_Test.csv")
final_df.write.option('header',True).csv("C:\\Test_Mahesh_OUT1\\New_Test.csv")
raw_df2.write.option('header',True).csv("C:\\Test_Mahesh_OUT2\\New_Test.csv")

