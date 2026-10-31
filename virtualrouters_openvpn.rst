OpenVPN remote access
=====================

Remote clients can securely connect to the router and permitted private networks.

Configure the service
---------------------

GET the router and replace ``configuration.upstream.vpn`` with:

.. literalinclude:: examples/virtualrouters/openvpn-service.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/openvpn-service.json>`

Choose a client network that does not overlap LANs or remote routed networks. PUT the complete
definition and wait for sync. NAT and firewall settings determine permitted LAN and Internet access.

Use the portal OpenVPN controls where exposed. The API operations below provide explicit user and
profile management.

Add or update a user
--------------------

``POST /virtual_routers/{uuid}/action/?do=add_openvpn_user``

.. literalinclude:: examples/virtualrouters/openvpn-user.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/openvpn-user.json>`

Usernames are 3–64 characters: a letter followed by letters, digits, dots, underscores or hyphens.
Passwords are 12–256 characters and write-only. Replace the placeholder with a unique secret.
Reusing a managed username updates that user's password while retaining identity.

.. code:: bash

   curl --fail-with-body --user "$CS_USER" -H 'Content-Type: application/json' \
     -X POST --data-binary @openvpn-user.json \
     "$API_URL/virtual_routers/$VR_UUID/action/?do=add_openvpn_user"

To remove a user, send ``{"username": "alice"}`` with ``do=remove_openvpn_user``. Wait for
configuration sync.

Download a client profile
-------------------------

``GET /virtual_routers/{uuid}/openvpn/profile/``

.. code:: bash

   curl --fail-with-body --user "$CS_USER" \
     "$API_URL/virtual_routers/$VR_UUID/openvpn/profile/" \
     --output openvpn-client.ovpn

A successful response is ``200 application/x-openvpn-profile`` with an attachment filename. Import
it into an OpenVPN client and authenticate with your managed VPN user.

The download is router-scoped, not a per-user URL. Only the owning account may export it. The router
must be started, in sync with matching desired/applied versions of at least 1, and OpenVPN must be
enabled. Keep the profile private.

=================================== ========================================
Result                              Next action
=================================== ========================================
``409 VR_NOT_READY``                Start the router and wait for sync
``409 OPENVPN_NOT_ENABLED``         Enable OpenVPN and wait for sync
``503 OPENVPN_PROFILE_UNAVAILABLE`` Retry this read-only download later
``401`` or ``404``                  Check authentication, ownership and UUID
=================================== ========================================

Check the HTTP result before importing: a JSON error is not a client profile.

Disable the service
-------------------

Set ``upstream.vpn`` to ``{"active": false}`` in a full Save. This does not itself delete retained
users. Remove users explicitly with the action or an empty ``openvpn_users`` array.

Schema
------

============================ ===============================================================
Field                        Description
============================ ===============================================================
``upstream.vpn.active``      Service enabled state
``upstream.vpn.vpn_type``    ``openvpn`` when enabled
``upstream.vpn.vpn_network`` Non-overlapping client network
``openvpn_users[]``          Issued UUID, username and order; password only on create/change
============================ ===============================================================

Preserve user UUIDs and omit unchanged passwords during unrelated full Saves.

Verify remote access
--------------------

Connect a real client, check its VPN address and reach an intended LAN service. Test Internet access
separately if required. Reaching another site requires routes/selectors and a return path for the
client network there.
