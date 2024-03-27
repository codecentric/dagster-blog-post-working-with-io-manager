from core.utils.generate_dagster_k8s_resource_tags import generate_dagster_k8s_resource_tags


def test_generate_dagster_k8s_resource_tags():
    assert generate_dagster_k8s_resource_tags("128m", "1Gi") == {
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": "128m", "memory": "1Gi"},
                    "limits": {"cpu": "128m", "memory": "1Gi"}
                }
            }
        }
    }

    assert generate_dagster_k8s_resource_tags("128m", "1Gi", "256m", "2Gi") == {
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": "128m", "memory": "1Gi"},
                    "limits": {"cpu": "256m", "memory": "2Gi"}
                }
            }
        }
    }