Virtual Routers Firewall Filters
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


List single filter
------------------

.. http:get:: /vrfwfilters/{vrfwfilter_uuid}/

Gets detailed information on a filter identified by `vrfwfilter_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/vrouters/request_vrfwfilter_get
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_vrfwfilter_get
    :language: javascript


Creating
--------

.. http:post:: /vrfwfilters/

    Creates a new virtual router firewall filter.

    :statuscode 201: object created

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwfilter_create
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwfilter_create
        :language: javascript


Deleting
--------

.. http:delete:: /vrfwfilters/{vrfwfilter_uuid}/

    Deletes a single virtual router firewall filter.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwfilter_delete
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwfilter_delete
        :language: javascript




Enable Filter Logging
-----------------------

.. http:post:: /vrfwfilters/{vrfwfilter_uuid}/action/?do=enable_logging

    Enables the filter logging on a filter identified by `vrfwfilter_uuid`.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwfilter_enable_logging
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwfilter_enable_logging
        :language: javascript


Disable Filter Logging
------------------------

.. http:post:: /vrfwfilters/{vrfwfilter_uuid}/action/?do=disable_logging

    Disables the filter logging on a filter identified by `vrfwfilter_uuid`.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwfilter_disable_logging
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwfilter_disable_logging
        :language: javascript

.. _vrfwfilters_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_vrfwfilter_schema
    :language: javascript
