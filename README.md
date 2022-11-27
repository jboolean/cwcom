# cw

## Install dependencies

### System dependencies
[Install `poetry`](https://python-poetry.org/docs/#installation), a python dependency manager, globally.


On Mac:

```shell
brew install poetry
```

and also Docker, which is used to package dependencies in a lambda-like virtual environment

```
brew install docker
```

Docker must be running to package for deploys.

### JS dependencies

```
nvm use
npm install
```

### Python dependencies:

```
poetry install
```

## Run dev server

```
npm run start
```

## Deployment
The production environments consists of
- Django running in AWS Lambda
- media in an S3 bucket
- statics in an s3 bucket
- Database in RDS Postgres

npm is installed with serverless to facilitate deployment to lambda

Docker is required for building dependencies for lambda during deployment