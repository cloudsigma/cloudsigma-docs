NAT Port Forwarding
===================

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

List single port forward
------------------------

.. http:get:: /portforwards/{portforward_uuid}/

Gets detailed information on a port forward identified by `portforward_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/vrouters/request_portforward_get
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_portforward_get
    :language: javascript

Creating
--------

.. http:post:: /portforwards/

Creates a new port forward.

:statuscode 201: object created

**Example request**:

.. literalinclude:: dumps/vrouters/request_portforward_create
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_portforward_create
    :language: javascript

Deleting
--------

.. http:delete:: /portforwards/{portforward_uuid}/

Deletes a single port forward identified by `portforward_uuid`.

:statuscode 204: No content, object deletion started.

**Example request**:

.. literalinclude:: dumps/vrouters/request_portforward_delete
    :language: http

**Example response**:

.. literalinclude:: dumps/vrouters/response_portforward_delete
    :language: javascript

.. _portforwards_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_portforward_schema
    :language: javascript
