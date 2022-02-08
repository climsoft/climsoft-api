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

### Swagger docs
Go to http://localhost:5080 for swagger doc

A copy of autogenerated OpenAPI definition is available [here](swagger/openapi.json) 

#### Swagger doc screenshot

![swagger doc](./swagger/screenshot.png)