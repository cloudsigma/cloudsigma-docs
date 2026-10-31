Static routes
=============

Direct selected destination networks through a reachable next hop.

Reading and creating
--------------------

GET the router, edit ``configuration.routes`` and PUT the complete definition.

.. literalinclude:: examples/virtualrouters/static-routes.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/static-routes.json>`

This example reaches ``10.40.0.0/16`` through another router at ``192.168.10.254`` on LAN 1. That
peer must actually route the destination and provide a return path.

Valid next hops
---------------

Use a reachable peer in a LAN subnet, a configured IPsec VTI peer endpoint, or the assigned WAN
provider gateway where supported. Do not use this router's own LAN address as its next hop.

VTI routes use the peer endpoint, not the public VPN peer address. The WAN default route is managed
automatically; do not duplicate it through the provider gateway. Destinations are IPv4 CIDRs,
including ``/32`` host routes; each destination may appear only once.

Editing and deleting
--------------------

Retain issued route UUIDs on edit. Remove a row to delete it and keep orders contiguous. Update
dependent routes when changing or removing a LAN or tunnel.

.. _routes_schema:

Schema
------

=========== =====================================
Field       Description
=========== =====================================
``uuid``    Server-issued route identifier
``network`` Destination CIDR or host route
``gateway`` Reachable peer address
``inet``    ``{"type": "inet", "label": "inet"}``
``order``   Contiguous order from 1
=========== =====================================

Verify the route
----------------

Wait for sync and send traffic from a real client through the intended path. Confirm forwarding and
return traffic. Repeat after edit/removal. A configuration row does not establish end-to-end
reachability.
