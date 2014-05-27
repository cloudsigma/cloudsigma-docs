Firewall Policies
=================

Allowed HTTP methods
--------------------

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics

Listing
-------

.. http:get:: /fwpolicies/

    Gets the list of firewall policies to which the authenticated user has access.

    :param fields: A set of field names specifying the returned fields
    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_fwpolicy_list
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_fwpolicy_list
        :language: javascript


Detailed listing
----------------
.. http:get:: /fwpolicies/detail/

    Gets a detailed list of firewall policies to which the authenticated user has access.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_fwpolicy_list_detail
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_fwpolicy_list_detail
        :language: javascript


Create
------
.. http:post:: /fwpolicies/

    Creates a firewall policy.

    :statuscode 201: no error

    **Example request - minimal**:

    .. literalinclude:: dumps/request_fwpolicy_create_minimal
        :language: javascript

    **Example response - minimal**:

    .. literalinclude:: dumps/response_fwpolicy_create_minimal
        :language: javascript

    This is the minimal data required to create a policy. It is blank one ( does not contain any rules ),
    but you can use it to attach it to a couple of servers and edit it later to match your needs.

    **Example request - full**:

    .. literalinclude:: dumps/request_fwpolicy_create_full
        :language: javascript

    **Example response - full**:

    .. literalinclude:: dumps/response_fwpolicy_create_full
        :language: javascript

    This is a more useful firewall policy. The rules are applied in the order they are stated.

.. note::
    * The IP and port fields support "!" prefix, which specifies "NOT" ( ex. "!192.168.1.1" ).
    * You can specify port ranges with ":" ( ex. "1:1024" or "!1:1024")
    * The IP fields support subnet definition using the CIDR notation ( ex. "192.168.1.1/24" )

Editing
-------
.. http:put:: /fwpolicies/{uuid}/

    Update an existing firewall policy

    .. warning::
        Changes are applied every 30 seconds to all running servers with nics that have the policy attached.

    :statuscode 200: no error

    **Example policy**:
        .. includejson:: dumps/response_fwpolicy_get
            :hide_header: true

    **Update request**:
        .. literalinclude:: dumps/request_fwpolicy_update
            :language: javascript

    **Update response**:
        .. literalinclude:: dumps/response_fwpolicy_update
            :language: javascript

Delete
------
.. http:delete:: /fwpolicies/{uuid}/

    Delete a firewall policy

    .. warning::
        Only policies attached to servers in status **stopped** can be deleted.

    :statuscode 204: no content, object is deleted

    **Example request**:

    .. includejson:: dumps/request_fwpolicy_delete

    **Example response**:

    .. includejson:: dumps/response_fwpolicy_delete

Attach policy to a server
-------------------------
Attaching a policy is done by specifying the policy *uuid* in the field *firewall_policy* on the server's NIC, using
the :ref:`create <server_create>` or :ref:`edit <server_edit>` server calls

.. includejson:: dumps/request_fwpolicy_server_attach
    :hide_header: true
    :accessor: objects.0

.. warning::
        Firewall policies are only applied when attached to your server's public network interfaces.


.. _firewall_restrictions:

Default restrictions
--------------------
Depending on your account's current state, the following restrictions are applied:

    * Level 0 - for *REGULAR* users:
        Running servers have limits set on originating broadcast and multicast traffic:
            * broadcast - limited to 5 packets/second with burst of 100
            * multicast - limited to 10 packets/second with burst of 100

    * Level 1 - for *TRIAL* users:
        Running servers cannot open communication channels to ports 22, 23, 25, 7777, 43594, 43595 and 25565

    * Level 2 - for *GUEST* and *NEW* users:
        Running servers can only send ICMP requests, request a DHCP IP, query a DNS server and
        send requests to TCP port 80 and 443 ( usually HTTP and HTTPS )

Each restriction level applies all the rules from the previous one - i.e. Level 0 rules are applied to Level 1, etc.
Please contact support if any of these restrictions breaks your workflow.

.. note::
    When converting from one user type to another, restrictions are automatically adjusted - no need to
    powercycle your running servers.


Schema
------

   .. literalinclude:: dumps/response_fwpolicy_schema
        :language: javascript
