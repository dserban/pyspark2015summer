import org.apache.spark._
import org.apache.spark.streaming._

object Streaming {
  def main(args: Array[String]) {
    val conf = new SparkConf().setMaster("local[*]").setAppName("streaming")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val ssc = new StreamingContext(sc, Seconds(1))
    ssc.checkpoint("/tmp/sparkstreamingcheckpoint")

    val lines = ssc.socketTextStream("localhost", 9999)

    val sums = lines
               .map( i => ("aggr", i.toInt) )
               .reduceByKeyAndWindow(_ + _, _ - _, Seconds(30), Seconds(5) )

    sums.print()

    ssc.start()
    ssc.awaitTermination()

    println("Spark Streaming from a Kafka topic")
  }
}
