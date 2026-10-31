.. _vrfwpolicies_schema:

Firewall policies
=================

Policies contain ordered traffic filters. Each filter identifies an interface, direction, match
conditions and allow/deny action.

Reading and creating
--------------------

GET the router, enable ``configuration.firewall.active`` and edit
``configuration.firewall.policies``. PUT the complete definition.

.. literalinclude:: examples/virtualrouters/firewall-policy.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/firewall-policy.json>`

This fragment applies to an existing router. Replace ``interface_uuid`` with the LAN UUID from GET.
It denies new traffic entering the router on LAN 1 to TCP destination port 25. It is not a complete
security policy or default-deny configuration.

Ordering and direction
----------------------

Policies and filters have separate contiguous orders from 1. Each filter requires ``direction``:
``in`` enters the selected router interface; ``out`` leaves it. Optional policy-level direction does
not replace filter direction.

An allow rule does not make every other packet denied. Define and test the intended deny rules
explicitly.

Editing and deleting
--------------------

Retain issued policy/filter UUIDs on edit. Remove a policy from the array to delete it. To retain a
disabled policy, set it and its filters inactive. To disable the firewall globally, remove its
policies and set ``firewall.active`` false.

.. _vrfwpolicy_schema:

Schema
------

============= ============================================
Field         Description
============= ============================================
``uuid``      Server-issued policy identifier
``active``    Enabled state
``name``      Display name
``order``     Policy position
``direction`` Optional grouping field
``filters``   Ordered filters, each with its own direction
============= ============================================

Verify a policy
---------------

Use a new matching connection, a non-matching control and a check after rule removal. Established
stateful connections can survive a rule change. Configuration sync does not replace packet tests.
