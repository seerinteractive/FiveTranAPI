Getting Started
===============

Head over to `FiveTran's API documentation <https://fivetran.com/docs/getting-started>`_ to obtain an API key and secret.

Installation
============

.. code-block:: bash
    pip3 install -r requirements.txt

Usage
=====

The FiveTran API Client uses attributes to build file paths, similar to `Google's Discovery JSON API <https://developers.google.com/discovery/v1/using>`_.

For example, if we wanted to get all groups, we would do the following:

.. code-block:: python
    #standard
    import os

    #local
    from auth import Auth
    from client import FiveTranAPI

    FIVETRAN_API_KEY = os.environ["FIVETRAN_API_KEY"]
    FIVETRAN_API_SECRET = os.environ["FIVETRAN_API_SECRET"]

    auth = Auth(api_key=FIVETRAN_API_KEY, 
                api_secret=FIVETRAN_API_SECRET)
    
    api = FiveTranAPI(auth=auth)
    result = api.connector.connector_details.execute(connector_id="123")



  api.<category>.<endpoint>.execute(**params)


The categories and endpoints can be registered in the registry.yaml file. The yaml for the above request (category=connector, endpoint=connector_details) is:

..

  connector:
    \- name: connector_details
      path: connectors/{connector_id}
      method: GET
      required: 
        \- connector_id
      dict_path:
        \- data


It's otherwise denoted:

..

  category:
      \- name # name of the endpoint
        path # template found `here <https://fivetran.com/docs/rest-api>`_
        method # HTTP method
        required # any required parameters, e.g connector_id
        dict_path # path to find a value, e.g. -data -items would be used for {'data': {'items': 1}}



Testing
-------

.. code-block:: bash
  FIVETRAN_API_KEY=<api-key> FIVETRAN_API_SECRET=<secret> pytest -m main -s -v


**TODO**
 * add the remaining API endpoints to the registry.yaml file