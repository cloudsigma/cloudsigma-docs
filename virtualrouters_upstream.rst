Virtual Routers Upstream
========================

Configure VPN
------------------------

.. http:post:: /upstream/{uuid}/action/?do=configure_vpn

    Configures the VPN service for a Virtual Router Upstream. The `vpn_type`
    allowed values are: pptp and ikev2.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_upstream_configure_vpn
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_upstream_configure_vpn
        :language: javascript

.. _upstream_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_upstream_schema
    :language: javascript
