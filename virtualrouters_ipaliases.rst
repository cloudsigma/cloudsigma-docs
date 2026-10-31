IP aliases
==========

Additional LAN addresses and additional WAN addresses use different fields.

Reading and editing
-------------------

GET the router, edit the appropriate array and PUT the complete definition. Aliases are part of that
definition, not standalone resources.

LAN aliases
-----------

Add entries to the selected LAN's ``ip_aliases``:

.. literalinclude:: examples/virtualrouters/lan-aliases.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/lan-aliases.json>`

This is an alias-array fragment. Use valid host addresses and prefixes; do not duplicate an
interface address or use a network/broadcast address. Retain issued alias UUIDs on edit. Remove an
entry to delete it and renumber retained orders.

An alias does not create another VLAN or DHCP pool. Ensure clients and routes use the intended
network.

Public WAN aliases
------------------

Use ``configuration.upstream.ipv4_address``:

.. literalinclude:: examples/virtualrouters/wan-addresses.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/wan-addresses.json>`

The first address is primary; later entries are additional addresses on the same WAN. Select your
own assigned subscribed addresses. Keep ``wan_ip_aliases`` empty. Remove dependent NAT and routing
references before detaching an address. Detachment does not cancel its subscription.

.. _ipaliases_schema:

Schema
------

=============== ======================================
LAN alias field Description
=============== ======================================
``uuid``        Server-issued identifier
``ip_address``  Interface host address and CIDR prefix
``order``       Contiguous order from 1
=============== ======================================

================= ====================================================
WAN address field Description
================= ====================================================
``ip``            Assigned public IPv4 string, not an IP-resource UUID
``order``         First is primary
================= ====================================================

Wait for sync and test traffic addressed to the alias. Additional WAN addresses are not independent
uplinks or automatic WAN failover.
