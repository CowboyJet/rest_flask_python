# CONTRIBUTING

## How to run the Dockerfile locally

```shell
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run"
```

## How to connect to database locally

By default sqllite is used.
If you want to connect to for example a postgresql database, enter the database connection string in the .env file.
See .env_example
