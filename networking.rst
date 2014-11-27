==========
Networking
==========

VLAN
----

Allowed HTTP methods
--------------------

+--------+--------------------------------------------------+
| Method | Description                                      |
+========+==================================================+
| GET    | get / list VLANs                                 |
+--------+--------------------------------------------------+
| PUT    | edit VLANs meta                                  |
+--------+--------------------------------------------------+

.. note::
    
    See :rfc:`2616#section-9` for more details on HTTP methods semantics

Listing
--------------------

.. http:get:: /vlans/

Gets the list of VLANs to which the authenticated user has access.

:statuscode 200: no error

    
**Example request**:

.. literalinclude:: dumps/request_vlan_list
    :language: http


**Example response**:

.. literalinclude:: dumps/response_vlan_list
   :language: javascript
        

Detailed listing
--------------------

.. http:get:: /vlans/detail/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_vlan_list_detail
    :language: http


**Example response**:

.. literalinclude:: dumps/response_vlan_list_detail
    :language: javascript

Get single VLAN
--------------------

.. http:get:: /vlans/(uuid:vlan_uuid)/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_vlan_get
    :language: http


**Example response**:

.. literalinclude:: dumps/response_vlan_get
    :language: javascript


Creating
--------------------

New VLANs are created by buying a subscription. See :doc:`subscriptions`.

Editing
--------------------

Currently only VLAN ``meta`` field can be edited.

.. http:put:: /vlans/(uuid:vlan_uuid)/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_vlan_update
    :language: http


**Example response**:

.. literalinclude:: dumps/response_vlan_update
    :language: javascript

Metadata
--------

It is possible to add arbitrary key-value data to a VLAN definition. See :doc:`meta` for more information.

Deleting
--------

Not applicable - The VLAN will disappear when the subscription for it expires.

Attaching To servers
--------------------

A VLAN can be attached to multiple servers. See :doc:`network_interfaces` for more information on using VLANs in NIC
configurations.

IPs
===

The IP object, contains the actual IP in it's ``uuid`` attribute.

The list of IPs includes the IPs that are owned (subscribed to) by the user, and the IPs which are dynamically
assigned to user's servers. The owned IP's are differentiated by dynamically received IPs by the fact that they have a
subscription attached to them (their ``subscription`` attribute is not empty).

The detailed listing includes more information about the IP object, such as netmask, nameservers, and gateway which
will be set on the NIC. The ``netmask`` value is in
`CIDR notation <https://en.wikipedia.org/wiki/CIDR_notation>`_ (*/24* for a *255.255.255.0* mask). The ``nameservers``
attribute contains a list of DNS servers, which will be assigned through DHCP, and the ``gateway`` attribute contains
the IP of the default gateway for the current IP.

Allowed HTTP methods
--------------------

+--------+--------------------------------------------------+
| Method | Description                                      |
+========+==================================================+
| GET    | get / list IPs                                   |
+--------+--------------------------------------------------+
| PUT    | edit IP metadata                                 |
+--------+--------------------------------------------------+

.. note::
    
    See :rfc:`2616#section-9` for more details on HTTP methods semantics

Listing
--------------------

.. http:get:: /ips/

Gets the list of IPSs to which the authenticated user has access.

:statuscode 200: no error


**Example request**:

.. literalinclude:: dumps/request_ip_list
    :language: http


**Example response**:

.. literalinclude:: dumps/response_ip_list
    :language: javascript


Detailed listing
----------------

.. http:get:: /ips/detail/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_ip_list_detail
    :language: http


**Example response**:

.. literalinclude:: dumps/response_ip_list_detail
    :language: javascript


Get single IP
-------------

.. http:get:: /ips/(uuid:ip_uuid)/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_ip_get
    :language: http


**Example response**:

.. literalinclude:: dumps/response_ip_get
    :language: javascript


Creating
--------

New IPs are created by buying a subscription. See :doc:`subscriptions`.

Editing
-------

Currently only IP ``meta`` field can be edited.


.. http:put:: /ips/(uuid:ip_uuid)/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_ip_update
    :language: http


**Example response**:

.. literalinclude:: dumps/response_ip_update
    :language: javascript

Metadata
--------

It is possible to add arbitrary key-value data to an IP definition. See :doc:`meta` for more information.

Deleting
--------
Not applicable - The IP will disappear when the subscription for it expires.

Attaching To servers
--------------------

An IP can be attached to a single server. To check whether IP is currently attached to a server look at the attribute
on the object in the detailed listing or on single object retrieval. If ``server`` is empty, then the IP is not
attached to a server and can be used for ``static`` IP configuration. See :doc:`network_interfaces` for more
information on using IPs in NIC configurations.


Schema
------

.. literalinclude:: dumps/response_vlan_schema
    :language: javascript

