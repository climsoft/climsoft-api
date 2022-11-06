# climsoft-api

To run this project, do the following (assuming you have docker-compose installed)

```bash
$ git clone https://github.com/opencdms/climsoft-api.git
$ cd climsoft-api
$ docker-compose up -d --build
```

### Configure climsoft-api

We can configure the API using different environment variables. Here is a list of them:

```
CLIMSOFT_SECRET_KEY
CLIMSOFT_DATABASE_URI
CLIMSOFT_FILE_STORAGE ["disk" or "s3"]
CLIMSOFT_S3_BUCKET
CLIMSOFT_AWS_REGION
CLIMSOFT_AWS_ACCESS_KEY_ID
CLIMSOFT_AWS_SECRET_ACCESS_KEY
CLIMSOFT_UPLOAD_DIR
CLIMSOFT_S3_SIGNED_URL_VALIDITY [in hours as integer]
CLIMSOFT_AUTH_ENABLED [true, false]
```
There is also an `.env.example` file. You can copy/rename this to `.env` and put correct
values. This will automatically be loaded when you run `docker-compose up -d --build`


### Serving images

When you upload an image via `/v1/file-upload/image` you get a response either like
```json
{
  "status": "success",
  "message": "Image uploaded successfully!",
  "result": [
    {
      "uploaded_to": {
        "storage": "s3",
        "object_key": "ddd77aa358c946aea925fcaee40ae8d9.png"
      }
    }
  ]
}
```
 or like

```json
{
  "status": "success",
  "message": "Image uploaded successfully!",
  "result": [
    {
      "uploaded_to": {
        "storage": "disk",
        "filepath": "climsoft_uploads/ddd77aa358c946aea925fcaee40ae8d9.png"
      }
    }
  ]
}
```

To retrieve the images, if the storage is s3, you will get the image at 
```
https://serveraddress/v1/s3/image/ddd77aa358c946aea925fcaee40ae8d9.png
```
if the storage is disk, you will get the image at
```
https://serveraddress/climsoft_uploads/ddd77aa358c946aea925fcaee40ae8d9.png
```

### Multi Deployments
There is a deployment.yml file in the repository root that you can use to deploy multiple instance at once. This will 
run one independent instance for each deployment of Climsoft API on this root URL: `http://domain.tld/{deployment_key}/climsoft`.
You can configure database uri and server name for each deployment.

Here is an example `deployment.yml` file for you:

```yaml
empty-database:
  NAME: Climsoft Deployment With Empty DB
  DATABASE_URI: "mysql+mysqldb://root:password@mariadb/climsoft"
  S3_BUCKET: climsoft-paper-archive
  AWS_REGION: eu-west-2
  AWS_ACCESS_KEY_ID: ACCESS_KEY_ID
  AWS_SECRET_ACCESS_KEY: SECRET_ACCESS_KEY

test-database:
  NAME: Climsoft Deployment With Test Data
  DATABASE_URI: "mysql+mysqldb://root:password@mariadb/mariadb_climsoft_test_db_v4"
  S3_BUCKET: climsoft-paper-archive
  AWS_REGION: eu-west-2
  AWS_ACCESS_KEY_ID: ACCESS_KEY_ID
  AWS_SECRET_ACCESS_KEY: SECRET_ACCESS_KEY
```

#### Selecting database
Whe you are on a server where multiple instances of climsoft were deployed, you need to choose a database when you authenticate.
This choice is stored in your access token and used later for making queries.

Look at the following screenshot,

![login form modal](./screenshots/login-form-modal.png)

When you are using multi-deployment, all the deployment keys will be listed as scopes.
You can choose any of the scopes and that database will be used to authenticate you.

Keep in mind that,
- if you choose multiple scopes, only the first one will be used
- if you choose none, database uri configured by `CLIMSOFT_DATABSE_URI` will be used.

When you are using the swagger doc located in `http(s)://domain.tld/docs#/default/authenticate_token_post`
(see the following screenshot),

![login form](./screenshots/login-form.png)

you have to put the scope yourself as, `deployment_key:{key}` (omit the curly braces), such that for the following config;

```yaml
test:
  NAME: Climsoft Test
  DATABASE_URI: "mysql+mysqldb://root:password@mariadb/climsoft"
```
if you want to choose database uri for `test` deployment, you have to put
`deployment_key:test` in scope (marked in screenshot)

### Design Exceptions

Climsoft tables often has composite primary keys. In that case, we usually 
receive all the primary keys as path parameters and then use them to make distinction
between rows. But there is some exceptions. Such as - 

- Physical Feature model has a column named `description`, but we are not using
it in path parameters. Instead, we are raising an exception where other primary keys
are same but description is different.


### Deployment

The default deployment config of this repository contains two deployments. One with an empty database and another one with
a seeded database with test data. If you do not want multi-deployment, delete `deployment.yml` from repository root. It will
deploy an instance with an empty database.

When you run single instance, the URL to sawgger doc is: http(s)://domain.tld/climsoft

When you run multi-deplyment, the URL to swagger doc is: http(s)://domain.tld/{deployment_key}/climsoft


#### Steps to follow

There are some scripts in `scripts` directory that can help you to deploy this
repository on a server.

```bash
$ cd scripts
$ chmod +x install-docker.sh
$ chmod +x install-docker-compose.sh
$ ./install-docker.sh
$ newgrp docker
$ ./install-docker-compose.sh
$ cd ..
$ docker-compose -f docker-compose.reference.yml up -d --build
```

If you want to restore database and other volumes each hour,

```bash
$ cd scripts
$ chmod +x restore-db.sh 
$ crontab e
$ 0 * * * * /path/to/this/repo/root/scripts/restore-db.sh /path/to/this/repo/root/docker-compose.reference.yml
```

### Swagger docs
Go to http://localhost:5080 for swagger doc

A copy of autogenerated OpenAPI definition is available [here](swagger/openapi.json) 

#### Swagger doc screenshot

![swagger doc](./swagger/screenshot.png)
