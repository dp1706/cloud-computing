## DOCKER INSTALLATION AND TEST

1. installing `$ sudo apt-get install docker docker.io -y`
2. giving permission ---$ sudo chmod 600 /var/run/docker.sock
3. checking whether installed or not by typing ---$ docker
4. pulling python version3.8 image ----$  docker pull python:3.8-slim
5. checking the download image ----$ docker images



6. $ docker run -dit --name=pyContainer python:3.8-slim
7. checing the container --$ docker container ls
8. inside container  ---$docker exec -it pyContainer /bin/bash


now inside the shell we will check whether python is woring or not and 
will check python version

9. python -c 'print("hello world!")'
10.python --version
11.ls
12.exit -(for exit from shell)




13.docker container stop pyContainer
14.docker container rm   pyContainer

## Assignment

we will create a folder in our local system and mount it to the docker

15. creating a folder in local system --$ mkdir testfolder
16. for finding path -- $ pwd

now we will create a new container and mount testfolder in that container

17. $ docker run -dit --name=pyC -v /home/dwarka/testfolder:/myfolder python:3.8-slim
18. docker exec -it pyC /bin/bash


after entering in shell-


now we will create a assignment.py file in the local system and it will reflect in out container folder and we will run it .

19. ls
20. python assignment.py









