.. _portforwards_schema:

NAT port forwarding
===================

Publish a private service through a selected public address and port.

.. code:: text

   Internet client -> 203.0.113.10:8443/TCP
                                 |
                            Virtual Router
                                 |
                         192.168.10.10:443/TCP

Reading and creating
--------------------

GET the router and edit ``configuration.nat.port_forwarding``. Enable ``nat.active`` and PUT the
complete definition.

.. literalinclude:: examples/virtualrouters/nat-port-forwarding.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/nat-port-forwarding.json>`

This is the NAT section to merge into a full definition. The listener must use an address assigned
to this router. The private target must be a usable host in one of its LAN subnets, with a working
return route.

Enabled NAT also supplies outbound translation for eligible LAN traffic. This is not an arbitrary
manual source-NAT editor.

Editing and deleting
--------------------

Retain the rule UUID on edit. Remove it from the array to delete it, then renumber retained rules.
Remove all forwarding rules and disable address forwarding before disabling NAT.

.. _portforward_schema:

Schema
------

=================== =============================
Field               Description
=================== =============================
``uuid``            Server-issued rule identifier
``forwarding_host`` Public listener address
``forwarding_port`` Public listener port, 1–65535
``mapped_host``     Private target address
``mapped_port``     Private target port, 1–65535
``protocol``        ``TCP`` or ``UDP``, uppercase
``order``           Contiguous order from 1
=================== =============================

Public ``forwarding_*`` and private ``mapped_*`` are not interchangeable.

Verify the rule
---------------

Wait for sync. Connect from an independent Internet client to the public listener and verify the
expected private service. Test a non-forwarded port too. A same-LAN test does not establish inbound
Internet forwarding.
