#!/bin/bash
#
# This script downloads the OpenAPI specification for the Fitbit Web API
# and saves it to the openapi directory.

OPENAPI_DIR="openapi"
if [ ! -d "${OPENAPI_DIR}" ]; then
  echo "Output directory '${OPENAPI_DIR}' does not exist. Please run the script from the project root directory."
  exit 1
fi

curl https://dev.fitbit.com/build/reference/web-api/explore/fitbit-web-api-swagger.json \
  --output ${OPENAPI_DIR}/fitbit-web-api-swagger.json

curl -X 'POST' \
  'https://converter.swagger.io/api/convert' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d @${OPENAPI_DIR}/fitbit-web-api-swagger.json \
    | jq \
    > ${OPENAPI_DIR}/fitbit-web-api-openapi.json
