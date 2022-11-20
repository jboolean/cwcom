# cw

## Install dependencies

```
nvm use
npm install
npm run bootstrap
npm run buildout
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