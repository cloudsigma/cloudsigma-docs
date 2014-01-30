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

.. http:get:: /capabilities/

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_capabilities
    :language: javascript

**Response**:

.. literalinclude:: dumps/response_capabilities
    :language: javascript



.. note::

    Bare in mind, that these capabilities are dynamic - they are based on the cloud usage, location, etc. For example
    a location might not support **lssd**, but support **magnetic** disk option, or vise versa. If a feature is not supported or
    is disabled, it will disappear from the result of this call. Most of the limits are straight forward and easy to
    figure out - they match options on servers and drives. There are some exceptions like:

    :cpu_per_smp:
        this means that the cpu, divided by the smp value, if smp > 1, should be in the range between 1000 and 2200 MHz.
        For example a server with 2000MHz cpu and 2 smp has 1000MHz per smp and is within the range, but a server with
        8000MHz cpu and 2 smp has a 4000MHz per smp, which is outside of the allowed range.


