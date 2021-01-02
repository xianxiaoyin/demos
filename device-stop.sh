#!/usr/bin/env bash

docker ps -a  | grep dp

if [ $? -eq 0 ]; then
    docker stop dp && docker rm dp
fi


