# CONTRIBUTING

## How to run the Dockerfile locally

```shell
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run"
```