from dagster import load_assets_from_package_module, define_asset_job

from core.assets import training, preprocessing
from core.utils.generate_dagster_k8s_resource_tags import generate_dagster_k8s_resource_tags

preprocessing_job_assets = load_assets_from_package_module(
    package_module=preprocessing,
    group_name="preprocessing"
)

preprocessing_job = define_asset_job(
    name="preprocessing_job",
    selection=preprocessing_job_assets,
    tags={**generate_dagster_k8s_resource_tags(cpu_request="128m", memory_request="1Gi")},
)

training_job_assets = load_assets_from_package_module(
    package_module=training,
    group_name="training"
)

training_job = define_asset_job(
    name="training_job",
    selection=training_job_assets,
    tags={**generate_dagster_k8s_resource_tags(cpu_request="128m", memory_request="1Gi")},
)
