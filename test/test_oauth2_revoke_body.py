# coding: utf-8

"""
    Fitbit Web API Explorer

    Fitbit provides a Web API for accessing data from Fitbit activity trackers, Aria scale, and manually entered logs. Anyone can develop an application to access and modify a Fitbit user's data on their behalf, so long as it complies with Fitbit Platform Terms of Service. These Swagger UI docs do not currently support making Fitbit API requests directly. In order to make a request, construct a request for the appropriate endpoint using this documentation, and then add an Authorization header to each request with an access token obtained using the steps outlined here: https://dev.fitbit.com/build/reference/web-api/developer-guide/authorization/.  # noqa: E501

    OpenAPI spec version: 1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fitbit_web_api
from fitbit_web_api.models.oauth2_revoke_body import Oauth2RevokeBody  # noqa: E501
from fitbit_web_api.rest import ApiException


class TestOauth2RevokeBody(unittest.TestCase):
    """Oauth2RevokeBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOauth2RevokeBody(self):
        """Test Oauth2RevokeBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = fitbit_web_api.models.oauth2_revoke_body.Oauth2RevokeBody()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()