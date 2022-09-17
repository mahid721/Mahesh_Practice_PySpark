import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from lib.utils import *



Spark = SparkSession\
    .builder\
    .appName("HelloSpark") \
    .master("local[2]") \
    .getOrCreate()

raw_df = Spark.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table.csv')

raw_df1 = Spark.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table2.csv')

un_df = raw_df.select('E_CITY')
un_df1 = raw_df1.select('E_CITY')

#un_df.show()
#un_df1.show()


unio_df = un_df.union(un_df1)
print(unio_df.count())
unio_df.show(50)

#
# union_df = raw_df.union(raw_df1)
# print(union_df.count())
#
# unionall_df = raw_df.unionAll(raw_df1)
# print(unionall_df.count())
# #Hyd_df.show()
# #Hyd_df.printSchema()
#
#
#
Hyd_df = Spark.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table.csv')
#
# Hyd_df.groupby('E_CITY').sum('E_Salary').show()
#
# Hyd_df.groupby('E_CITY').avg('E_Salary').show()
#
# Hyd_df.groupby('E_CITY').agg(sum('E_Salary')).agg(avg('E_Salary')).agg(min('E_Salary')).show()

Hyd_df1 = Hyd_df.groupby('E_CITY').agg(
                                sum('E_Salary').alias('sum_salary'),
                                avg('E_Salary').alias('avg_salary'),
                                min('E_Salary').alias('min_salary')
                            )



Hyd_df1.show()

Hyd_df2 = Hyd_df1.filter(Hyd_df1.E_CITY == 'OGL')
Hyd_df2.show()

pp = Hyd_df2.collect()
print(pp[0][0],pp[0][1],pp[0][2],pp[0][3])
# print(pp[1][0],pp[1][1],pp[1][2],pp[1][3])

city = pp[0][0]
sum_salry = pp[0][1]
avg_salary = pp[0][2]
min_salary = pp[0][3]
print(city,sum_salry,avg_salary,min_salary)

select_query = """
                select * from master_table
                where salary > {avg_salary}

""".format(avg_salary=avg_salary)
