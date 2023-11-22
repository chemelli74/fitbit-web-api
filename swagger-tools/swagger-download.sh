#!/bin/bash

# Download current stable 3.x.x branch (OpenAPI version 3)

STABLE="3.0.51"

wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/$STABLE/swagger-codegen-cli-$STABLE.jar -O swagger-codegen-cli.jar
