Virtual Routers VPN Tunnels
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


List single tunnel
------------------

.. http:get:: /tunnels/{tunnel_uuid}/

Gets detailed information on a VPN tunnel identified by `tunnel_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/vrouters/request_tunnels_get
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_tunnels_get
    :language: javascript


Creating
--------

.. http:post:: /tunnels/

    Creates a new virtual router VPN tunnel.

    :statuscode 201: object created

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_tunnels_create
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_tunnels_create
        :language: javascript


Editing
-------

.. http:put:: /tunnels/{tunnel_uuid}/

    Edits a VPN tunnel.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_tunnels_update
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_tunnels_update
        :language: javascript


Deleting
--------

.. http:delete:: /tunnels/{tunnel_uuid}/

    Deletes a single virtual router VPN tunnel identified by `tunnel_uuid`.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_tunnels_delete
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_tunnels_delete
        :language: javascript


Schema
------

.. literalinclude:: dumps/vrouters/response_tunnels_schema
    :language: javascript
