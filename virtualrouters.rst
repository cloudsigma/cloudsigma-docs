Virtual Routers
===============

CloudSigma Virtual Routers provide routing, firewall, NAT and VPN services for your CloudSigma
networks. Each router runs on a dedicated OPNsense appliance. Configure it through the CloudSigma
portal or API.

This guide describes the current production service. Availability and resource limits depend on the
location and your active subscription.

Before you begin
----------------

You need an account with Virtual Routers enabled, an active router subscription, at least one
assigned public IPv4 address and a subscribed private VLAN. Attach the servers you want to route to
that VLAN. Each LAN uses a distinct VLAN. Do not run competing DHCP servers on the same VLAN.

Examples use documentation addresses and illustrative UUIDs. Replace them with your own assigned
addresses and resource identifiers. The example router type is ``basic``; use the type provided for
your subscription.

Quick start in the portal
-------------------------

1. Sign in to the CloudSigma portal for your location and open **Virtual Routers**.
2. Create a router using the available subscription. Enter a name and select its public address.
3. Configure **LAN 1**: choose your VLAN and enter a gateway address, for example
   ``192.168.10.1/24``.
4. If required, enable DHCP with a pool such as ``192.168.10.100`` to ``192.168.10.199``. Enable NAT
   if LAN clients should access the Internet through the router.
5. Save the definition. Start the router if it is not already starting. Wait until it is started and
   its configuration has finished applying.
6. Connect a server on the VLAN. Obtain a DHCP lease, or assign a non-conflicting address and use
   the router's LAN address as its gateway.
7. Check the server's gateway, DNS resolution and the network traffic you intend to allow.

For later changes, open the router's **Upstream**, **LAN**, **Firewall**, **NAT**, **VPN** or
**Routing** section as appropriate. Save, wait for sync, then refresh the browser page to verify
persistence. Advanced API operations below do not imply a corresponding portal editor.

.. code:: text

   Internet
      |
   Public WAN address
      |
   CloudSigma Virtual Router
      |
   LAN 1 gateway: 192.168.10.1/24
      |
   Private VLAN
      +-- Application server: 192.168.10.10
      +-- DHCP clients: 192.168.10.100-199

API endpoint and authentication
-------------------------------

Use the API endpoint for your :doc:`location <locations>`, followed by
``/api/2.0/virtual_routers/``, and normal CloudSigma
`authentication <general.html#authentication>`__.

.. code:: bash

   export API_URL='https://<location-api-host>/api/2.0'
   export CS_USER='<your-account-email>'
   export VR_UUID='<router-uuid>'

The curl examples use ``--user "$CS_USER"``, which prompts for your password. Use
``Accept: application/json`` and, for JSON writes, ``Content-Type: application/json``. Keep trailing
slashes. Use your CloudSigma account, not appliance-administrator credentials.

Allowed HTTP methods
--------------------

+--------+-------------------------------------------------+--------------------------------------------+
| Method | Resource                                        | Purpose                                    |
+========+=================================================+============================================+
| GET    | ``/virtual_routers/``                           | List accessible routers                    |
+--------+-------------------------------------------------+--------------------------------------------+
| GET    | ``/virtual_routers/detail/``                    | Detailed collection                        |
+--------+-------------------------------------------------+--------------------------------------------+
| GET    | ``/virtual_routers/{uuid}/``                    | Read one router                            |
+--------+-------------------------------------------------+--------------------------------------------+
| POST   | ``/virtual_routers/``                           | Create a router                            |
+--------+-------------------------------------------------+--------------------------------------------+
| PUT    | ``/virtual_routers/{uuid}/``                    | Save its complete desired definition       |
+--------+-------------------------------------------------+--------------------------------------------+
| DELETE | ``/virtual_routers/{uuid}/``                    | Delete a stopped router                    |
+--------+-------------------------------------------------+--------------------------------------------+
| POST   | ``/virtual_routers/{uuid}/action/?do={action}`` | Start, stop or a supported scoped          |
|        |                                                 | configuration action                       |
+--------+-------------------------------------------------+--------------------------------------------+
| GET    | ``/virtual_routers/schema/``                    | Resource field metadata                    |
+--------+-------------------------------------------------+--------------------------------------------+

All paths are relative to your location's ``/api/2.0`` base.

Listing
-------

.. code:: bash

   curl --fail-with-body --silent --show-error --user "$CS_USER" \
     -H 'Accept: application/json' "$API_URL/virtual_routers/"

The collection response contains ``meta`` and ``objects``. Follow the normal pagination metadata for
additional pages.

Detailed listing
----------------

.. code:: bash

   curl --fail-with-body --silent --show-error --user "$CS_USER" \
     -H 'Accept: application/json' "$API_URL/virtual_routers/detail/"

List single virtual router
--------------------------

.. code:: bash

   curl --fail-with-body --silent --show-error --user "$CS_USER" \
     -H 'Accept: application/json' "$API_URL/virtual_routers/$VR_UUID/"

Read ``configuration`` for the saved definition. Read lifecycle and configuration status separately:
a started appliance can still have a pending or failed configuration.

Creating
--------

``POST /virtual_routers/`` accepts a complete ``configuration``. Replace the example VLAN UUID and
public address with your subscribed resources. Omit UUIDs for new child objects; the service assigns
them.

Minimal working configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/virtualrouters/create-vr.json
   :language: json

:download:`Download JSON example <examples/virtualrouters/create-vr.json>`

Save this JSON as ``create-vr.json`` and submit:

.. code:: bash

   curl --fail-with-body --silent --show-error --user "$CS_USER" \
     -H 'Accept: application/json' -H 'Content-Type: application/json' \
     -X POST --data-binary @create-vr.json "$API_URL/virtual_routers/"

A successful create normally returns ``201 Created``. The create response is collection-shaped: read
the new router UUID from ``objects[0].uuid``.

Creation, startup and configuration application are asynchronous. If the router is created but not
starting, use Start. Do not create another router because boot takes time.

Editing
-------

``PUT /virtual_routers/{uuid}/`` saves the desired definition. Supported network and service
settings can be changed while running; updates are not restricted to the name.

1. GET the latest router.
2. Copy ``type`` and ``configuration`` into your request, preserving returned child UUIDs, unchanged
   nested settings and ordering.
3. Make the intended changes.
4. Include the current ``desired_configuration_version`` at the top level as a concurrency guard.
5. PUT the complete definition, then GET until it is in sync.

.. code:: bash

   curl --fail-with-body --silent --show-error --user "$CS_USER" \
     -H 'Accept: application/json' -H 'Content-Type: application/json' \
     -X PUT --data-binary @updated-vr.json "$API_URL/virtual_routers/$VR_UUID/"

The optional version guard must be a non-negative JSON integer. ``409 STALE_CONFIG_VERSION`` means
GET the new definition and reapply your intended edits. ``400 INVALID_CONFIG_VERSION`` means the
guard has an invalid type or value. Omitting the guard allows Save without protection against
stale-page overwrites.

Do not PUT an unfiltered GET response. State/status, owner, jobs, registration/configuration status,
applied versions and errors are server-managed. The desired version is accepted only as an update
precondition.

An explicit empty child collection removes its contents. Omitting the independently managed
OpenVPN-user, IPsec-tunnel or address-forwarding collection preserves it; ``[]`` requests removal.
This is not a general PATCH API: preserve the rest of the complete configuration.

Passwords and pre-shared keys are write-only. Omit an unchanged secret on an identity-preserving
update to retain it. Do not replace a redacted secret with an empty string.

Start and stop
--------------

.. code:: bash

   curl --fail-with-body --user "$CS_USER" -H 'Content-Type: application/json' \
     -X POST -d '{}' "$API_URL/virtual_routers/$VR_UUID/action/?do=start"

   curl --fail-with-body --user "$CS_USER" -H 'Content-Type: application/json' \
     -X POST -d '{}' "$API_URL/virtual_routers/$VR_UUID/action/?do=stop"

Accepted actions return ``202 Accepted``. These actions do not accept extra body fields. Stop
interrupts traffic. Wait for it to finish before starting again or deleting. A stopped router
retains its saved configuration.

Configuration status
--------------------

========================================== ============================================
Field                                      Meaning
========================================== ============================================
``state`` and ``status``                   Appliance lifecycle and operation progress
``registration_status``                    Registration for configuration
``desired_configuration_version``          Latest accepted desired configuration
``applied_configuration_version``          Latest confirmed applied configuration
``config_status``                          Configuration synchronization state
``config_error_code`` and ``config_error`` Error information for a failed configuration
``jobs``                                   Related background operations
========================================== ============================================

Before treating a router as configured, require a started router,
``registration_status == "registered"``, ``config_status == "in_sync"`` and equal desired/applied
versions of at least 1. Then test the relevant traffic. Sync does not prove a VPN peer is connected
or that packets reach their destination.

For a rejected Save, inspect the error code and field. If a response is lost or times out, GET the
router and inspect versions/status before another write. An apply failure means the new
configuration is not confirmed; it does not establish that the previous configuration stopped
forwarding. Correct the problem and Save once no earlier operation remains unresolved.

Deleting
--------

Stop the router and wait for it to be stopped, then:

.. code:: bash

   curl --fail-with-body --silent --show-error --user "$CS_USER" \
     -X DELETE "$API_URL/virtual_routers/$VR_UUID/"

Deletion may be accepted with ``202`` or completed with ``204``. Poll the detail resource until it
is absent or returns ``404``.

Deletion removes the router and its service attachments. Public-IP and VLAN subscriptions are not
cancelled automatically. They remain your resources and may continue to incur charges. Cancel
unwanted subscriptions separately through the normal subscription workflow.

.. _virtualrouters_schema:

Schema
------

.. code:: bash

   curl --fail-with-body --silent --show-error --user "$CS_USER" \
     -H 'Accept: application/json' "$API_URL/virtual_routers/schema/"

This endpoint describes top-level resource metadata, not a complete nested JSON Schema. Use the
nested field tables and complete creation example on these pages.

=================== ==============================================
Configuration field Contents
=================== ==============================================
``name``            Router name
``lan_interface``   Ordered LANs, VLANs, DHCP and LAN aliases
``upstream``        Public WAN addresses and OpenVPN service
``firewall``        Enabled state and ordered policies/filters
``nat``             Outbound NAT, port forwards and 1:1 forwarding
``openvpn_users``   Managed remote-access users
``vpn``             IPsec enabled state and tunnels
``routes``          Ordered static routes
=================== ==============================================

Nested objects have a closed field set: unknown keys are rejected. Keep required empty strings,
arrays and inactive flags as shown. Ordered collections use contiguous positive ``order`` values
starting at 1. Preserve issued UUIDs for existing entries and omit them for new entries.

Virtual Router Features
-----------------------

- :doc:`LAN interfaces and DHCP <virtualrouters_lans>`
- :doc:`IP aliases <virtualrouters_ipaliases>`
- :doc:`Upstream and public addresses <virtualrouters_upstream>`
- :doc:`NAT port forwarding <virtualrouters_port_forwarding>`
- :doc:`1:1 address forwarding <virtualrouters_address_forwarding>`
- :doc:`Firewall policies <virtualrouters_firewall_policies>`
- :doc:`Firewall filters <virtualrouters_firewall_filters>`
- :doc:`OpenVPN remote access <virtualrouters_openvpn>`
- :doc:`IPsec VPN tunnels <virtualrouters_vpn_tunnels>`
- :doc:`Static routes <virtualrouters_routes>`

.. toctree::
   :maxdepth: 2
   :hidden:

   virtualrouters_lans
   virtualrouters_ipaliases
   virtualrouters_upstream
   virtualrouters_port_forwarding
   virtualrouters_address_forwarding
   virtualrouters_firewall_policies
   virtualrouters_firewall_filters
   virtualrouters_openvpn
   virtualrouters_vpn_tunnels
   virtualrouters_routes
