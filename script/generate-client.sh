#!/bin/bash

OUTPUT_DIR="."
CONFIG_FILE="openapi/openapi-config.yaml"
OPENAPI_SPEC="openapi/fitbit-web-api-openapi-fixed.json"
PACKAGE_URL="https://github.com/chemelli74/fitbit-web-api"

docker run --rm -v "${PWD}:/data" openapitools/openapi-generator-cli generate \
   --input-spec /data/${OPENAPI_SPEC} \
   --generator-name python \
   --output /data/${OUTPUT_DIR} \
   --config /data/${CONFIG_FILE} \
   --package-name fitbit_web_api \
