Virtual Routers
================

Allowed HTTP methods
--------------------

+--------+--------------------------+
| Method | Description              |
+========+==========================+
| GET    | get / list object/s      |
+--------+--------------------------+
| POST   | create new object/s      |
+--------+--------------------------+
| PUT    | update / modify object/s |
+--------+--------------------------+
| DELETE | delete object/s          |
+--------+--------------------------+


.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
-------

.. http:get:: /virtualrouters/

    Gets the list of virtual routers to which the authenticated user has access.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_list_one
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_list_one
        :language: javascript

Detailed listing
----------------

.. http:get:: /virtualrouters/detail/

    Gets the detailed list of virtual routers to which the authenticated user has access.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_list_detail_one
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_list_detail_one
        :language: javascript


List single virtual router
--------------------------

.. http:get:: /virtualrouters/{virtualrouter_uuid}/

    Gets detailed information on the virtual router identified by
    `virtualrouter_uuid`.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_get
        :language: http


    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_get
        :language: javascript

Creating
--------

.. http:post:: /virtualrouters/

    Creates a new virtual router. The minimal amount of information you need
    to set is given below.

    :statuscode 201: object created


Minimal virtual router configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_virtualrouter_create_minimal
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_virtualrouter_create_minimal
        :language: javascript

More complex virtual router configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_complex_create
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_complex_create
        :language: javascript

Editing
-------

.. http:put:: /virtualrouters/{uuid}/

    Edits a virtual router. Note that if a virtual router is running, only the field
    ``name`` can be changed, and all other changes to the definition of a
    running virtual router will be ignored.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_safe_update
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_safe_update
        :language: javascript


Deleting
--------

Single virtual router
~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /virtualrouters/{virtualrouter_uuid}/

    Deletes a single virtual router identified by
    `virtualrouter_uuid`.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_delete
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_delete
        :language: javascript



Enable Firewall
-----------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=enable_firewall

    Activates the firewall feature on a virtual router identified by
    `virtualrouter_uuid`.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_enable_firewall
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_enable_firewall
        :language: javascript


Disable Firewall
------------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=disable_firewall

    Deactivates the firewall feature on a virtual router identified by
    `virtualrouter_uuid`. This will disable all the applied filters.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_disable_firewall
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_disable_firewall
        :language: javascript


Enable Firewall logging
-----------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=enable_firewall_logging

    Enables firewall logging for all active filters on a virtual router identified by
    `virtualrouter_uuid`

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_enable_firewall_logging
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_enable_firewall_logging
        :language: javascript


Disable Firewall logging
------------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=disable_firewall_logging

    Disables firewall logging for all the active filters on a virtual router identified by
    `virtualrouter_uuid`

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_disable_firewall_logging
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_disable_firewall_logging
        :language: javascript


Enable NAT
-----------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=enable_nat

    Activates the NAT feature on a virtual router identified by
    `virtualrouter_uuid`

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_enable_nat
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_enable_nat
        :language: javascript


Disable NAT
------------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=disable_nat

    Deactivates the NAT feature on a virtual router identified by
    `virtualrouter_uuid`

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_disable_nat
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_disable_nat
        :language: javascript


Enable VPN
-----------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=enable_vpn

    Activates the VPN feature on a virtual router identified by
    `virtualrouter_uuid`

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_enable_vpn
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_enable_vpn
        :language: javascript


Disable VPN
------------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=disable_vpn

    Deactivates the VPN feature on a virtual router identified by
    `virtualrouter_uuid`

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_disable_vpn
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_disable_vpn
        :language: javascript


Get Log
------------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=get_log

    Get the latest log entries on a virtual router identified by
    `vrfwfilter_uuid`. Valid ``log_name`` values that can be included
    in the query parameters are: system and firewall.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_get_log
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_get_log
        :language: javascript

Get Keys
------------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=get_keys

    Get the keys related to virtual router identified by
    `virtualrouter_uuid`

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_get_keys
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_get_keys
        :language: javascript


Export key
------------------------

.. http:post:: /virtualrouters/{virtualrouter_uuid}/action/?do=export_key

    Export the key identified by `key_uuid` of the virtual router identified by
    `virtualrouter_uuid`

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrouters_export_key
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrouters_export_key
        :language: javascript

.. _virtualrouters_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_vrouters_schema
    :language: javascript


Virtual Router Features
========================

More information about a virtual router's features.

.. toctree::
    :maxdepth: 2

    virtualrouters_lans
    virtualrouters_ipaliases
    virtualrouters_upstream
    virtualrouters_port_forwarding
    virtualrouters_firewall_policies
    virtualrouters_firewall_filters
    virtualrouters_vpn_tunnels
    virtualrouters_routes
