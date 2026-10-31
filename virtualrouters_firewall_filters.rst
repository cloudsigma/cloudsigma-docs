.. _vrfwfilters_schema:

Firewall filters
================

Edit ``configuration.firewall.policies[].filters`` and PUT the complete router definition after a
current GET.

.. _vrfwfilter_schema:

IP and transport-layer schema
-----------------------------

================================ =========================================================
Field                            Description
================================ =========================================================
``uuid``                         Server-issued rule identifier
``active``                       Enabled state; set explicitly
``action``                       ``allow`` or ``deny``
``direction``                    ``in`` or ``out`` relative to the interface
``interface``                    ``WAN``, a selected WAN address, or the returned LAN name
``interface_uuid``               LAN UUID for a LAN rule; omit for WAN
``protocol``                     ``tcp``, ``udp`` or ``all``, lowercase
``src``, ``dst``                 Source/destination IPv4 address or subnet expression
``src_port``, ``dst_port``       Source/destination port expression
``src_addr_op``, ``dst_addr_op`` Corresponding address operand enabled
``src_port_op``, ``dst_port_op`` Corresponding port operand enabled
``nexthop``                      Empty string
``log``                          Rule logging
``order``                        Position within the policy
================================ =========================================================

False operand flags require empty operands and mean no restriction for that operand. Enabled
operands need a valid expression. Port conditions require TCP or UDP; ``all`` cannot carry concrete
port matches.

Ports support single values, ranges and comma-separated combinations such as ``80,443,8000-8010``.
Addresses accept one IPv4 address, one CIDR network, or ``any``. Address
expressions are at most 64 characters; port expressions at most 255. Do not supply hostnames or
invent a policy-routing next hop.

Use the exact returned LAN name and UUID for a LAN rule. For WAN, use ``WAN`` or an assigned address
and omit ``interface_uuid``.

Ethernet-layer filtering
------------------------

Where the appliance supports Ethernet filtering, use ``layer: "l2"`` with MAC/EtherType fields
instead of IP/port fields:

.. literalinclude:: examples/virtualrouters/ethernet-filter.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/ethernet-filter.json>`

Replace the LAN UUID. MAC values are ``any`` or lowercase colon-separated addresses. This example
matches one source MAC carrying IPv4 frames; use ``arp`` to match ARP frames, or ``any`` for all
EtherTypes.

Set ``log`` false. Do not include ``protocol``, address/port operands or ``nexthop`` in an Ethernet
rule. Unsupported appliance capability is rejected.

Editing, deleting and verification
----------------------------------

Retain the rule UUID on edit. Remove the row to delete it and keep orders contiguous. Wait for sync,
then test matching traffic, a non-matching control and recovery after removal. Use new connections
for stateful tests.
