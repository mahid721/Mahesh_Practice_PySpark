from pyspark.sql import *
from pyspark.sql import functions as F
# from pyspark.sql.types import StringType


# Spark = SparkSession\
#     .builder\
#     .appName("HelloSpark") \
#     .master("local[2]") \
#     .getOrCreate()

spark = SparkSession.builder.appName("Mahesh").master("local[2]").getOrCreate()


raw_df = spark.read.option("header",True).option('inferschema',True).csv('C:\\Test_Mahesh\\Emp_table.csv')

# raw_df.show()
# raw_df.printSchema()

raw_df = raw_df.withColumn('e_dob',F.regexp_replace('e_dob','-','/')).withColumn('e_doj',F.regexp_replace('e_doj','/','-'))


raw_df2 = raw_df.withColumn('e_dob',F.to_date('e_dob','dd/MM/yyyy'))\
                .withColumn('e_doj',F.to_date('e_doj','dd-MM-yyyy'))\
                .withColumn('today_dt',F.current_date())

raw_df3 = raw_df2.withColumn('age',F.datediff('today_dt','e_dob')/365)\
                 .withColumn('month_diff',F.months_between('today_dt','e_dob'))\
                 .withColumn('dob_year',F.year('e_dob'))\
                 .withColumn('currentyear',F.year('today_dt'))\
                 .withColumn('age_yeardiff',F.col('currentyear')-F.col('dob_year'))\
                 .withColumn('age_yeardiff1',F.expr('currentyear')-F.expr('dob_year'))

raw_df4 = raw_df3.withColumn('age_yeardiff2',raw_df3.currentyear-raw_df3.dob_year)


raw_df5 = raw_df2.withColumn('yr_mon',F.date_format('e_doj','M-yyyy'))\
                 .withColumn('dummy_dt',F.to_date(F.col('dummy_dt').cast(StringType()),'MMddyyyy'))
raw_df5.show()
