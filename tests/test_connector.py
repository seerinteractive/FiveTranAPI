# standard
import os
import sys
import json
from pprint import pprint as p

# third party
import pytest
import yaml

# local
from fivetran.auth import Auth
from fivetran.client import FiveTranAPI

from fivetran.common.exceptions import MissingRequiredParameters
from fivetran.common.exceptions import ReportNotImplemented

from tests.fixtures import auth
from tests.fixtures import api
from tests.fixtures import _load_json



@pytest.mark.create_connector
def test_create_connector(api, monkeypatch):
    def mock_create_connector(*args, **kwargs):
        return _load_json("create_connector")

    monkeypatch.setattr(FiveTranAPI, "_make_request", mock_create_connector)
    data = {
        "service": "criteo",
        "group_id": "projected_sickle",
        "trust_certificates": True,
        "run_setup_tests": True,
        "config": {
            "schema": "criteo",
            "username": "myuser",
            "password": "mypassword",
            "app_token": "myapptoken",
        },
    }
    result = api.connector.create_connector.execute(data=data)

    assert result["connected_by"] == "interment_burdensome"


@pytest.mark.connector_details
def test_connector_details(api, monkeypatch):
    def mock_connector_details(*args, **kwargs):
        return _load_json("connector_details")

    monkeypatch.setattr(FiveTranAPI, "_make_request", mock_connector_details)

    result = api.connector.connector_details.execute(connector_id="123")
    assert result["id"] == "speak_inexpensive"


@pytest.mark.modify_connector
def test_modify_connector(api, monkeypatch):
    def mock_modify_connector(*args, **kwargs):
        return _load_json("modify_connector")

    monkeypatch.setattr(FiveTranAPI, "_make_request", mock_modify_connector)

    result = api.connector.modify_connector.execute(connector_id="123")

    assert result["connected_by"] == "interment_burdensome"


@pytest.mark.wrong_params
def test_wrong_params(api, monkeypatch):
    def mock_wrong_params(*args, **kwargs):
        return _load_json("connector_details")

    monkeypatch.setattr(FiveTranAPI, "_make_request", mock_wrong_params)

    with pytest.raises(MissingRequiredParameters) as e:
        api.connector.connector_details.execute(incorrect_param="123")


@pytest.mark.wrong_path
def test_wrong_path(api, monkeypatch):
    def mock_wrong_path(*args, **kwargs):
        return _load_json("connector_details")

    monkeypatch.setattr(FiveTranAPI, "_make_request", mock_wrong_path)

    with pytest.raises(ReportNotImplemented) as e:
        api.wrong.path.execute()
