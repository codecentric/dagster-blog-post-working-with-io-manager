from core.definitions import defs


def test_defs_can_load():
    # sanity check
    loaded_jobs = defs.get_all_job_defs()
    expected_job_names = [
        "__ASSET_JOB",  # internal dagster job. always present.
        "training_job",
        "preprocessing_job"
    ]

    for job in loaded_jobs:
        assert job.name in expected_job_names
        expected_job_names.remove(job.name)

    # No need to check if resources are loaded, as dagster will throw an error if they are not.
