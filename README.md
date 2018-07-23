Make sure that you have installed docker.

To start app run - `docker run -p 8080:8080 ws_server_app`

To create docker cluster: 
    `docker swarm init` then,
    `docker service create 
        --name lab 
        --publish 8080:8080 
        --replicas=5 ws_server_app:latest`

By default cluster consists of 3 replicas.

To change amount of replicas: 
    `docker service update --replicas=<count_of_replicas:int> lab`

To see info about replicas:
    `docker service ps lab_web`
