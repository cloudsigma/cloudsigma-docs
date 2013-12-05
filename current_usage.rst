=============
Current Usage
=============

Allowed HTTP methods
--------------------

+--------+--------------------------------------------------+
| Method | Description                                      |
+========+==================================================+
| GET    | get / list object/s                              |
+--------+--------------------------------------------------+

.. note::
    
    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
-------

.. http:get:: /currentusage/

    Gets the current usage of the authenticated user has access.

    :param context: another account whose drives should be listed
    :statuscode 200: no error

   
    **Example request**:

    .. sourcecode:: http

      GET /2.0/currentusage/ HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json
      Authorization: Basic dGVzdHVzZXJAY2xvdWRzaWdtYS5jb206dmJudmJu


    **Example response**:

    .. sourcecode:: http

        HTTP/1.0 200 OK
        Content-Type: application/json; charset=utf-8

        {
            "balance": {
                "balance": "9899.16666666666666666667",
                "currency": "CHF"
            },
            "usage": {
                "cpu": {
                    "burst": 0,
                    "subscribed": 0,
                    "using": 0
                },
                "dssd": {
                    "burst": 0,
                    "subscribed": 0,
                    "using": 0
                },
                "ip": {
                    "burst": 0,
                    "subscribed": 0,
                    "using": 0
                },
                "mem": {
                    "burst": 0,
                    "subscribed": 0,
                    "using": 0
                },
                "ssd": {
                    "burst": 0,
                    "subscribed": 0,
                    "using": 0
                },
                "vlan": {
                    "burst": 0,
                    "subscribed": 0,
                    "using": 0
                }
            }
        }

Request schema
~~~~~~~~~~~~~~

    None.

Response schema
~~~~~~~~~~~~~~~

    .. parsed-literal::
    
        {
            "allowed_detail_http_methods": [
                "get"
            ],
            "allowed_list_http_methods": [
                "get"
            ],
            "default_format": "application/json",
            "default_limit": 20,
            "fields": {
                "balance": {
                    "default": "No default provided.",
                    "help_text": "A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}",
                    "readonly": false,
                    "required": true,
                    "type": "dict"
                },
                "usage": {
                    "default": "No default provided.",
                    "help_text": "A dictionary of data. Ex: {'price': 26.73, 'name': 'Daniel'}",
                    "readonly": false,
                    "required": true,
                    "type": "dict"
                }
            }
        }
