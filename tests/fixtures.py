# standard
import pytest
import os
import json

# local
from fivetran.auth import Auth
from fivetran.client import FiveTranAPI

from tests.settings import FIVETRAN_API_KEY
from tests.settings import FIVETRAN_API_SECRET


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def auth():

    return Auth(api_key=FIVETRAN_API_KEY, api_secret=FIVETRAN_API_SECRET)


@pytest.fixture
def api(auth):
    return FiveTranAPI(auth=auth)


def _load_json(filename):
    with open(f"{CURRENT_DIR}/data/{filename}.json", "r") as f:
        return json.loads(f.read())
