#! /bin/bash

# run docker container
echo "Running docker container..."
docker run --rm -d --name docker-nginx -p 5000:80 -v ~/docker-nginx/html:/usr/share/nginx/html nginx