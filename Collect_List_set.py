import sys
from pyspark.rdd import *
from pyspark.sql import functions as f


df.columns

df.rdd


Spark = SparkSession\
    .builder\
    .appName("HelloSpark") \
    .master("local[2]") \
    .getOrCreate()


call_df = Spark.read.option('header',True).option('inferschema',True).csv('C:\\Test_Mahesh\\Collect_data.csv')
#call_df.show()

# ex_df=call_df.groupby('rollno').agg(f.collect_list('name').alias('name'),f.collect_list('designation').alias('designation'))
#ex_df.withColumn('bava_out',ex_df.name[f.size(ex_df.name)-1]).show(truncate=False)
#ex_df.show(truncate=False)


ex_df = call_df.groupby('rollno').agg(f.collect_list('name')[0])
index = 1
ex_df = call_df.groupby('rollno').agg(f.collect_list('name')[f.size.collect_list(call_df.name)-1])



#call_df.groupby('rollno').agg(collect_set('name'),collect_set('designation')).show(truncate=False)


#eex_df = call_df.groupby('designation').agg(collect_list('name'),collect_list('rollno')).show(truncate=False)


#call_df.groupby('designation').agg(collect_set('name'),collect_set('rollno')).show(truncate=False)

#ex_df.select('rollno',explode('name')).show()
#ex_df.select('rollno',explode('designation')).show()

#ex_df.select('rollno',explode_outer('designation')).show()

#ex_df.select('rollno',explode('name')).show()
#ex_df.select('rollno',posexplode('name')).show()