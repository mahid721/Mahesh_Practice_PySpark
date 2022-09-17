import sys
from pyspark.sql import *
from lib.logger import Log4j
from lib.utils import *




sparkSession = SparkSession \
    .builder \
    .appName("HelloSpark") \
    .master("local[2]") \
    .getOrCreate()


max_df = sparkSession.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table.csv')
max_df.show()
max_df.printSchema()

max_df.createOrReplaceTempView('emp_table')
select_query = """
                    select *
                    from emp_table
                    Where E_Salary == (Select Max(E_salary) From emp_table)
                """
sparkSession.sql(select_query).show()

max_df1 = sparkSession.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table.csv')
max_df1.createOrReplaceTempView('emp_table1')
select_query1 = """
                    select Sum(E_Salary) over(partition by E_Salary Order by E_ID) as SUM_Salary
                    from emp_table1
                """
sparkSession.sql(select_query1).show()



