## HANDOOP INSTALLATION
---

#### UBUNTU VERSION :  18.04
#### JAVA PRE-INSTALLED VERSION : 11.0.6( To install -- `sudo apt-get install default-jdk` )
---
* Commands:

> `sudo apt-get install update`

>`sudo apt-get update`

> `sudo wget http://mirrors.estointernet.in/apache/hadoop/common/hadoop-2.10.0/hadoop-2.10.0.tar.gz` 

> `tar -xzvf hadoop-2.10.0.tar.gz`

> `sudo mv hadoop-2.10.0 /usr/local/hadoop`

> `readlink -f /usr/bin/java | sed "s:bin/java::"`

> `export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")`

> `export PATH=$PATH:$JAVA_HOME/bin`

> `export PATH=$PATH:/usr/local/hadoop/bin`

* To find version and check hadoop is installed properly

> `hadoop version` or `hadoop`

* Command for running wordcount mapper and reducer file which is in the hadoop_assignment directory

```
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar 
-input /home/dwarka/hadoop_assignment/input.txt 
-output /home/dwarka/hadoop_assignment/output 
-mapper /home/dwarka/hadoop_assignment/mapper.py 
-reducer /home/dwarka/hadoop_assignment/reducer.py
```

---

