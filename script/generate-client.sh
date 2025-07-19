#!/bin/bash

OUTPUT_DIR="xxx"
OPENAPI_SPEC="openapi/fitbit-web-api-openapi-fixed.json"

docker run --rm -v "${PWD}:/data" openapitools/openapi-generator-cli generate \
   --input-spec /data/${OPENAPI_SPEC} \
   --generator-name python \
   --output /data/${OUTPUT_DIR} \
   --package-name fitbit_web_api \
