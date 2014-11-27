Capabilities
============

Allowed HTTP methods
--------------------

+--------+--------------------------------------------------+
| Method | Description                                      |
+========+==================================================+
| GET    | get the capabilities object                      |
+--------+--------------------------------------------------+

.. note::
    
    See :rfc:`2616#section-9` for more details on HTTP methods semantics



The capabilities API call is used to gather all the basic, sensible limits of the API, to prevent applying static
limits inside the client application.

Bare in mind, that these capabilities are dynamic - they are based on the cloud usage, location, etc. For example
a location might not support **lssd**, but support **magnetic** disk option, or vise versa. If a feature is not supported or
is disabled, it will disappear from the result of this call. Most entries are obvious limits on the guest or drive properties.

:hosts:
    A list of available host types and their limitations.

    :cpu_per_smp:
        This gives a range of valid cpu values, per smp, for the given host type. For example, for AMD hosts, one CPU must be
        between 1000 and 2500MHz: a guest 2000MHz cpu and 2 smp has 1000MHz per smp and is valid, but a guest with
        8000MHz cpu and 2 smp has a 4000MHz per smp is not.

.. _hypervisors:

:hypervisors:
    A list of hypervisors and which hosts they are available on. More details on the hosts can be found in the in the
    hosts entry.

:drives:
    A list of available drive types and their limitations. The values in max_size and min_size are deprecated and are
    identical to the nested ones in size.

:snapshots:
    Information about the current and maximum number of snapshots allowed for the account. These are global, not per drive.

:servers:
    This entry is deprecated and contains the same values for amd hosts.

.. http:get:: /capabilities/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_capabilities
    :language: http

**Response**:

.. literalinclude:: dumps/response_capabilities
    :language: javascript




