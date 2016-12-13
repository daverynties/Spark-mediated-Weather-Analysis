# Spark Mediated Weather Analysis

#### Run Command (Sequential):

spark-submit reduce.py "/home/NOAA_DATA/2008/*.gz","/home/NOAA_DATA/2009/*.gz","/home/NOAA_DATA/2010/*.gz","/home/NOAA_DATA/2011/*.gz","/home/NOAA_DATA/2012/*.gz"

#### Run Command (Cloud):
First, make sure that you either copy or link the `./conf/slaves` and  `./conf/spark-env.sh` to the `<SparkROOT>/conf/`

Initialize and startup the master:

`<SparkROOT>/sbin/start-master.sh`

Initialize and startup the slaves toward the master:

`<SparkROOT>/sbin/start-slaves.sh <MASTER-HOST-OR-IP>`

Execute your program (in the cloud).  In this example, output goes to `eos24`, and if the slaves file from this director was used, then the workers are DC01-DC25.  To see the active connection or jobs, got to `<MASTER-HOST-OR-IP>:8080`, this a webgui for information regarding the `MASTER`

Execute:

`spark-submit --master=spark://eos24.cis.gvsu.edu:7077 reduce.py "/home/NOAA_DATA/2008/*.gz","/home/NOAA_DATA/2009/*.gz","/home/NOAA_DATA/2010/*.gz","/home/NOAA_DATA/2011/*.gz","/home/NOAA_DATA/2012/*.gz"`

Stop slaves:

`<SparkROOT>/sbin/stop-all.sh`
