VMWare Servers
==============

VMMware specific notes
~~~~~~~~~~~~~~~~~~~~~~

The VMWare server integration in the CloudSigma API is still in a BETA stage. Only partial functionality is exposed
and the API definition and functionality are subject to changes.

Allowed HTTP methods
--------------------

+--------+--------------------------+
| Method | Description              |
+========+==========================+
| GET    | get / list object/s      |
+--------+--------------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics

Listing
-------

.. http:get:: /vmware_servers/

    Gets the list of servers to which the authenticated user has access.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_vmware_servers_list
    :language: http

    **Example response**:

    .. literalinclude:: dumps/response_vmware_servers_list
    :language: javascript

Schema
------

.. literalinclude:: dumps/response_vmware_servers_schema
    :language: javascript
