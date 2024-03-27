from dagster import load_assets_from_package_module, materialize_to_memory

from core.resources.data_generator import DataGenerator


def test_preprocessing():
    from core.assets import preprocessing

    result = materialize_to_memory(
        resources={
            "data_generator": DataGenerator(),
        },
        assets=[
            *load_assets_from_package_module(preprocessing, "preprocessing"),
        ],
    )

    assert result.success


def test_training():
    from core.assets import preprocessing, training

    result = materialize_to_memory(
        resources={
            "data_generator": DataGenerator(),
        },
        assets=[
            *load_assets_from_package_module(preprocessing, "preprocessing"),
            *load_assets_from_package_module(training, "training"),
        ],
    )

    assert result.success
