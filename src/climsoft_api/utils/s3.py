import minio


def get_minio_client(settings):
    client = minio.Minio(
        's3.amazonaws.com',
        access_key=settings.AWS_ACCESS_KEY_ID,
        secret_key=settings.AWS_SECRET_ACCESS_KEY,
        region=settings.AWS_REGION
    )
    return client


def create_presigned_url(settings, bucket_name, object_name):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    client = get_minio_client(settings)
    return client.get_presigned_url(
        method='GET',
        bucket_name=bucket_name,
        object_name=object_name
    )
