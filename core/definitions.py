import os

from dagster import Definitions

from core.jobs import preprocessing_job, training_job, training_job_assets, preprocessing_job_assets
from core.resources import RESOURCES_PROD, RESOURCES_DEV

resources_by_deployment_name = {
    "PROD": RESOURCES_PROD,
    "DEV": RESOURCES_DEV
}

deployment_name = os.getenv("DEPLOYMENT_NAME", "PROD")

defs = Definitions(
    assets=[
        *preprocessing_job_assets,
        *training_job_assets,
    ],
    jobs=[
        preprocessing_job,
        training_job
    ],
    resources=resources_by_deployment_name[deployment_name],
)
