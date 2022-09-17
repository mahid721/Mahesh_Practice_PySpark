import sys
from pyspark.sql import *
from pyspark.sql import functions as F


Spark = SparkSession\
    .builder\
    .appName("HelloSpark") \
    .master("local[2]") \
    .getOrCreate()

# Spark = SparkSession.builder.appname("Mahesh").master("Local[2]").getOrCreate()


raw_df = Spark.read.option("header",True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table.csv')

raw_df1 = Spark.read.option("header",True).option('inferschema',True).csv('C:\\Test_Mahesh\\city_data.csv')

raw_df2 = Spark.read.option("header",True).option('inferschema',True).csv('C:\\Test_Mahesh\\dep_data.csv')

# raw_df.show()
#
# raw_df1.show()
#
# raw_df2.show()

raw_df.join(raw_df1,(raw_df.E_CITY == raw_df1.E_CITY) & (raw_df.E_CITY == 'NKBD'),'right_outer').show(60)


# raw_df.join(raw_df1).show()  # Like crossjoin