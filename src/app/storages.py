from os import environ

S3_STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": environ.get("AWS_STORAGE_BUCKET_NAME"),
            "access_key": environ.get("AWS_S3_ACCESS_KEY_ID"),
            "secret_key": environ.get("AWS_SECRET_ACCESS_KEY"),
            "region_name": environ.get("AWS_S3_REGION_NAME"),
            "location": "media",
            "gzip": False,
            "default_acl": "private",
            "querystring_auth": True,
            "signature_version": "s3v4",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": environ.get("AWS_STORAGE_BUCKET_NAME"),
            "access_key": environ.get("AWS_S3_ACCESS_KEY_ID"),
            "secret_key": environ.get("AWS_SECRET_ACCESS_KEY"),
            "region_name": environ.get("AWS_S3_REGION_NAME"),
            "location": "static",
            "gzip": True,
            "default_acl": "public-read",
            "querystring_auth": False,
            "signature_version": "s3v4",
        },
    },
}
