.. _addressforwards_schema:

.. _11-address-forwarding:

1:1 address forwarding
======================

Map an assigned public address to a private host when you need an address-level mapping rather than
a selected port.

Creating
--------

This operation is available through the API. Send this body to
``POST /virtual_routers/{uuid}/action/?do=add_nat_address_forward``:

.. literalinclude:: examples/virtualrouters/address-forward.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/address-forward.json>`

The external address must already be attached to this router. The target must be a usable host in a
LAN subnet. Names use 3–64 characters: a letter followed by letters, digits, dots, underscores or
hyphens.

.. code:: bash

   curl --fail-with-body --user "$CS_USER" -H 'Content-Type: application/json' \
     -X POST --data-binary @address-forward.json \
     "$API_URL/virtual_routers/$VR_UUID/action/?do=add_nat_address_forward"

The action enables NAT/address forwarding. Acceptance is not completion: wait for configuration
sync.

Editing and deleting
--------------------

Submit the same name to update that mapping. Remove it with ``{"name": "web-host"}`` and
``do=remove_nat_address_forward``.

For full-definition updates, edit ``configuration.nat.address_forwarding`` and retain issued UUIDs.
An explicit empty array removes all mappings. Set ``address_forwarding_active`` true when mappings
exist, false when empty. NAT must be enabled while mappings exist.

.. _addressforward_schema:

Aggregate schema
----------------

================= ================================
Field             Description
================= ================================
``uuid``          Server-issued mapping identifier
``name``          Mapping name
``upstream_ipv4`` Assigned public address
``local_ipv4``    Private host address
``order``         Contiguous order from 1
================= ================================

The scoped action uses ``external_address``/``target_address``; aggregate rows use
``upstream_ipv4``/``local_ipv4``. Do not mix these shapes.

Verify the mapping
------------------

Test the expected private service from an independent external client. Check return traffic and the
intended firewall policy. After removal, verify the mapping is gone.
