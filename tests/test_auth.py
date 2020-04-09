# third party
import pytest
import os

# local
from fivetran.auth import Auth


@pytest.mark.auth
def test_auth():

    FIVETRAN_API_KEY = os.environ.get("FIVETRAN_API_KEY", "123")
    FIVETRAN_API_SECRET = os.environ.get("FIVETRAN_API_SECRET", "123")

    auth = Auth(api_key=FIVETRAN_API_KEY, api_secret=FIVETRAN_API_SECRET)

    assert auth.api_key == FIVETRAN_API_KEY
    assert auth.api_secret == FIVETRAN_API_SECRET
