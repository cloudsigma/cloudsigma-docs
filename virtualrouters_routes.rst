Virtual Routers Routes
================================


Allowed HTTP methods
--------------------

+--------+--------------------------+
| Method | Description              |
+========+==========================+
| GET    | get / list object/s      |
+--------+--------------------------+
| POST   | create new object/s      |
+--------+--------------------------+
| DELETE | delete object/s          |
+--------+--------------------------+


List single route
------------------

.. http:get:: /routes/{route_uuid}/

Gets detailed information on a route identified by `route_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/vrouters/request_routes_get
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_routes_get
    :language: javascript


Creating
--------

.. http:post:: /routes/

    Creates a new virtual router route.

    :statuscode 201: object created

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_routes_create
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_routes_create
        :language: javascript


Deleting
--------

.. http:delete:: /routes/{route_uuid}/

    Deletes a single virtual router route.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_routes_delete
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_routes_delete
        :language: javascript

.. _routes_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_routes_schema
    :language: javascript
