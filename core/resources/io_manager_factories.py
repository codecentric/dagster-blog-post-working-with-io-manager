from abc import ABC, abstractmethod
from typing import Optional

from dagster import ResourceDependency, ConfigurableIOManagerFactory, build_asset_context
from dagster_aws.s3.resources import ResourceWithS3Configuration
from pydantic import Field
from upath import UPath


class LocalUPathIOManagerFactory(ConfigurableIOManagerFactory, ABC):
    """
      An abstract base class for creating IO managers that interact with local file systems.

      This class provides a framework for creating IO managers that can be configured
      to work with local file systems. It inherits from `ConfigurableIOManagerFactory` and is
      designed to be extended by subclasses that implement specific IO manager types for local
      storage.

      Attributes:
          base_path (Optional[str]): An optional base path for the IO manager. If not provided,
              the IO manager will use the storage directory specified in the context. This attribute
              specifies the root directory where the IO manager will read from or write to.
    """
    base_path: Optional[str] = Field(default=None)

    @abstractmethod
    def io_manager_class(self):
        raise NotImplementedError

    def create_io_manager(self, context):
        return self.io_manager_class()(
            base_path=UPath(
                self.base_path or context.instance.storage_directory()
            )
        )


class S3UPathIOManagerFactory(ConfigurableIOManagerFactory, ABC):
    """
      An abstract base class for creating IO managers that interact with S3 storage.

      This class provides a framework for creating IO managers that can be configured
      to work with S3 storage. It inherits from `ConfigurableIOManagerFactory` and is
      designed to be extended by subclasses that implement specific IO manager types.

      Attributes:
          s3_bucket (str): The S3 bucket to use for the IO manager. This attribute
              specifies the name of the S3 bucket where the IO manager will read
              from or write to.

          s3_prefix (str): The S3 prefix to use for the IO manager. This attribute
              specifies the prefix within the S3 bucket that the IO manager will
              use to organize its data.

          s3_configuration (ResourceDependency[ResourceWithS3Configuration]): A
              dependency on a resource that provides S3 configuration details,
              including access keys and endpoint URLs. This attribute is used
              to configure the IO manager's connection to S3.
      """

    s3_bucket: str = Field(description="The S3 bucket to use for the IO manager.")
    s3_prefix: str = Field(description="The S3 prefix to use for the IO manager.")
    s3_configuration: ResourceDependency[ResourceWithS3Configuration]

    @abstractmethod
    def io_manager_class(self):
        """
        This abstract method must be implemented by subclasses
        to return the class of the IO manager that this factory will create.
        The returned class should be a subclass of `UPathIOManager` or a similar
        base class for IO managers that interact with S3 storage.

        :return: The class of the IO manager that this factory will create.
        """
        raise NotImplementedError

    def create_io_manager(self, context):
        """
        Creates and returns an instance of the IO
        manager class specified by the `io_manager_class` method. The IO
        manager is configured with the S3 bucket, prefix, and configuration
        details provided by this factory.

        :return: An instance of the IO manager class specified by the `io_manager_class` method.
        """
        return self.io_manager_class()(
            base_path=UPath(
                # Construct the S3 path from the bucket and prefix
                f"s3://{self.s3_bucket}/{self.s3_prefix}",

                # Configure the IO manager with the S3 configuration
                key=self.s3_configuration.aws_access_key_id,
                secret=self.s3_configuration.aws_secret_access_key,
                client_kwargs={
                    "endpoint_url": self.s3_configuration.endpoint_url
                }
            )
        )


