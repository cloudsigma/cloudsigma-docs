===================
Asynchronous server
===================

Authentication
--------------

In order to use the asynchronous server, you must first authenticate through the API. This will give you a cookie that is valid for 2 minutes and that has to be used when connecting to the server.

:statuscode 200: no error

**Example request**:

.. sourcecode:: http

  POST /2.0/accounts/action/?do=authenticate_asynchronous HTTP/1.1
  Host: api.cloudsigma.com
  Accept: application/json
  Authorization: Basic dGVzdHVzZXJAY2xvdWRzaWdtYS5jb206dmJudmJu


**Example response**:

.. sourcecode:: http

    HTTP/1.0 200 OK
    Content-Type: application/json; charset=utf-8
    Set-Cookie: async_auth=YTlhZmMwYTctOWYzNi00ZmUzLThlYmUtMGZiOGZlODE0ZmQx|1356012032|f785e3d8083c7666209e54477652de0d057f0791; expires=Thu, 20-Dec-2012 14:02:32 GMT; Max-Age=120; Path=/

    {}


Using this cookie will allow you to connect to the server at /2.0/websocket


Information
-----------

The websocket server sends frames every time one of the following changes:

    * :doc:`subscriptions`
    * :doc:`drives`
    * :doc:`servers`
    * :doc:`networking`
    * :ref:`balance`
    * :doc:`profile`
    * :doc:`jobs`


The frame is a JSON object that contains the following fields:
    * resource_type: A text field that describes the type of resource covered by the notification.
    * resource_uri: The URI of the resource that has changed.

The JSON object might contain a 'object' key, that will contain the full blown resource referenced by the notification, JSON encoded.
