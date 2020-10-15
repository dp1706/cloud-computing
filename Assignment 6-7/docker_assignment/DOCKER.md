## DOCKER INSTALLATION AND TEST
* INSTALLING
> installing `$ sudo apt-get install docker docker.io -y`

> giving permission `$ sudo chmod 600 /var/run/docker.sock`

> checking `$ docker`

> pulling python version3.8 image  `$  docker pull python:3.8-slim`

> checking the download image  `$ docker images`


* CREATING CONTAINER
> `$ docker run -dit --name=pyContainer python:3.8-slim`

> checing the container  `$ docker container ls`

> inside container   `$docker exec -it pyContainer /bin/bash`

* INSIDE THE CONTAINER SHELL

> `$ python -c 'print("hello world!")'`

> `$ python --version`

> `$ ls`

> `$ exit` 



* STOPING AND DELETING CONTAINER

> `$ docker container stop pyContainer`

> `$ docker container rm   pyContainer`

## Assignment

* We will create a folder in our local system and mount it to the docker

> Creating a folder in local system  `$ mkdir testfolder`

> For finding path  `$ pwd`


* Now we will create a new container and mount testfolder in that container

> `$ docker run -dit --name=pyC -v /home/dwarka/testfolder:/myfolder python:3.8-slim`

> `$ docker exec -it pyC /bin/bash`


* After entering in shell-


  Now we will create a assignment.py file in the local system and it will reflect in out container folder and we will run it .

> `$ ls`
> `$ python assignment.py`









