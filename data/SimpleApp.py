"""SimpleApp.py"""
from pyspark import SparkContext

#logFile = "YOUR_SPARK_HOME/README.md"  # Should be some file on your system
logFile = "/usr/spark-2.0.2/README.md"
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

sc.stop()
