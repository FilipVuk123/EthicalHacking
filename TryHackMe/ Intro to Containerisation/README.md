https://tryhackme.com/room/introtocontainerisation

# What is Containerisation

Modern applications are often complex and usually depend on frameworks and libraries being installed on a device before the application can run. These dependencies can:

Be difficult to install depending on the environment the application is running (some operating systems might not even support them!)
Create difficulty for developers to diagnose and replicate faults, as it could be a problem with the application's environment - not the application itself!
Can often conflict with each other. For example, having multiple versions of Python to run different applications is a headache for the user, and an application may work with one version of Python and not another.
Containerisation platforms remove this headache by packaging the dependencies together and “isolating” (note: this is not to be confused with "security isolation" in this context) the application’s environment.

However, it is worth noting that containerisation platforms make use of the “namespace” feature of the kernel, which is a feature used so that processes can access resources of the operating system without being able to interact with other processes.

The isolation offered by namespaces adds a benefit of security because it means that if an application in the container is compromised, usually (unless they share the same namespace), other containers are unaffected.

# Introducing Docker

Docker is a relatively hassle-free, extensive and open source containerisation platform. The Docker ecosystem allows applications (images - we’ll come onto this in a later room) to be deployed, managed and shared with ease.

Working on Linux, Windows and MacOS, Docker is a smart choice for running applications. Applications can be published as “images” and shared with others. All that is required is pulling (downloading) the image and running it with Docker.

Docker engine is extensive and allows you to do things like:

Connect containers together (for example, a container running a web application and another container running a database)

Export and import applications (images)

Transfer files between the operating system and container

Docker uses the programming syntax YAML to allow developers to instruct how a container should be built and what is run. This is a significant reason why Docker is so portable and easy to debug; share the instructions, and it will build and run the same on any device that supports the Docker Engine.

# The History of Docker


# The Benefits & Features of Docker

- Docker is Free
The Docker ecosystem is free to use and open-sourced. While business plans exist, you can completely download, use, create, run and share images.

- Docker is Compatible
The Docker platform is compatible with Linux, macOS and Windows. Because of how containerisation works, if a device supports the Docker Engine, you can run any container, regardless of the application or dependencies.

- Docker is Efficient & Minimal
Docker is an efficient way to isolate applications in comparison to alternatives such as virtual machines. This is because the Docker Engine runs and interacts with the host operating system, and containers do not run a fully-fledged operating system for each container. For example, containers can share a minimal operating system image, meaning you only need to store it once.


- Docker is Easy to Get Started With
The Docker developer documentation is very well documented, with lots of articles, working examples and answered questions on the Internet. The chances are, if you want to do something in Docker, someone has already asked about or done it.

The syntax to get started with Docker is easy to pick up. You can start your first container in no time (the fact that there are docker images for all sorts of applications already published helps.) 

- Docker is Easy to Share With Others
A significant benefit of Docker is its portability. Docker uses “images” to store instructions to dictate how the container should be built (just an instruction manual!).

These “images” can be exported, shared and uploaded to both public and private repositories such as DockerHub and GitHub. The “image” can be run by anything that supports the Docker engine, as long as the syntax is valid.

- Docker is Minimal
These Docker images discussed above are minimal. You will often find many-core and luxurious tools and packages in a container that are missing. While this can look like a disadvantage, it, in fact, allows:
Containers to be built exactly how the developer wishes
Better security, knowing exactly what runs within a container can reduce the risk of unnecessary packages becoming vulnerable and posing a security risk.

- Docker is Cheaper to Run
Running containers is usually a cheaper option than running virtual machines. This is especially noticeable in cloud environments, where CPU, RAM, and Disk space are expensive. 



# How does Containerisation Work?


Every process running on Linux will be assigned two things:
- A namespace
- A process identifier (PID)


Namespaces are how containerisation is achieved! Processes can only "see" other processes that are in the same namespace - no conflicts in theory. Take Docker, for example, every new container will be running as a new namespace, although the container may be running multiple applications (and in turn, processes).


