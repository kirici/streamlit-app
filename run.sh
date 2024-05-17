#!/bin/bash
set -eu

# Global consts
CTR_PORT=9090

# Global vars
SCRIPT_PATH="$(dirname "$(realpath "$0")")"
PROJECT_NAME="${SCRIPT_PATH##*/}"

podman run \
  -td \
  --replace \
  -p "${CTR_PORT}":8501 \
  --name "${PROJECT_NAME}" \
  "${PROJECT_NAME}":latest
