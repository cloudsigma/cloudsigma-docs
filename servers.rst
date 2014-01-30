Servers / VMs
=============

Allowed HTTP methods
--------------------

+--------+--------------------------+
| Method | Description              |
+========+==========================+
| GET    | get / list object/s      |
+--------+--------------------------+
| POST   | create new object/s      |
+--------+--------------------------+
| PUT    | update / modify object/s |
+--------+--------------------------+
| DELETE | delete object/s          |
+--------+--------------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics

.. _server_schema:

Listing
-------

.. http:get:: /servers/

    Gets the list of servers to which the authenticated user has access.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_server_list
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_list
        :language: javascript

Detailed listing
----------------

.. http:get:: /servers/detail/

    Gets the detailed list of servers to which the authenticated user has access.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_server_list_detail
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_list_detail
        :language: javascript

.. _server_create:

Creating
--------

.. http:post:: /servers/

    Creates a new virtual server or multiple servers. The minimial amount of information you need to set is as follows

    :statuscode 201: object created

    **Example request**:

    .. literalinclude:: dumps/request_server_create_minimal
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_create_minimal
        :language: javascript


.. _server_edit:

Editing
-------

.. http:put:: /servers/{uuid}/

    Edits a server. Used also for attaching NIC's and drives to servers. Note that if a server is running, only
    ``name``, ``meta``, and ``tags`` fields can be changed, and all other changes to the definition of a running server
    will be ignored.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_server_edit_minimal
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_edit_minimal
        :language: javascript


.. _attach_drive:

Attach a drive
--------------


.. http:put:: /servers/{uuid}/

    Attaching a drive is just an :ref:`edit server <server_edit>` operation.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_server_attach_drive
       :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_attach_drive
       :language: javascript

Meta
-----

It is possible to add arbitrary key-value data to a server definition. See :doc:`meta` for more information.

Device channel
~~~~~~~~~~~~~~
Device channel is used to specify the controller number and unit number for each attached drive. This is used so
every time you reboot your virtual machine, the drive remains on the same place in your guest OS ( ex: /dev/sdc )
You specify the channel in the following format - {controller}:{unit} with the following limits for ide and virtio
device types:

    * ide - 0:0, 0:1, 1:0, 1:1 ( total of 4 drives, max 2 units per controller, i.e 0-1)
    * virtio - 0:0, ..., 0:5, ..., 1:0, etc ( total of 1024 drives, max 6 units per controller i.e 0-5)

Deleting
--------

Single server
~~~~~~~~~~~~~

.. http:delete:: /servers/{uuid}/

    Deletes a single server.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/request_server_delete
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_delete
        :language: javascript

.. _servers-delete-recursive:

Delete Server together with attached drives (recursive delete)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /servers/{uuid}/?recurse={recurse_option}

It is possible to delete a server together with it's drives (recursive delete). There are three options: delete all
attached drives, delete only disks(non-cdrom drives), or delete only attached cdroms. To recursively delete drives,
supply a ``recurse`` URL parameter with a value as described in the following table:

+----------------+----------------------------------------------------------------+
| Recurse option | Effect                                                         |
+================+================================================================+
| all_drives     | All attached drives regardless of media type will be deleted   |
+----------------+----------------------------------------------------------------+
| disks          | Only attached drives with media type ``disk`` will be deleted  |
+----------------+----------------------------------------------------------------+
| cdroms         | Only attached drives with media type ``cdrom`` will be deleted |
+----------------+----------------------------------------------------------------+

**Example request to delete a server with all attached drives**:

A server is created with a cdrom and disk drives:

.. literalinclude:: dumps/response_server_recurse_del_all_drives_create
    :language: javascript

The following drives are available in the account:

.. literalinclude:: dumps/response_server_recurse_del_all_drives_drives_before
    :language: javascript

The server is recursively deleted with all drives:

.. literalinclude:: dumps/request_server_recurse_del_all_drives_delete
    :language: javascript

After ``DELETE`` of the server the, drives attached to the server are deleted:

.. literalinclude:: dumps/response_server_recurse_del_all_drives_drives_after
    :language: javascript

**Example request to delete a server with attached disk drives and leave CDROMs**:

A server is created with a cdrom and disk drives:

.. literalinclude:: dumps/response_server_recurse_del_all_drives_create
    :language: javascript

The following drives are available in the account:

.. literalinclude:: dumps/response_server_recurse_del_disks_drives_before
    :language: javascript

The server is recursively deleted with all attached drives with media type ``disk``:

.. literalinclude:: dumps/request_server_recurse_del_disks_delete
    :language: javascript

After ``DELETE`` of the server, only drives with media type ``disk`` attached to the server are deleted. CDROMs are
left intact:

.. literalinclude:: dumps/response_server_recurse_del_disks_drives_after
    :language: javascript


.. _server-runtime:

Server Runtime and Server Details
----------------------------------

.. http:get:: /servers/{uuid}/

    Gets detailed information for server identified by `server_uuid`.

    :statuscode 200: no error

    If the server is started the definition includes a `runtime` attribute. The runtime object contains information on,
    when the server was started, and runtime information about the server NICs, such as how much traffic went through
    the interface and what are the dynamic IPs assigned to the NIC. The NIC runtime is also available in the NIC
    definition of the running server.

    **Example request**:

    .. literalinclude:: dumps/request_server_get_running
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_get_running
        :language: javascript

Server Actions
--------------

Start
~~~~~

.. http:post:: /servers/{uuid}/action/?do=start

    Starts a server with specific UUID.

    :statuscode 202: Action accepted, execution is proceeding.

    **Example request**:

    .. literalinclude:: dumps/request_server_start
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_start
        :language: javascript

.. warning::
    Servers have some default network restrictions, applied depending on your user state. Please refer to
    the :ref:`default restrictions <firewall_restrictions>` section the Firewall policies documentation

Stop
~~~~

.. http:post:: /servers/{uuid}/action/?do=stop

    Stops a server with specific UUID.

    :statuscode 202: Action accepted, execution is proceeding.

    **Example request**:

    .. literalinclude:: dumps/request_server_stop
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_stop
        :language: javascript


Start in a separate availability group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to hint the system which servers are preferred to run on separate hardware host.
See :ref:`servers-avoid`.


Open VNC Tunnel
~~~~~~~~~~~~~~~

.. http:post:: /servers/{uuid}/action/?do=open_vnc

    Opens a VNC tunnel to a server with specific UUID.

    :statuscode 202: Action accepted, execution is proceeding.

    .. note::

      VNC URL will be different each time you close/open the tunnel.

    **Example request**:

    .. literalinclude:: dumps/request_server_open_vnc
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_open_vnc
        :language: javascript



Close VNC Tunnel
~~~~~~~~~~~~~~~~

.. http:post:: /servers/{uuid}/action/?do=close_vnc

    Closes a VNC tunnel to a server with specific UUID.

    :statuscode 202: Action accepted, execution is proceeding.

    **Example request**:

    .. literalinclude:: dumps/request_server_close_vnc
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_server_close_vnc
        :language: javascript


Cloning
~~~~~~~

.. http:post:: /servers/{uuid}/action/?do=clone

:statuscode 202: Action accepted, execution is proceeding.

Clones a server. Does cascading clone of server drives, i.e. all disk drives attached to the server are cloned and
attached to the new server. CDROM drives attached to the clone source are attached to the clone.
IPs of the cloned server are set to DHCP. All other properties of the clone are equal to the original.

The optional body can contain a ``name`` attribute, which will be the name of the newly-cloned
server and/or ``random_vnc_password`` boolean attribute which if set will generate a new vnc password for the new
server.

**Example clone source server**:

.. includejson:: dumps/response_server_get_clone_source
    :hide_header: true

**Example clone request**:

.. literalinclude:: dumps/request_server_clone
    :language: javascript

**Example clone response**:

.. literalinclude:: dumps/response_server_clone
    :language: javascript

.. note::

    The name of the cloned drive will be changed using the clone naming strategy set in the profile.
    See :doc:`clone_naming` for more information 

Cloning with Drives on Different Storage (Avoid)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to hint the system which drives are preferred to be on separate physical storage host.
See :ref:`drives-avoid`.
I

Server NIC Configurations
-------------------------

The network interfaces are configured in the "nics" attribute. For more information on configuring network interfaces
check :doc:`network_interfaces` section.

Here is an example of defining a network interface with a dynamically assigned IP (for brevity only the "nics"
attribute of the definitions is shown):

.. includejson:: dumps/request_server_add_private_nic
    :keys: nics

.. includejson:: dumps/response_server_add_private_nic
    :keys: nics

Availability groups
-------------------

It is possible to query which servers share common hardware hosts. See :ref:`server-availability`.

Advanced settings
-----------------
On every server configuration there are a few advanced options you can setup.

.. includejson:: dumps/response_server_create_full
    :hide_header: true
    :accessor: objects.0
    :keys: enable_numa,hv_relaxed,hv_tsc,cpus_instead_of_cores


* ``cpus_instead_of_cores``:
    - Type: true/false
    - Description: selects whether the SMP is exposed as cores of a single CPU or separate CPUs.
      This should be set to ``false`` for Windows, because there are license requirements for multiple CPUs.


* ``enable_numa``:
    - Type: true/false
    - Description: This option exposes the NUMA/CPU topology of the hypervisor to the virtual machine. It
      boosts performance for NUMA aware applications. The option should be set to ``true`` for servers
      with SMP bigger than 6, since this is the number of cores we have per NUMA node on the hypervisor.
      If set to ``true``, ``cpus_instead_of_cores`` should also be set to ``true`` for Linux,
      because some Linux distributions do not support multiple NUMA nodes on multple CPU cores,
      but only on multiple CPUs.

* ``hv_relaxed``
    - Type: true/false
    - Description: Relax constraints on timers. This improves the behavior of VMs running Windows.

* ``hv_tsc``:
    - Type: true/false
    - Description: Enables more precise timers for Windows. This boost performance for timer specific code.

.. warning::
    ``hv_relaxed`` and `hv_tsc` should be set to ``false`` for VMs running Linux

Server State Diagram
--------------------

.. image:: images/ServerStates.png

Schema
------

.. literalinclude:: dumps/response_server_schema
    :language: javascript
