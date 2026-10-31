Upstream and public addresses
=============================

The upstream provides Internet connectivity and public addresses for VPN and inbound NAT.

Reading and editing
-------------------

GET the router, edit ``configuration.upstream`` and PUT the complete definition. Use
``wan_type: "internet"`` and ``internet_protocol: "ipv4"``.

Public addresses
----------------

.. literalinclude:: examples/virtualrouters/upstream-addresses.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/upstream-addresses.json>`

This is an upstream fragment. Replace documentation addresses with your own subscribed allocations.
Use address strings, not resource UUIDs. The first ordered address is primary; later entries share
the same WAN interface.

Keep the required ``ip_config`` object from the complete creation example. It is not a way to claim
arbitrary public addresses; the location supplies provider-side WAN settings.

Add or remove an address
------------------------

1. GET the latest definition and version.
2. Update the ordered ``ipv4_address`` array.
3. Update dependent NAT rules and other references in the same coherent definition.
4. Save with the version guard and wait for sync.
5. Test inbound traffic and its return path from an external client.

Removing an address releases its attachment, not its subscription. Changing the primary address can
affect VPN identities and external clients.

OpenVPN settings
----------------

``upstream.vpn`` controls remote access. Use ``{"active": false}`` when disabled. See :doc:`OpenVPN
remote access <virtualrouters_openvpn>` for enablement, users and profiles.

.. _upstream_schema:

Schema
------

===================== =============================================
Field                 Description
===================== =============================================
``wan_type``          ``internet``
``internet_protocol`` ``ipv4``
``ipv4_address``      Ordered selected public addresses
``wan_ip_aliases``    Empty array; use ``ipv4_address``
``ip_config``         Required WAN object from the complete example
``vpn``               OpenVPN service settings
===================== =============================================

Keep other required inactive fields unchanged.
