# coding: utf-8

# flake8: noqa

"""
    Fitbit Web API Explorer

    Fitbit provides a Web API for accessing data from Fitbit activity trackers, Aria scale, and manually entered logs. Anyone can develop an application to access and modify a Fitbit user's data on their behalf, so long as it complies with Fitbit Platform Terms of Service. These Swagger UI docs do not currently support making Fitbit API requests directly. In order to make a request, construct a request for the appropriate endpoint using this documentation, and then add an Authorization header to each request with an access token obtained using the steps outlined here: https://dev.fitbit.com/build/reference/web-api/developer-guide/authorization/.  # noqa: E501

    OpenAPI spec version: 1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from fitbit_web_api.api.active_zone_minutes_intraday_time_series_api import (
    ActiveZoneMinutesIntradayTimeSeriesApi,
)
from fitbit_web_api.api.active_zone_minutes_time_series_api import (
    ActiveZoneMinutesTimeSeriesApi,
)
from fitbit_web_api.api.activity_api import ActivityApi
from fitbit_web_api.api.activity_intraday_time_series_api import (
    ActivityIntradayTimeSeriesApi,
)
from fitbit_web_api.api.activity_time_series_api import ActivityTimeSeriesApi
from fitbit_web_api.api.authorization_api import AuthorizationApi
from fitbit_web_api.api.body_api import BodyApi
from fitbit_web_api.api.body_time_series_api import BodyTimeSeriesApi
from fitbit_web_api.api.breathing_rate_api import BreathingRateApi
from fitbit_web_api.api.breathing_rate_intraday_api import BreathingRateIntradayApi
from fitbit_web_api.api.cardio_fitness_score__vo2_max_api import (
    CardioFitnessScoreVO2MaxApi,
)
from fitbit_web_api.api.devices_api import DevicesApi
from fitbit_web_api.api.electrocardiogram_api import ElectrocardiogramApi
from fitbit_web_api.api.friends_api import FriendsApi
from fitbit_web_api.api.heart_rate_intraday_time_series_api import (
    HeartRateIntradayTimeSeriesApi,
)
from fitbit_web_api.api.heart_rate_time_series_api import HeartRateTimeSeriesApi
from fitbit_web_api.api.heart_rate_variability_api import HeartRateVariabilityApi
from fitbit_web_api.api.heart_rate_variability_intraday_api import (
    HeartRateVariabilityIntradayApi,
)
from fitbit_web_api.api.nutrition_api import NutritionApi
from fitbit_web_api.api.nutrition_time_series_api import NutritionTimeSeriesApi
from fitbit_web_api.api.sleep_api import SleepApi
from fitbit_web_api.api.sp_o2_api import SpO2Api
from fitbit_web_api.api.sp_o2_intraday_api import SpO2IntradayApi
from fitbit_web_api.api.subscriptions_api import SubscriptionsApi
from fitbit_web_api.api.temperature_api import TemperatureApi
from fitbit_web_api.api.user_api import UserApi

# import ApiClient
from fitbit_web_api.api_client import ApiClient
from fitbit_web_api.configuration import Configuration

# import models into sdk package
from fitbit_web_api.models.food_item import FoodItem
from fitbit_web_api.models.meal import Meal
from fitbit_web_api.models.oauth2_introspect_body import Oauth2IntrospectBody
from fitbit_web_api.models.oauth2_revoke_body import Oauth2RevokeBody
from fitbit_web_api.models.profile_json_body import ProfileJsonBody