#!/bin/bash
# update code
project_dir="/opt/src/DeployMachineLearningModel/"
cd $project_dir && git pull

# build and run with new code
running_container=$(docker ps | grep deploy_ml_model | awk  -F ' ' '{print $1}')
if [ -n "$running_container" ]; then
    echo "container id not empty, stop it firstly"
    docker stop $running_container
else
    echo "empty container id"
fi
docker build -t deploy_ml_model .
docker image rm -f $(docker images -f "dangling=true" -q)
docker run -p 8000:5000 deploy_ml_model
