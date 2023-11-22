#!/bin/bash

java -jar ./swagger-tools/swagger-codegen-cli.jar generate \
   -i https://dev.fitbit.com/build/reference/web-api/explore/fitbit-web-api-swagger.json \
   -l python \
   -o . \
   -DpackageName=fitbit-web-api \
   --library asyncio
