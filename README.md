# Spark-mediated-Weather-Analysis

#### Run Command (Sequential):

spark-submit reduce.py "/home/NOAA_DATA/2008/*.gz","/home/NOAA_DATA/2009/*.gz","/home/NOAA_DATA/2010/*.gz","/home/NOAA_DATA/2011/*.gz","/home/NOAA_DATA/2012/*.gz"

#### Run Command (Cloud):

initialize and startup the cloud
    ../sbin/start-all.sh
execute your program (in the cloud).  In this example, output goes to eos22.
    ../bin/spark-submit --master=spark://eos22.cis.gvsu.edu:7077 PySparkWordCount.py Alice_in_Wonderland.txt
shutdown the cloud
    ../sbin/stop-all.sh
