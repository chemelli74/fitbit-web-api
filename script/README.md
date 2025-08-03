# Scripts

The scripts in this directory are used to generate the python client library from the public Fitbit OpenAPI specification.

## Schema Generation

The `generate-schema.sh` script is used to download the latest schema from the
Fitbit API. This script downloads the swagger file and converts it to an
OpenAPI specification (`openapi/fitbit-web-api-openapi.json`).

## Schema Upgrades

The upstream Fitbit OpenAPI specification is incomplete and is missing response
schemas for most API endpoints. The `upgrade-schema.py` script is used to
fix these issues and produce a more complete schema.

The script takes `openapi/fitbit-web-api-openapi.json` as input and produces
`openapi/fitbit-web-api-openapi-fixed.json` as output. This fixed schema is
then used for API generation.

The upgrade process works as follows:

1.  **Bug Fixes**: The script applies a series of hardcoded fixes for known
    issues in the upstream schema.
2.  **Dynamic Schema Loading**: The script dynamically loads all `*.json` files
    from the `openapi/model/` directory. Each file is expected to contain a
    JSON schema definition for a single data model or API response. The filename
    is converted from `snake_case` to `PascalCase` to create the schema name
    (e.g., `get_sleep_goal_response.json` becomes `GetSleepGoalResponse`).
3.  **Response Mapping**: A `PATH_CONFIG` dictionary within the script maps API
    paths (e.g., `/1.2/user/-/sleep/goal.json`) to their corresponding response
    schemas that were loaded in the previous step.

This approach allows for a maintainable way to augment the upstream schema with
missing information. To add a new response schema, one would typically:

1.  Create a new JSON schema file in `openapi/model/` for the response object.
2.  Create another JSON schema file in `openapi/model/` for the data model if needed.
3.  Update the `PATH_CONFIG` in `upgrade-schema.py` to link the API path to the new response schema.

## Schema Coverage

This section tracks the progress of enhancing the OpenAPI schema with response
objects.

### Completed API Categories

- Sleep
- User

### Remaining API Categories

The following API categories still need to be updated with response schemas:

- Active Zone Minutes Intraday Time Series
- Active Zone Minutes Time Series
- Activity
- Activity Intraday Time Series
- Activity Time Series
- Authorization
- Body
- Body Time Series
- Breathing Rate
- Breathing Rate Intraday
- Cardio Fitness Score (VO2 Max)
- Devices
- Electrocardiogram
- Friends
- Heart Rate Intraday Time Series
- Heart Rate Time Series
- Heart Rate Variability
- Heart Rate Variability Intraday
- Irregular Rhythm Notifications
- Nutrition
- Nutrition Time Series
- SpO2
- SpO2 Intraday
- Subscriptions
- Temperature

## API Generation

The `generate-api.sh` script is used to generate the python client
library from the OpenAPI specification. This uses the `openapi-generator-cli`
to generate a `python-aiohttp` client from the `openapi/fitbit-web-api-openapi-fixed.json` file.
