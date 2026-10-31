IPsec VPN tunnels
=================

IPsec connects your CloudSigma networks to another site. Configure complementary peer identities,
security settings and protected networks at both ends.

Read capabilities
-----------------

``GET /virtual_routers/{uuid}/ipsec/capabilities/`` returns supported native IKE/ESP choices allowed
for this router and subscription.

.. code:: bash

   curl --fail-with-body --user "$CS_USER" -H 'Accept: application/json' \
     "$API_URL/virtual_routers/$VR_UUID/ipsec/capabilities/"

Use offered ``ike_versions``, ``ike_proposals``, ``esp_proposals`` and lifetime defaults. An
unavailable catalogue returns ``503 IPSEC_CAPABILITIES_UNAVAILABLE``.

Creating a policy-based tunnel
------------------------------

Send this body to ``POST /virtual_routers/{uuid}/action/?do=add_ipsec_tunnel``:

.. literalinclude:: examples/virtualrouters/ipsec-tunnel.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/ipsec-tunnel.json>`

Replace addresses and the secret. Local identity must match the primary WAN; remote identity must
match the peer. Each network array contains exactly one network. Names use 3–64 characters beginning
with a letter, followed by letters, digits, dots, underscores or hyphens. Keys are 12–256 characters
without control characters.

.. code:: bash

   curl --fail-with-body --user "$CS_USER" -H 'Content-Type: application/json' \
     -X POST --data-binary @ipsec-tunnel.json \
     "$API_URL/virtual_routers/$VR_UUID/action/?do=add_ipsec_tunnel"

Start actions are ``start`` and ``trap``. A new scoped tunnel without ``security`` uses IKEv2
AES256/SHA256/modp2048 with 28800/3600-second IKE/child lifetimes. Obtain target capabilities before
selecting explicit native security.

Native security
---------------

.. literalinclude:: examples/virtualrouters/ipsec-security.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/ipsec-security.json>`

This is the object shape, not a guaranteed allowed catalogue. Proposal arrays form a negotiation
set, not a guaranteed priority order. Lifetimes are non-negative integer seconds subject to native
validation.

Editing and deleting
--------------------

To edit security or the start action without resubmitting the key, use ``do=edit_ipsec_tunnel``:

.. literalinclude:: examples/virtualrouters/ipsec-edit.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/ipsec-edit.json>`

This preserves the stored key, tunnel identity and sibling configuration. It does not change
peer/selectors/key. The add action can update the same named tunnel for broader edits and requires
the key; omitting security preserves an existing native selection.

Remove one tunnel with ``{"name": "office-link"}`` and ``do=remove_ipsec_tunnel``. Wait for sync
after each action.

Route-based tunnels
-------------------

For a VTI pair, replace the two network arrays in the add request with:

.. literalinclude:: examples/virtualrouters/ipsec-vti-endpoints.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/ipsec-vti-endpoints.json>`

These are distinct host endpoints on one point-to-point subnet. Preserve host bits and reverse the
endpoints at the other router. No extra top-level ``mode`` field is accepted.

Add a route for the remote LAN, such as ``192.168.20.0/24`` via ``10.254.0.2``. Configure the return
route through ``10.254.0.1`` at the peer.

Runtime status
--------------

``GET /virtual_routers/{uuid}/ipsec/status/``

.. code:: bash

   curl --fail-with-body --user "$CS_USER" -H 'Accept: application/json' \
     "$API_URL/virtual_routers/$VR_UUID/ipsec/status/"

========================================= ======================================
Signal                                    Meaning
========================================= ======================================
``configuration_in_sync``                 Desired configuration applied
``ike_connected`` / ``ike_state``         IKE establishment
``esp_installed`` / ``child_sa_state``    Encrypted child SA installation
``counters``                              Packet/byte counts for the current SA
``available``, ``stale``, ``observed_at`` Observation availability and freshness
Tunnel ``state``                          Administrative/runtime state
========================================= ======================================

IKE can be established without an installed ESP child SA. Unavailable/stale observations mean
unknown, not healthy. Counters may reset on rekey and are not lifetime billing totals. This endpoint
has no durable last-change history.

.. _tunnels_schema:

Schema
------

=================== =================================================
Scoped add field    Description
=================== =================================================
``name``            Managed tunnel name
``peer``            Remote public address
``local_identity``  Primary WAN address
``remote_identity`` Peer address
``local_networks``  One protected local network or local VTI endpoint
``remote_networks`` One protected remote network or peer VTI endpoint
``pre_shared_key``  Write-only shared secret
``active``          Optional, defaults to true
``start_action``    Optional ``start`` or ``trap``
``security``        Optional native IKE/ESP settings
=================== =================================================

The full GET representation stores tunnels in ``configuration.vpn.tunnels`` using issued UUIDs,
``tunnel_name``, enabled state, peer, phase settings and optional ``native_security``. Do not insert
scoped add bodies directly into that array. Prefer scoped actions and preserve returned aggregate
fields during unrelated Saves.

Verify the tunnel
-----------------

Wait for sync, inspect IKE and ESP separately, then send real traffic and confirm counters increase
in both directions. For VTI, verify routes and the return path. A saved active flag or established
IKE alone does not prove payload traffic. Security changes can renegotiate and interrupt the tunnel.
