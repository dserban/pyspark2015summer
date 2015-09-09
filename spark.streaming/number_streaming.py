from sys      import argv, exit
from operator import add, sub

from pyspark           import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    if len(argv) != 3:
        print "Please pass host and port number as arguments."
        exit(-1)
    sc = SparkContext()
    ssc = StreamingContext(sc, 1)
    ssc.checkpoint('/tmp/sparkstreamingcheckpoint')

    lines = ssc.socketTextStream(argv[1], int(argv[2]))
    sums =                                    \
      lines                                   \
      .map( lambda line: int(line) )      \
      .map( lambda number: ('aggr', number) ) \
      .reduceByKeyAndWindow(add, sub, 30, 5)
    sums.pprint()

    ssc.start()
    ssc.awaitTermination()

