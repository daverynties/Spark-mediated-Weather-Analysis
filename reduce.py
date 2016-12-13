from __future__ import print_function

import sys
import os
from operator import add

from pyspark.sql import SparkSession

def get_data(line):
    val = line.strip()
    (year, temp) = (val[15:19], val[87:92])
    if (temp != "+9999"):
        return [(year, temp)]
    else:
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: reduce <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonReduce")\
        .getOrCreate()

    sc = spark.sparkContext
    lines = sc.textFile(sys.argv[1])

    max_temp = lines.flatMap(get_data).reduceByKey(lambda a,b : a if int(a) > int(b) else b)
    max_temp = max_temp.collect();

for (year, temp) in max_temp:
    print(year + ":" + temp)

spark.stop()
