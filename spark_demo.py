# add library(spark/python/lib/) to project(settings/project/show all/show paths => add library)
from pyspark import SparkContext

sc = SparkContext("local", "demo95")
rdd1 = sc.parallelize(range(1, 100))
print(rdd1.collect())
print(rdd1.reduce(lambda a, b: a + b))
sc.stop()