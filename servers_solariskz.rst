Solaris Kernel Zone Servers
===========================

Hypervisor specific notes
-------------------------

Solaris kernel zones require at least one bootable drive to be attached and it will only try to boot from drives that
have a `bootindex` value. Additionally, they do not support booting over the network.

Due to their nature, they do not support different drivers for network interfaces or drives. Additionally, the drive
channel is ignored and the order of drives in the definition is passsed to the guest.


Example
-------

    **Example request**:

    .. literalinclude:: dumps/request_skzserver_create_minimal
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_skzserver_create_minimal
        :language: javascript

