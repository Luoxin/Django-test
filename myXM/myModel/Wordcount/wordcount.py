import logging
from operator import add

from pyspark import SparkContext


logging.basicConfig(format='%(message)s', level=logging.INFO)

test_file_name = "E:\Pycharm-workspace\Spark\Wordcount\input.txt"
out_file_name = "E:\Pycharm-workspace\Spark\Wordcount\spark-out"

# Word Count
sc = SparkContext("local", "Simple App")
# text_file rdd object
text_file = sc.textFile(test_file_name)
# counts
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile(out_file_name)

# # flatMap 先映射后扁平化 Return a new RDD by first applying a function to all elements of this RDD,
# # and then flattening the results.
# rdd = sc.parallelize([2, 3, 4])
# print(rdd.flatMap(lambda x: range(1, x)).collect())
# # map 是直接将数据做映射
# rdd = sc.parallelize(["b", "a", "c"])
# print(rdd.map(lambda x: (x, 1)).collect())
# #reduceByKey Merge the values for each key using an associative reduce function.
# rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
# print(rdd.reduceByKey(add).collect())
