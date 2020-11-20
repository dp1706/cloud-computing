#!/bin/bash

cp initial-centroids.txt centroids.txt # copy initial assigned centroids to a file for running iterations

iterations=0
while [ $iterations -lt 20 ]
do
    #rm -rf output #delete output directory as required by hadoop runtime

    #hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar -input inputfile.txt -file centroids.txt -output output/ -mapper ./mapper.py -reducer ./reducer.py 2>/dev/null 1>/dev/null # run hadoop command where last part is to hide the output of this command

    converged=$(./checker.py output/part-00000) # runs convergence-checker.py with argument output/part-00000 and store the printed output in converged
    if [ $converged = 1 ]
    then
        rm centroids.txt #delete temp_centroids file
        cp ./output/part-00000 centroids.txt # copy output of reducer as new temp_centroid file
        echo -e
        break
    else
        rm centroids.txt
        cp ./output/part-00000 centroids.txt

        iterations=$((iterations+1))
        #echo -ne "\nIteration: " # print
        #echo $iterations # print
	echo -e "Cluster centroids:"
        cat centroids.txt
    fi

done

cp centroids.txt final-output.txt # Generate final output
