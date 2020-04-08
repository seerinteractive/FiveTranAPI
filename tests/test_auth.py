# third party
import pytest
import os

# local
from auth import Auth


@pytest.mark.auth
def test_auth():

    FIVETRAN_API_KEY = os.environ["FIVETRAN_API_KEY"]
    FIVETRAN_API_SECRET = os.environ["FIVETRAN_API_SECRET"]

    auth = Auth(api_key=FIVETRAN_API_KEY, api_secret=FIVETRAN_API_SECRET)

    assert auth.api_key == FIVETRAN_API_KEY
    assert auth.api_secret == FIVETRAN_API_SECRET


