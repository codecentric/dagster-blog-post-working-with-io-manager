import pytest
from dagster import build_asset_context
from dagster_aws.s3.resources import ResourceWithS3Configuration
from upath import UPath

from core.resources import S3UPathIOManagerFactory, S3PandasParquetIOManager

@pytest.mark.parametrize('io_manager', [S3PandasParquetIOManager])
def test_s3_upath_io_manager_factory(io_manager):
    """
    Test the `S3UPathIOManagerFactory` class and its ability to create
    IO managers that interact with S3 storage. This test verifies that
    the factory can create an IO manager instance with the correct S3
    bucket, prefix, and configuration details.
    """

    context = build_asset_context()

    # Define the S3 bucket, prefix, and configuration details
    s3_bucket = "my-bucket"
    s3_prefix = "my-prefix"
    s3_configuration = ResourceWithS3Configuration(
        aws_access_key_id="my-access-key",
        aws_secret_access_key="my-secret-key",
        endpoint_url="https://s3.amazonaws.com"
    )

    # Create an instance of the `S3UPathIOManagerFactory` class
    factory = io_manager(
        s3_bucket=s3_bucket,
        s3_prefix=s3_prefix,
        s3_configuration=s3_configuration
    )

    # Create an IO manager using the factory
    im = factory.create_io_manager(context)

    # Verify that the IO manager was created successfully
    assert im is not None

    # Verify that the IO manager has the correct S3 bucket, prefix, and configuration
    assert im._base_path.path == UPath(f"s3://{s3_bucket}/{s3_prefix}").path

    assert isinstance(im, io_manager.io_manager_class.__annotations__["return"])

