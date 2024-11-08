#!/bin/bash

sudo apt-get update
sudo apt-get install python3 git docker.io -y
sudo systemctl enable --now docker
sudo systemctl start docker

sudo docker pull 

sleep 20s

sudo docker pull bilac88/demoday-dvp-202403

sleep 30s

sudo docker run --name api_demoday -d -p 8000:8000 bilac88/demoday-dvp-202403
