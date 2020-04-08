# standard
import base64
from pprint import pprint as p

# third party
import requests

# local

from config import request_registry

from exceptions import MissingRequiredParameters
from exceptions import ReportNotImplemented

from utils import find_value_in_nested_dict


class FiveTranAPI:
    """API wrapper for FiveTran
    
    Raises:
        ReportNotImplemented: if a report requested doesn't exist
        MissingRequiredParameters: if parameters are not present where required
        
    """

    BASE = "https://api.fivetran.com"
    VERSION = "v1"

    ENDPOINTS = request_registry

    def __init__(self, auth):
        self._auth = auth
        self._request_info = None
        self._section = None

    def __getattr__(self, val):
        """Overriding attr to build the API url
        
        Arguments:
            val {str} -- path to the request
        
        Raises:
            ReportNotImplemented: if a report is not available in the registry.yaml file
            MissingRequiredParameters: [description]
        
        Returns:
            self -- the instance itself
        """
        section = self._section
        if section:

            self._request_info, *_ = [
                request for request in self._request_info if request["name"] == val
            ]

        else:
            try:
                self._request_info = FiveTranAPI.ENDPOINTS[val]
                self._section = val
            except (KeyError):
                raise ReportNotImplemented(
                    "Report is not present. Please refer to config.request_registry or the documentation"
                )

        return self

    def _make_request(self, method, url, data=None):
        """Makes a request to the FiveTran API
        
        Arguments:
            method {str} -- get, put, patch, etc
            url {str} -- the fully formed url to request
        
        Keyword Arguments:
            data {dict} -- any data to be sent to the api (default: {None})
        
        Returns:
            dict -- dict value representation of the request output
        """

        return requests.request(
            method, url, json=data, auth=(self._auth.api_key, self._auth.api_secret),
        ).json()

    def execute(self, data=None, **params):
        """Performs the HTTP request to FiveTran
        
        Keyword Arguments:
            data {dict} -- data to be sent to the api (default: {None})
        
        Raises:
            MissingRequiredParameters: checks to ensure required params are provided
        
        Returns:
            dict -- FiveTran's API response
        """

        request = self._request_info

        # check required fields
        required = request.get("required", [])

        for field in required:
            if field not in params.keys():
                raise MissingRequiredParameters(
                    f"Missing the following parameters: {field}"
                )

        # build request
        path = request["path"].format(**params)
        method = request["method"]

        url = "/".join([FiveTranAPI.BASE, FiveTranAPI.VERSION, path])
        dict_path = request["dict_path"]

        # make request
        resp = self._make_request(method, url, data)

        # parse request
        parsed = find_value_in_nested_dict(dict_path, resp)

        return parsed
