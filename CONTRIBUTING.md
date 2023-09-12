# CONTRIBUTING

## How to run the Dockerfile locally

```shell
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run"
```

## How to run the docker worker locally

```shell
docker run -w /app --network=host flask-smorest-api sh -c "rq worker -u redis://localhost:6379 emails"
```

The --network=host is needed if you're running a local redis on wsl as a service

## How to connect to database locally

By default SQLite is used.
If you want to connect to for example a Postgresql database, enter the database connection string in the .env file.
See .env_example

## Starting the Postgresql and Redis services

```shell
sudo systemctl start postgresql
sudo systemctl start redis-server
```
