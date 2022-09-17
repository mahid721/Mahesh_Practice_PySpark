import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from lib.utils import *



abc = SparkSession\
        .builder\
        .appName("HelloSpark") \
        .master("local[2]") \
        .getOrCreate()

Hyd_df = abc.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table.csv')
Hyd_df.show(truncate=False)
Hyd_df.show(,False)
# Hyd_df.printSchema()

#Hyd_df.select("E_ID","E_FName").show()
#
# Hyd_df.select(Hyd_df.Emp_ID,"E_FName").show(100)
# Hyd_df.select(Hyd_df.Emp_ID,expr("concat(E_FName,' ',E_LName)as E_Name ")).show(5)
# Hyd_df.select(Hyd_df.Emp_ID,concat_ws("E_FName","E_LName").alias("E_Name")).show(5)
#
#
# Hyd_df.filter(Hyd_df.E_CITY == 'HYD').show()
#
# Hyd_df.filter(Hyd_df.E_DEP == 'IT').show()

# Hyd_df.filter(Hyd_df.E_DEP.isin('IT','HR')).show()

lst = ["HYD","CBM","RPD"]
# Hyd_df.filter(Hyd_df.E_CITY.isin(lst)).show()
#
# Hyd_df.filter(~(Hyd_df.E_CITY.isin(lst))).show()
#
# Hyd_df.filter((Hyd_df.E_CITY == 'OGL') | (Hyd_df.E_CITY == 'HYD')).show()
#
# Hyd_df.filter((Hyd_df.E_CITY == 'OGL') & (Hyd_df.E_DEP == 'IT')).show()
#
# Hyd_df.filter(Hyd_df.E_CITY.startswith("N")).show()
#
# Hyd_df.filter(Hyd_df.E_CITY.endswith("D")).show()
#
#
# Hyd_df.filter(Hyd_df.E_CITY.like("%RT%")).show()
#
# Hyd_df.filter(~(Hyd_df.E_CITY.like("%RT%"))).show()

