### Randomly Generated List Of People (JSON)
```
from pyspark.sql import SQLContext

sqlContext = SQLContext(sc)

df = sqlContext.read.json('/tmp/fakepeople/people.txt')

df
DataFrame[_id: string, address: string, age: bigint, balance: double, company: string, email: string, eyeColor: string, gender: string, guid: string, index: bigint, isActive: boolean, latitude: double, longitude: double, name: string, phone: string, picture: string, registered: string]

df.agg( {"balance": "max"} ).show()
df.agg( {"balance": "min"} ).show()
```
### Detect Regional and Global Peak Oil Events (CSV)
```
from pyspark.sql import SQLContext, Row
sqlContext = SQLContext(sc)

lines = sc.textFile('/tmp/peakoil/oil.txt', 4)

parts = lines.map(lambda l: l.split(','))

datapoints = parts.map( lambda p: Row( year=int(p[0]), region=p[1], oil_prod=int(p[2]) ) )

schema = sqlContext.createDataFrame(datapoints)

schema.registerTempTable('datapoints')

na_oil_prod = sqlContext.sql("SELECT * FROM datapoints WHERE region = 'NA'")

na_oil_prod.collect()

na_peak_oil = sqlContext.sql("SELECT * FROM datapoints WHERE region = 'NA' ORDER BY oil_prod DESC LIMIT 1")

na_peak_oil.collect()

me_peak_oil = sqlContext.sql("SELECT * FROM datapoints WHERE region = 'ME' ORDER BY oil_prod DESC LIMIT 1")

me_peak_oil.collect()

# SELECT
#   year,
#   SUM(oil_prod) AS global_oil_prod
# FROM
#   datapoints
# GROUP BY
#   year
# ORDER BY global_oil_prod DESC
# LIMIT 1

global_peak_oil = sqlContext.sql("SELECT year, SUM(oil_prod) AS global_oil_prod FROM datapoints GROUP BY year ORDER BY global_oil_prod DESC LIMIT 1")

global_peak_oil.collect()
```
