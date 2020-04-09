class Auth:
    """Wraper for authentication implemented by the FiveTranAPI

    Args:
        api_key (str): API key found here: https://fivetran.com/docs/rest-api/getting-started
        api_secret (str): API secrect found here: https://fivetran.com/docs/rest-api/getting-started
    
    Attributes:
        api_key (str): API key found here: https://fivetran.com/docs/rest-api/getting-started
        api_secret (str): API secrect found here: https://fivetran.com/docs/rest-api/getting-started        
    """

    def __init__(self, api_key, api_secret):
        self._api_key = api_key
        self._api_secret = api_secret

    @property
    def api_key(self):
        return self._api_key

    @property
    def api_secret(self):
        return self._api_secret
