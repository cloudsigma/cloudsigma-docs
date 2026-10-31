LAN interfaces and DHCP
=======================

A LAN connects the router to a private VLAN. Servers on that VLAN use its router interface address
as their gateway.

Reading and editing
-------------------

GET the router, edit ``configuration.lan_interface`` and PUT the complete router definition.

LAN 1 is required. Additional LANs may be added or removed within your subscription limits and the
production limit of eight LANs. Each uses a distinct subscribed VLAN belonging to your account. Do
not remove LAN 1 or replace it by promoting another LAN.

Retain each existing LAN's UUID; omit it for a new LAN. Orders are contiguous from 1. Subnets must
not overlap. Remove dependent forwarding rules, routes and firewall references consistently when
removing a LAN. Your application servers must be attached to the selected VLAN separately.

Configure DHCP
--------------

.. literalinclude:: examples/virtualrouters/lan.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/lan.json>`

This is one new LAN row, not a full PUT body. Replace its VLAN UUID. For edits, retain the existing
LAN UUID.

The DHCP range must be ordered and entirely inside the LAN subnet. Do not include the network,
broadcast or router address. Keep statically assigned hosts out of the pool. A one-address pool is
allowed.

To disable DHCP, set ``dhcp`` to ``false`` and both pool endpoints to empty strings. Existing
clients can retain leases until renewal or expiry.

.. _lans_schema:

Schema
------

=================== ==============================================
Field               Description
=================== ==============================================
``uuid``            Server-issued LAN identifier, retained on edit
``name``            Display name
``order``           Position, starting at 1
``vlan``            Subscribed VLAN UUID
``ip_address``      Router host address with CIDR prefix
``default_gateway`` Empty; use static routes for next hops
``dhcp``            DHCP enabled state
``dhcp_ip_range``   ``from`` and ``to`` endpoints
``ip_aliases``      Ordered additional interface addresses
=================== ==============================================

Keep other required inactive fields as shown in the complete example.

Verify the change
-----------------

Wait for sync. Request a fresh DHCP lease from a client on the VLAN, check its address, mask,
gateway and resolver, then test DNS and permitted traffic. A retained old lease does not prove the
new DHCP configuration works.
