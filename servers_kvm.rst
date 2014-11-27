KVM Servers
===========

Device channel
~~~~~~~~~~~~~~
Device channel is used to specify the controller number and unit number for each attached drive. This is used so
every time you reboot your virtual machine, the drive remains on the same place in your guest OS ( ex: /dev/sdc )
You specify the channel in the following format - {controller}:{unit} with the following limits for ide and virtio
device types:

    * ide - 0:0, 0:1, 1:0, 1:1 ( total of 4 drives, max 2 units per controller, i.e 0-1)
    * virtio - 0:0, ..., 0:5, ..., 1:0, etc ( total of 1024 drives, max 6 units per controller i.e 0-5)

Open VNC Tunnel
~~~~~~~~~~~~~~~

.. http:post:: /servers/{uuid}/action/?do=open_vnc

    Server's console (virtual keyboard, mouse, and display) is exposed to the user through the VNC protocol.
    The ``open_vnc`` call opens a VNC tunnel to the server. The returned object contains a ``vnc_url`` specifying the
    endpoint to which to connect the VNC client. The password for the VNC connection is specified in the
    ``vnc_password`` field on the server definition. Note that the tunnel is not closed until reboot, so if you prefer
    you can close is using the ``close_vnc`` action.

    :statuscode 202: Action accepted, execution is proceeding.

    .. note::

      VNC URL will be different each time you close/open the tunnel.

    **Example request**:

    .. literalinclude:: dumps/request_server_open_vnc
        :language: http

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
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_server_close_vnc
        :language: javascript


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
