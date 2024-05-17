#!/bin/bash
set -eu

# Global vars
SCRIPT_PATH="$(dirname "$(realpath "$0")")"
PROJECT_NAME="${SCRIPT_PATH##*/}"

podman tag "${PROJECT_NAME}":latest "${PROJECT_NAME}":previous
podman build \
  --label project="${PROJECT_NAME}" \
  -t "${PROJECT_NAME}":latest \
  -f "${SCRIPT_PATH}"/Containerfile \
  "${SCRIPT_PATH}"
podman rmi -f "${PROJECT_NAME}":previous
