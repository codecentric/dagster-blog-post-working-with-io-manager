from dagster import EnvVar, FilesystemIOManager
from dagster_aws.s3 import S3Resource, S3PickleIOManager

from core.resources.csv_io_manager import S3CSVIOManager, CSVIOManager
from core.resources.data_generator import DataGenerator
from core.resources.io_manager_factories import S3UPathIOManagerFactory
from core.resources.model_io_manager import S3ModelIOManager, ModelIOManager
from core.resources.pandas_parquet_io_manager import S3PandasParquetIOManager, PandasParquetIOManager

# Resource that gives access to S3.
# S3Resource provides a get_client method that returns a boto3 client for interacting with S3.
# For our purposes, we will use the S3Resource to pass just the credentials to our IOManagers.
# This works because S3Resource is a subclass of ResourceWithS3Configuration, which is what
# we use in our IOManagers to configure s3fs

s3_resource = S3Resource(
    aws_access_key_id=EnvVar('MINIO_ACCESS_KEY'),
    aws_secret_access_key=EnvVar('MINIO_SECRET_KEY'),
    endpoint_url=EnvVar('MINIO_HOST')
)

RESOURCES_PROD = {
    "io_manager": S3PickleIOManager(
        s3_resource=s3_resource,
        s3_bucket="dagster-runs"
    ),
    "parquet_io_manager": S3PandasParquetIOManager(
        s3_bucket="processing",
        s3_prefix="parquet_files",
        s3_configuration=s3_resource
    ),
    "csv_io_manager": S3CSVIOManager(
        s3_bucket="processing",
        s3_prefix="csv_files",
        s3_configuration=s3_resource
    ),
    "model_io_manager": S3ModelIOManager(
        s3_bucket="processing",
        s3_prefix="models",
        s3_configuration=s3_resource
    ),
    "data_generator": DataGenerator(),
}

RESOURCES_DEV = {
    "io_manager": FilesystemIOManager(),
    "parquet_io_manager": PandasParquetIOManager(),
    "csv_io_manager": CSVIOManager(),
    "model_io_manager": ModelIOManager(),
    "data_generator": DataGenerator(),
}
