#!/bin/bash

#PATH CONFIGURATION

export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
export PATH=$PATH:/usr/local/hadoop/bin
export PATH=$PATH:$JAVA_HOME/bin

#executing part 1

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /home/dwarka/college/sem5/cloud_computing/lab/lab_8/input/big.txt -output /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_1/output -mapper /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_1/mapper.py -reducer /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_1/reducer.py

#executing part2

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /home/dwarka/college/sem5/cloud_computing/lab/lab_8/input/big.txt -output /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_2/output -mapper /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_2/mapper.py -reducer /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_2/reducer.py


#executing part3

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /home/dwarka/college/sem5/cloud_computing/lab/lab_8/input/big.txt -output /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_3/output -mapper /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_3/mapper.py -reducer /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_3/reducer.py -combiner /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_3/combiner.py

#executing part4

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /home/dwarka/college/sem5/cloud_computing/lab/lab_8/input/big.txt -output /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_4/output -mapper /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_4/mapper.py -reducer /home/dwarka/college/sem5/cloud_computing/lab/lab_8/part_4/reducer.py


