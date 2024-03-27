from typing import Optional


def generate_dagster_k8s_resource_tags(
        cpu_request: str,
        memory_request: str,
        cpu_limit: Optional[str] = None,
        memory_limit: Optional[str] = None,
) -> dict:
    if not cpu_limit:
        cpu_limit = cpu_request

    if not memory_limit:
        memory_limit = memory_request

    return {
        "dagster-k8s/config": {
            "container_config": {
                "resources": {
                    "requests": {"cpu": cpu_request, "memory": memory_request},
                    "limits": {"cpu": cpu_limit, "memory": memory_limit}
                }
            }
        }
    }
