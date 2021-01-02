#!/usr/bin/env bash

docker ps -a  | grep dp

if [ $? -ne 0 ]; then
    docker stop dp && docker rm dp
fi


