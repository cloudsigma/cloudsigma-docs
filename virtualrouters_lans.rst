Virtual Routers Lans
====================

Editing
-------

.. http:put:: /virtualrouters/{uuid}/

    Edits a virtual router LAN Interface. Note that only ``name`` and ``order``
    fields can be changed, and all other changes to the definition of a
    LAN Interface will be ignored.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_lans_safe_update
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_lans_safe_update
        :language: javascript


Configure DHCP
------------------------

.. http:post:: /lans/{uuid}/action/?do=configure_dhcp

    Configures the DHCP service for a Virtual Router LAN Interface.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_lans_configure_dhcp
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_lans_configure_dhcp
        :language: javascript

.. _lans_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_lans_schema
    :language: javascript
