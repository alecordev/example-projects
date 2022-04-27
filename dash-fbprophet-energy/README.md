Docker build:

`docker build --tag python-docker .`

List images:

`docker images`

Tag an image (just built):

- `docker build -t name .`
- `docker tag python-docker:latest python-docker:v1.0.0`

Run and open a port:

`docker run --publish 5000:5000 python-docker`

Run in detached mode:

`docker run -d -p 5000:5000 python-docker`

Run command / connect to running Container:

`docker exec -it CONTAINER /bin/bash`
