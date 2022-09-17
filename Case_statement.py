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


raw_df.show()

raw_df1 = raw_df.withColumn('city',when(raw_df.E_CITY == 'HYD','Hyderabad')
                                    .when(raw_df.E_CITY == 'CBM','Cumbum')
                                    .when(raw_df.E_CITY == 'NKBD','Nekunambad')
                                    .when(raw_df.E_CITY == 'NRT','Narasraopeta')
                                    .when(raw_df.E_CITY == 'OGL','Ongole')
                                    .otherwise(raw_df.E_CITY)
                                    )
raw_df1.show()
