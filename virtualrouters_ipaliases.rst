IP Aliases
==========

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


List single IP alias
--------------------

.. http:get:: /ipaliases/{ipalias_uuid}/

Gets information on an IP Alias identified by `ipalias_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/vrouters/request_ipaliases_get
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_ipaliases_get
    :language: javascript

Creating
--------

.. http:post:: /ipaliases/

Creates a new IP Alias.

:statuscode 201: object created

**Example request**:

.. literalinclude:: dumps/vrouters/request_ipaliases_create
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_ipaliases_create
    :language: javascript

Deleting
--------

.. http:delete:: /ipaliases/{ipalias_uuid}/

Deletes a single IP Alias identified by `ipalias_uuid`.

:statuscode 204: No content, object deletion started.

**Example request**:

.. literalinclude:: dumps/vrouters/request_ipaliases_delete
    :language: http

**Example response**:

.. literalinclude:: dumps/vrouters/response_ipaliases_delete
    :language: javascript

.. _ipaliases_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_ipaliases_schema
    :language: javascript
