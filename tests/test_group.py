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

sys.path.append("..")


@pytest.fixture
def auth():

    FIVETRAN_API_KEY = os.environ.get("FIVETRAN_API_KEY", "123")
    FIVETRAN_API_SECRET = os.environ.get("FIVETRAN_API_SECRET", "123")

    return Auth(api_key=FIVETRAN_API_KEY, api_secret=FIVETRAN_API_SECRET)


@pytest.fixture
def api(auth):
    return FiveTranAPI(auth=auth)


def _load_json(filename):
    with open(f"data/{filename}.json", "r") as f:
        return json.loads(f.read())


@pytest.mark.get_groups
def test_get_groups(api, monkeypatch):
    def mock_get_groups(*args, **kwargs):
        return _load_json("get_groups")

    monkeypatch.setattr(FiveTranAPI, "_make_request", mock_get_groups)

    groups = api.group.get_groups.execute()

    assert len(groups)


@pytest.mark.get_connectors
def test_get_connectors(api, monkeypatch):
    def mock_get_connectors(*args, **kwargs):
        return _load_json("get_connectors")

    monkeypatch.setattr(FiveTranAPI, "_make_request", mock_get_connectors)

    connectors = api.group.get_connectors.execute(group_id="projected_sickle")
    connector, *_ = connectors
    assert connector["id"] == "iodize_impressive"


@pytest.mark.get_group_details
def test_get_group_details(api, monkeypatch):
    def mock_get_group_details(*args, **kwargs):
        return _load_json("get_group_details")

    monkeypatch.setattr(FiveTranAPI, "_make_request", mock_get_group_details)

    results = api.group.get_group_details.execute(group_id="123")

    assert results["id"] == "projected_sickle"
