Server Network Interfaces
==========================

Private and Public Network Interfaces
-------------------------------------

There are three configurations for any one NIC that determines how that NIC behaves. Not all combinations of
configuration are valid:

- ``vlan``: Private Network
- ``ip_v4_conf``: Public IP v4 Network, either static, DHCP, or manually assigned.
- ``ip_v6_conf``: Public IP v6 Network, either static, DHCP, or manually assigned.


==========  ==========  ==========  ======
   Configurations                   Result
----------------------------------  ------
vlan        ip_v4_conf  ip_v6_conf
==========  ==========  ==========  ======
True        True        True        Error: Cannot assign all configs on a NIC
True        True        False       Error: Cannot assign both Private and Public on a NIC
True        False       True        Error: Cannot assign both Private and Public on a NIC
True        False       False       Private network assigned
False       True        True        Both IP v4 and v6 assigned
False       True        False       Only IP v4 assigned
False       False       True        Only IP v6 assigned
False       False       False       No config assigned
==========  ==========  ==========  ======

IP Assignment for Public Interfaces
-----------------------------------

Assignment of IPs on private network interface is up to the user.

For public network interfaces it is possible to configure the way the address is assigned by setting the "conf"
attribute on the ``ip_v4_conf`` or ``ip_v6_conf`` object:

:"dhcp":
    The address is chosen by the system at boot time and assigned through DHCP. On each reboot the VM may get a
    different address. It is an error to specify the IP address for "conf": "dhcp". It is possible get the currently
    assigned dynamic IP of a NIC from the :ref:`server runtime <server-runtime>` of a running server.

    .. includejson:: dumps/request_server_add_dhcp_nic
        :accessor: nics.0
        :keys: ip_v4_conf
        :hide_header: true

:"static":
    The address is chosen and specified by the user. It is assigned to the NIC through DHCP and does not change between
    reboots. The "ip" attribute is mandatory and an IP address can be assigned from the addresses owned by the user.

    .. includejson:: dumps/request_server_change_nic_to_static
         :accessor: nics.0
         :keys: ip_v4_conf
         :hide_header: true

:"manual":
    There is no address specified for the NIC, and the user has to specify the IP address from within the VM. When this
    setting is used, the NIC is allowed to use all IPs for which the user has subscription. This "conf" can be used to
    assign multiple IPs to the same NIC.

    .. includejson:: dumps/request_server_add_manual_nic
        :accessor: nics.0
        :keys: ip_v4_conf
        :hide_header: true


.. note::
    The cloud firewall does not allow traffic to/from IPs which are not owned or not assigned to the VM. The only
    exception is for "manual" conf where the VM is allowed to use any of the IPs which are owned by the user (the user
    has a subscriptions for them).

MAC Addresses
-------------

Newly created NICs have their mac address randomly generated.

.. note::
    All traffic from a MAC address different from the assigned by the system is stopped by the cloud firewall, so users
    should no attempt to change their MACs from within their VM.

In order to update a NIC definition, the definition should have its "mac" attribute filled in. If on "nics" list update
a MAC address disappears from the list, the corresponding NIC is deleted. If a MAC appears in the new list, the
corresponding nic is updated, and if no MAC is specified on a NIC, a new NIC is created. It is an error to attempt to
specify a MAC address which was not previously in the "nics" list.

The order of NICs in the "nics" attribute is important, because it is also the order in which nics are presented to the
VM. It is possible to rearrange NICs by rearranging their orded in the "nics" list.

NIC Models
----------
The "model" attribute specifies the model of the emulated network card. It is recommended to use ``virtio``, whenever
possible (when drivers for virtio are available for the VM operating system).


==========  ====    ==========      ===================================================
Model       Bus     Speed           Description
==========  ====    ==========      ===================================================
e1000       PCI     1Gb/s           Intel Gigabit Ethernet
i82551      ?       ?               ?
i82557b     ?       ?               ?
i82559er    ?       ?               ?
ne2k_pci    PCI     10Mb/s          NE2000
pcnet       ?       ?               ?
rtl8139     ?       10/100Mb/s      Realtek Fast Ethernet
virtio      PCI     1Gb/s           Virtual High Performance Ethernet card (see Virtio)
==========  ====    ==========      ===================================================


Reference: `Wikibooks QEMU/Devices/Network <https://en.wikibooks.org/wiki/QEMU/Devices/Network>`_.


NIC Runtime
------------

When a server is running, the server definition provides information on the currently assigned dynamic IP and the data
traffic made through the NIC. See :ref:`server runtime <server-runtime>` for more details.

Examples
--------

**Example 1 - Private Network assigned to server**:

Definition with all other values default:

.. includejson:: dumps/request_server_add_private_nic

Result:

.. includejson:: dumps/response_server_add_private_nic


**Example 2 - Dynamic IP v4 (DHCP) assigned to NIC with e1000 model**:

Definition with model set to 'e1000':

.. includejson:: dumps/request_server_add_dhcp_nic

Result:

.. includejson:: dumps/response_server_add_dhcp_nic


**Example 3 - Update nics**:

Here is an example of a server with two nics:

.. includejson:: dumps/response_server_get_two_nics

In order to change the IP configuration of the NIC the definitions should have a MAC specified. Notice that in order to
not delete the other NIC both NICs should be put in the request:

.. includejson:: dumps/request_server_change_nic_to_static

The result is:

.. includejson:: dumps/response_server_change_nic_to_static



**Example 4 - Rearrange nics**:

In order to rearrange the NICs of the server definition from *Example 3*, the definition should just be updated
with different order of NICs (NICs are recognized by their MAC):

.. includejson:: dumps/request_server_rearrange_nics

The resulting "nics" are:

.. includejson:: dumps/response_server_rearrange_nics


Notice that the private and public NICs changed order compared to *Example 3*.

**Example 5 - Delete a NIC and change type of the other**:

In order to change a NIC from private to public just remove the "vlan" field and "ip_v4_conf" field. This can also be
combined with deletion of the other interface. Using the NICs from *Example 4* here is how to delete the
public NIC and change the private NIC to public:

.. includejson:: dumps/request_server_del_and_change_nic


.. includejson:: dumps/response_server_del_and_change_nic


Notice that the NIC has the same MAC as the private NIC from *Example 4*, but is configured with DHCP.
