NAT Address Forwarding
======================

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


List single address forward
---------------------------

.. http:get:: /addressforwards/{addressforward_uuid}/

Gets information on an address forward identified by `addressforward_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/vrouters/request_addressforward_get
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_addressforward_get
    :language: javascript


Creating
--------

.. http:post:: /addressforwards/

Creates a new address forward.

:statuscode 201: object created

**Example request**:

.. literalinclude:: dumps/vrouters/request_addressforward_create
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_addressforward_create
    :language: javascript

Deleting
--------

.. http:delete:: /addressforwards/{addressforward_uuid}/

Deletes a single address forward identified by `addressforward_uuid`.

:statuscode 204: No content, object deletion started.

**Example request**:

.. literalinclude:: dumps/vrouters/request_addressforward_delete
    :language: http

**Example response**:

.. literalinclude:: dumps/vrouters/response_addressforward_delete
    :language: javascript


.. _addressforwards_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_addressforward_schema
    :language: javascript
