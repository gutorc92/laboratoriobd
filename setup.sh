#!/bin/bash
sudo docker stop arangolei
sudo docker rm arangolei
sudo docker run -e ARANGO_ROOT_PASSWORD=testando --name arangolei -p 8529:8529 -d arangodb:3.1.21

