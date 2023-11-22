#!/bin/bash

java -jar ./swagger-tools/swagger-codegen-cli.jar generate \
   -i https://dev.fitbit.com/build/reference/web-api/explore/fitbit-web-api-swagger.json \
   -l python \
   -o .

# Restore projetc name after automatic file update
sed -i -e 's/swagger-client/fitbit-web-api/g' setup.py
