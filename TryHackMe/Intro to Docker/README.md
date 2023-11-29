https://tryhackme.com/room/introtodockerk8pdqk

# Basic Docker Syntax

## Docker Pull

Before we can run a Docker container, we will first need an image.

Images can be downloaded using the docker pull command and providing the name of the image. 

For example, docker pull nginx. Docker must know where to get this image (such as from a repository which we’ll come onto in a later task).

## Docker Image x/y/z
The docker image command, with the appropriate option, allows us to manage the images on our local system.

## Docker Image ls
This command allows us to list all images stored on the local system. We can use this command to verify if an image has been downloaded correctly and to view a little bit more information about it (such as the tag, when the image was created and the size of the image).

## Docker Image rm
If we want to remove an image from the system, we can use docker image rm along with the name (or Image ID). In the following example, I will remove the "ubuntu" image with the tag "22.04". My command will be docker image rm ubuntu:22.04:




# Running Your First Container

The Docker run command creates running containers from images. This is where commands from the Dockerfile (as well as our own input at runtime) are run. Because of this, it must be some of the first syntaxes you learn.

The command works in the following way: `docker run [OPTIONS] IMAGE_NAME [COMMAND] [ARGUMENTS...]`  the options enclosed in brackets are not required for a container to run.

## First, Simply Running a Container

Let's recall the syntax required to run a Docker container: `docker run [OPTIONS] IMAGE_NAME [COMMAND] [ARGUMENTS...]` . In this example, I am going to configure the container to run:

An image named "helloworld"
"Interactively" by providing the -it switch in the [OPTIONS] command. This will allow us to interact with the container directly.
I am going to spawn a shell within the container by providing /bin/bash as the [COMMAND] part. This argument is where you will place what commands you want to run within the container (such as a file, application or shell!)


So, to achieve the above, my command will look like the following: `docker run -it helloworld /bin/bash`

We can verify that we have successfully launched a shell because our prompt will change to another user account and hostname. The hostname of a container is the container ID (which can be found by using `docker ps`)

# Intro to Dockerfiles

Dockerfiles is a formatted text file which essentially serves as an instruction manual for what containers should do and ultimately assembles a Docker image.

You use Dockerfiles to contain the commands the container should execute when it is built. To get started with Dockerfiles, we need to know some basic syntax and instructions. Dockerfiles are formatted in the following way:

INSTRUCTION argument

RUN
FROM
COPY
WORKDIR
CMD
EXPOSE



```
FROM ubuntu:22.04

WORKDIR / 

RUN touch helloworld.txt
```

Building Your First Container

Once we have a Dockerfile, we can create an image using the docker build command. This command requires a few pieces of information:

- Whether or not you want to name the image yourself (we will use the -t (tag) argument).
- The name that you are going to give the image.
- The location of the Dockerfile you wish to build with.


I’ll provide the scenario and then explain the relevant command. Let’s say we want to build an image - let’s fill in the two required pieces of information listed above:
- We are going to name it ourselves, so we are going to use the -t argument.
- We want to name the image.
- The Dockerfile is located in our current working directory (.).


The command would look like so: `docker build -t helloworld .`


Let’s level up our Dockerfile. So far, our container will only create a file - that’s not very useful! In the following Dockerfile, I am going to:
Use Ubuntu 22.04 as the base operating system for the container.
Install the “apache2” web server.
Add some networking. As this is a web server, we will need to be able to connect to the container over the network somehow. I will achieve this by using the EXPOSE instruction and telling the container to expose port 80.
Tell the container to start the “apache2” service at startup. Containers do not have service managers like systemd (this is by design - it is bad practice to run multiple applications in the same container. For example, this container is for the apache2 web server - and the apache2 web server only).

```
# THIS IS A COMMENT
FROM ubuntu:22.04

# Update the APT repository to ensure we get the latest version of apache2
RUN apt-get update -y 

# Install apache2
RUN apt-get install apache2 -y

# Tell the container to expose port 80 to allow us to connect to the web server
EXPOSE 80 

# Tell the container to run the apache2 service
CMD ["apache2ctl", "-D","FOREGROUND"]
```

`docker build -t webserver .`


For example, you can reduce the size of a docker image (and reduce build time!) using a few ways:

- Only installing the essential packages. What’s nice about containers is that they’re practically empty from the get-go - we have complete freedom to decide what we want.
- Removing cached files (such as APT cache or documentation installed with tools). The code within a container will only be executed once (on build!), so we don’t need to store anything for later use.
- Using minimal base operating systems in our FROM instruction. Even though operating systems for containers such as Ubuntu are already pretty slim, consider - using an even more stripped-down version (i.e. ubuntu:22.04-minimal). Or, for example, using Alpine (which can be as small as 5.59MB!).
Minimising the number of layers - I’ll explain this further below.




# Intro to Docker Compose

Docker Compose, in summary, allows multiple containers (or applications) to interact with each other when needed while running in isolation from one another.


Before we demonstrate Docker Compose, let’s cover the fundamentals of using Docker Compose.
- We need Docker Compose installed (it does not come with Docker by default). Installing it is out of scope for this room, as it changes depending on your operating system and other factors. You can check out the installation documentation here.
- We need a valid docker-compose.yml file - we will come onto this shortly.
- A fundamental understanding of using Docker Compose to build and manage containers.


I have put some of the essential Docker Compose commands into the table below:

up
start
down
stop
build


With that said, let’s look into how we can use Docker Compose ourselves. In this scenario, I am going to assume the following requirements:

1. An E-commerce website running on Apache
2. This E-commerce website stores customer information in a MySQL database
Now, we could manually run the two containers via the following:

1. Creating the network between the two containers: docker network create ecommerce
2. Running the Apache2 webserver container: docker run -p 80:80 --name webserver --net ecommerce webserver
3. Running the MySQL Database server: docker run --name database --net ecommerce webserver


Instead, we can use Docker Compose via docker-compose up to run these containers together, giving us the advantages of:

1. One simple command to run them both
2. These two containers are networked together, so we don’t need to go about configuring the network.
3. Extremely portable. We can share our docker-compose.yml file with someone else, and they can get the setup working precisely the same without understanding how the containers work individually.
4. Easy to maintain and change. We don’t have to worry about specific containers using (perhaps outdated) images.


With that said, let’s look at our first docker-compose.yml file. This docker-compose.yml file assumes the following:

1. We will run one web server (named web) from the previously mentioned scenario.
2. We will run a database server (named database) from the previously mentioned scenario.
3. The web server is going to be built using its Dockerfile, but we are going to use an already-built image for the database server (MySQL)
4. The containers will be networked to communicate with each other (the network is called ecommerce).
5. Our directory listing looks like the following:
- docker-compose.yml
- web/Dockerfile

Here is what our docker-compose.yml file would look like (as a reminder, it is essential to pay attention to the indentation):
```
version: '3.3'
services:
  web:
    build: ./web
    networks:
      - ecommerce
    ports:
      - '80:80'


  database:
    image: mysql:latest
    networks:
      - ecommerce
    environment:
      - MYSQL_DATABASE=ecommerce
      - MYSQL_USERNAME=root
      - MYSQL_ROOT_PASSWORD=helloword
    
networks:
  ecommerce:
```



# Intro to the Docker Socket

This task will explain how Docker interacts between the operating system and the container. When you install Docker, there are two programs that get installed:

The Docker Client
The Docker Server
Docker works in a client/server model. Specifically, these two programs communicate with each other to form the Docker that we know and love. Docker achieves this communication using something called a socket. Sockets are an essential feature of the operating system that allows data to be communicated. 

For example, when using a chat program, there could be two sockets:

A socket for storing a message that you are sending
A socket for storing a message that someone is sending you.
The program will interact with these two sockets to store or retrieve the data within them! A socket can either be a network connection or what is represented as a file. What's important to know about sockets is that they allow for Interprocess Communication (IPC). This simply means that processes on an operating system can communicate with each other!

For example, let's take this command: docker run helloworld. The Docker Client will request the Docker server to run a container using the image "helloworld". Now, whilst this explanation is fairly basic, it is the essential premise of how Docker works.




# Practical


