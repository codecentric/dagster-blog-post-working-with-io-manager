#!/bin/bash

sleep 5

buckets=("processing" "artifacts" "dagster-runs")

mc alias set local "${MINIO_ENDPOINT}" "${MINIO_ACCESS_KEY}" "${MINIO_SECRET_KEY}"

# Iterate over the array and create buckets using mc CLI
for bucket_name in "${buckets[@]}"; do
    mc mb local/"$bucket_name"
done