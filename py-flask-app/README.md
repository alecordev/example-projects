# Commands

- `docker-compose up`
- `docker-compose down`
- `docker-compose down --volumes`

Another way, running detached:

- `docker-compose up -d`
- `docker-compose stop`

Check the environment variables available for a given defined service (i.e. _web_):

- `docker-compose run web env`
