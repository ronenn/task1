# Load balancer task with vagrant and docker based on python flask REST API

## Architecture
The environment is composed of 3 components:
1. The load balancer implemeneted as Nginx reverse proxy server. The nginx server run on port 80.
2. Python flask application run on port 5000. The port is only exposed to the nginx server and not to host machine.
3. Same as (2) for high availability and load balancing

Each request coming to nginx, it proxy it to one of the 2 python application using round robin.
This is implemented using nginx **upstream** configuration:

```
upstream docker-flask {
        server myflask1:5000;
        server myflask2:5000;
    }
```

The nginx configuration is in the file **nginx.conf**

The pyhon flask server implementation is in file **app.py**

All the above is run using docker containers where vagrant run those containers in order.

## How to deploy the environment
Requirements:
1. Make sure vagrant is installed
2. Make sure docker is installed

After cloning this repo, change directory to the cloned directory.

Before bringing up the environment, we need the build the docker image of the python flask server. 

To do it, run the following:

```
docker build -t my_docker_flask .
```

This will create a docker image for the app.

Then, to bring up the environment, run the following:

```vagrant up --no-parallel```

The **Vagarnatfile** tells vagrant to use docker provider and it first build the docker image **my_docker_flask** before running 3 docker containers:
1. Application host implemented with python flask library
2. Another identical container to simulate the load balancing.
3. Nginx container to do the load balancing.

So if the command run successfuly you should see 3 containers running, after running the command:

```docker ps```

One container of nginx and 2 containers of my_docker_flask image.

The nginx is running in port 80, so going to http://localhost/host or http://localhost/date should give you the right response.

To stop the environment run the following:

```vagrant halt```

To reload the environment after you made some changes, run the following:

```vagrant reload```


## How to test the environment
There is a bash script file called **test.sh** that tests load balancing work properly.

Just run:

```./test.sh``` 

and verify the result is 50. 

What the script does, it runs **curl -s http://localhost/host | grep flask1** 100 times. Since the load balancing is done using the round robin method, we should get 
half of the time requests coming from a one of the instanstce ("flask1") and half of the time requests coming from the second instance ("flask2").

## How to use the API
The api contain 2 endpoints:
1. "/host" - returns the hostname
2. "/date" - returns the cureent date and time in UTC

So to call the first endpoint, run in your browser "http://localhost/host" or with curl tool for example: **curl -s http://localhost/host**

For the second endpoint, run in your browser "http://localhost/date" or with curl tool for example: **curl -s http://localhost/date**
