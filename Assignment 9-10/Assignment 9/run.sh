#!/bin/bash

#PATH CONFIGURATION
cd ~
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
export PATH=$PATH:/usr/local/hadoop/bin
export PATH=$PATH:$JAVA_HOME/bin

#RUN Command

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /home/dwarka/Assignment_9/inputfile.txt -output /home/dwarka/Assignment_9/output -mapper /home/dwarka/Assignment_9/mapper.py -reducer /home/dwarka/Assignment_9/reducer.py
