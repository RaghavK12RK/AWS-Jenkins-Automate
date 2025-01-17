#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull raghavendrark14/simple-python-flask-app

# Run the Docker image as a container
docker run -d -p 5040:5040 raghavendrark14/simple-python-flask-app
