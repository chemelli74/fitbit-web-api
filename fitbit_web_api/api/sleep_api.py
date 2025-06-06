# coding: utf-8

"""
Fitbit Web API Explorer

Fitbit provides a Web API for accessing data from Fitbit activity trackers, Aria scale, and manually entered logs. Anyone can develop an application to access and modify a Fitbit user's data on their behalf, so long as it complies with Fitbit Platform Terms of Service. These Swagger UI docs do not currently support making Fitbit API requests directly. In order to make a request, construct a request for the appropriate endpoint using this documentation, and then add an Authorization header to each request with an access token obtained using the steps outlined here: https://dev.fitbit.com/build/reference/web-api/developer-guide/authorization/.  # noqa: E501

OpenAPI spec version: 1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fitbit_web_api.api_client import ApiClient


class SleepApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_sleep(self, start_time, duration, _date, **kwargs):  # noqa: E501
        """Log Sleep  # noqa: E501

        Creates a log entry for a sleep event and returns a response in the format requested.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_sleep(start_time, duration, _date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_time: Start time includes hours and minutes in the format HH:mm. (required)
        :param int duration: Duration in milliseconds. (required)
        :param date _date: Log entry in the format yyyy-MM-dd. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.add_sleep_with_http_info(
                start_time, duration, _date, **kwargs
            )  # noqa: E501
        else:
            (data) = self.add_sleep_with_http_info(
                start_time, duration, _date, **kwargs
            )  # noqa: E501
            return data

    def add_sleep_with_http_info(
        self, start_time, duration, _date, **kwargs
    ):  # noqa: E501
        """Log Sleep  # noqa: E501

        Creates a log entry for a sleep event and returns a response in the format requested.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_sleep_with_http_info(start_time, duration, _date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_time: Start time includes hours and minutes in the format HH:mm. (required)
        :param int duration: Duration in milliseconds. (required)
        :param date _date: Log entry in the format yyyy-MM-dd. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["start_time", "duration", "_date"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_sleep" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'start_time' is set
        if "start_time" not in params or params["start_time"] is None:
            raise ValueError(
                "Missing the required parameter `start_time` when calling `add_sleep`"
            )  # noqa: E501
        # verify the required parameter 'duration' is set
        if "duration" not in params or params["duration"] is None:
            raise ValueError(
                "Missing the required parameter `duration` when calling `add_sleep`"
            )  # noqa: E501
        # verify the required parameter '_date' is set
        if "_date" not in params or params["_date"] is None:
            raise ValueError(
                "Missing the required parameter `_date` when calling `add_sleep`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "start_time" in params:
            query_params.append(("startTime", params["start_time"]))  # noqa: E501
        if "duration" in params:
            query_params.append(("duration", params["duration"]))  # noqa: E501
        if "_date" in params:
            query_params.append(("date", params["_date"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.2/user/-/sleep.json",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_sleep(self, log_id, **kwargs):  # noqa: E501
        """Delete Sleep Log  # noqa: E501

        Deletes a user's sleep log entry with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sleep(log_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str log_id: The ID of the sleep log to be deleted. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_sleep_with_http_info(log_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_sleep_with_http_info(log_id, **kwargs)  # noqa: E501
            return data

    def delete_sleep_with_http_info(self, log_id, **kwargs):  # noqa: E501
        """Delete Sleep Log  # noqa: E501

        Deletes a user's sleep log entry with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sleep_with_http_info(log_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str log_id: The ID of the sleep log to be deleted. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["log_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sleep" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'log_id' is set
        if "log_id" not in params or params["log_id"] is None:
            raise ValueError(
                "Missing the required parameter `log_id` when calling `delete_sleep`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "log_id" in params:
            path_params["log-id"] = params["log_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.2/user/-/sleep/{log-id}.json",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_sleep_by_date(self, _date, **kwargs):  # noqa: E501
        """Get Sleep Log  # noqa: E501

        The Get Sleep Logs by Date endpoint returns a summary and list of a user's sleep log entries (including naps) as well as detailed sleep entry data for a given day.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sleep_by_date(_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date _date: The date of records to be returned. In the format yyyy-MM-dd. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_sleep_by_date_with_http_info(_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sleep_by_date_with_http_info(
                _date, **kwargs
            )  # noqa: E501
            return data

    def get_sleep_by_date_with_http_info(self, _date, **kwargs):  # noqa: E501
        """Get Sleep Log  # noqa: E501

        The Get Sleep Logs by Date endpoint returns a summary and list of a user's sleep log entries (including naps) as well as detailed sleep entry data for a given day.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sleep_by_date_with_http_info(_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date _date: The date of records to be returned. In the format yyyy-MM-dd. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["_date"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sleep_by_date" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter '_date' is set
        if "_date" not in params or params["_date"] is None:
            raise ValueError(
                "Missing the required parameter `_date` when calling `get_sleep_by_date`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "_date" in params:
            path_params["date"] = params["_date"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.2/user/-/sleep/date/{date}.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_sleep_by_date_range(self, base_date, end_date, **kwargs):  # noqa: E501
        """Get Sleep Logs by Date Range  # noqa: E501

        The Get Sleep Logs by Date Range endpoint returns a list of a user's sleep log entries (including naps) as well as detailed sleep entry data for a given date range (inclusive of start and end dates).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sleep_by_date_range(base_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date base_date: The date of records to be returned. In the format yyyy-MM-dd. (required)
        :param date end_date: The date of records to be returned. In the format yyyy-MM-dd. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_sleep_by_date_range_with_http_info(
                base_date, end_date, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_sleep_by_date_range_with_http_info(
                base_date, end_date, **kwargs
            )  # noqa: E501
            return data

    def get_sleep_by_date_range_with_http_info(
        self, base_date, end_date, **kwargs
    ):  # noqa: E501
        """Get Sleep Logs by Date Range  # noqa: E501

        The Get Sleep Logs by Date Range endpoint returns a list of a user's sleep log entries (including naps) as well as detailed sleep entry data for a given date range (inclusive of start and end dates).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sleep_by_date_range_with_http_info(base_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date base_date: The date of records to be returned. In the format yyyy-MM-dd. (required)
        :param date end_date: The date of records to be returned. In the format yyyy-MM-dd. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["base_date", "end_date"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sleep_by_date_range" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'base_date' is set
        if "base_date" not in params or params["base_date"] is None:
            raise ValueError(
                "Missing the required parameter `base_date` when calling `get_sleep_by_date_range`"
            )  # noqa: E501
        # verify the required parameter 'end_date' is set
        if "end_date" not in params or params["end_date"] is None:
            raise ValueError(
                "Missing the required parameter `end_date` when calling `get_sleep_by_date_range`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "base_date" in params:
            path_params["base-date"] = params["base_date"]  # noqa: E501
        if "end_date" in params:
            path_params["end-date"] = params["end_date"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.2/user/-/sleep/date/{base-date}/{end-date}.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_sleep_goal(self, **kwargs):  # noqa: E501
        """Get Sleep Goal  # noqa: E501

        Returns the user's sleep goal.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sleep_goal(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_sleep_goal_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sleep_goal_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sleep_goal_with_http_info(self, **kwargs):  # noqa: E501
        """Get Sleep Goal  # noqa: E501

        Returns the user's sleep goal.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sleep_goal_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sleep_goal" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.2/user/-/sleep/goal.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_sleep_list(self, sort, offset, limit, **kwargs):  # noqa: E501
        """Get Sleep Logs List  # noqa: E501

        The Get Sleep Logs List endpoint returns a list of a user's sleep logs (including naps) before or after a given day with offset, limit, and sort order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sleep_list(sort, offset, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The sort order of entries by date asc (ascending) or desc (descending). (required)
        :param int offset: The offset number of entries. (required)
        :param int limit: The maximum number of entries returned (maximum;100). (required)
        :param date before_date: The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified.
        :param date after_date: The date in the format yyyy-MM-ddTHH:mm:ss.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_sleep_list_with_http_info(
                sort, offset, limit, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_sleep_list_with_http_info(
                sort, offset, limit, **kwargs
            )  # noqa: E501
            return data

    def get_sleep_list_with_http_info(
        self, sort, offset, limit, **kwargs
    ):  # noqa: E501
        """Get Sleep Logs List  # noqa: E501

        The Get Sleep Logs List endpoint returns a list of a user's sleep logs (including naps) before or after a given day with offset, limit, and sort order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sleep_list_with_http_info(sort, offset, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The sort order of entries by date asc (ascending) or desc (descending). (required)
        :param int offset: The offset number of entries. (required)
        :param int limit: The maximum number of entries returned (maximum;100). (required)
        :param date before_date: The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified.
        :param date after_date: The date in the format yyyy-MM-ddTHH:mm:ss.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "sort",
            "offset",
            "limit",
            "before_date",
            "after_date",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sleep_list" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'sort' is set
        if "sort" not in params or params["sort"] is None:
            raise ValueError(
                "Missing the required parameter `sort` when calling `get_sleep_list`"
            )  # noqa: E501
        # verify the required parameter 'offset' is set
        if "offset" not in params or params["offset"] is None:
            raise ValueError(
                "Missing the required parameter `offset` when calling `get_sleep_list`"
            )  # noqa: E501
        # verify the required parameter 'limit' is set
        if "limit" not in params or params["limit"] is None:
            raise ValueError(
                "Missing the required parameter `limit` when calling `get_sleep_list`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "before_date" in params:
            query_params.append(("beforeDate", params["before_date"]))  # noqa: E501
        if "after_date" in params:
            query_params.append(("afterDate", params["after_date"]))  # noqa: E501
        if "sort" in params:
            query_params.append(("sort", params["sort"]))  # noqa: E501
        if "offset" in params:
            query_params.append(("offset", params["offset"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.2/user/-/sleep/list.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_sleep_goal(self, min_duration, **kwargs):  # noqa: E501
        """Update Sleep Goal  # noqa: E501

        Create or update the user's sleep goal and get a response in the JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sleep_goal(min_duration, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str min_duration: Duration of sleep goal. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_sleep_goal_with_http_info(
                min_duration, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_sleep_goal_with_http_info(
                min_duration, **kwargs
            )  # noqa: E501
            return data

    def update_sleep_goal_with_http_info(self, min_duration, **kwargs):  # noqa: E501
        """Update Sleep Goal  # noqa: E501

        Create or update the user's sleep goal and get a response in the JSON format.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_sleep_goal_with_http_info(min_duration, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str min_duration: Duration of sleep goal. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["min_duration"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_sleep_goal" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'min_duration' is set
        if "min_duration" not in params or params["min_duration"] is None:
            raise ValueError(
                "Missing the required parameter `min_duration` when calling `update_sleep_goal`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "min_duration" in params:
            query_params.append(("minDuration", params["min_duration"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.2/user/-/sleep/goal.json",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
