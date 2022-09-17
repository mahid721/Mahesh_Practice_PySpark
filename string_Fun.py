import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from lib.utils import *



Spark = SparkSession\
    .builder\
    .appName("HelloSpark") \
    .master("local[2]") \
    .getOrCreate()



