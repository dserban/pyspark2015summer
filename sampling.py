from pyspark import SparkContext

sc = SparkContext()
raw_rdd =                                      \
    sc.textFile('/data/sparkdata/data.txt.gz') \
      .repartition(sc.defaultParallelism)      \
      .cache()

cnt = raw_rdd.count()

sample = raw_rdd.sample(False, 0.1)

for line in sample.collect():
    print line

sc.stop()
