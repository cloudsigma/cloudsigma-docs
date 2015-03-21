Backfilling
===========

Backfilling is a feature which allows you to start servers without guarantee how long they will be running.
The servers defined as "backfilling servers" behave the same as normal servers, except for the following:

* they occupy the free resources currently available in the cloud
* they can be stopped at an arbitrary moment if demand for resources appears by normal servers
* instead of shutdown they can be dynamically downsized in terms of CPU and memory if demand for
  resources appears by normal servers
* they are billed at a separate discount burst rate. No CPU and MEM subscriptions are allowed for the resources
  consumed by the backfilling servers.

In order to use backfilling servers your account must be granted a special permission.

Checking For Available Backfilling Resources
--------------------------------------------

If your account is granted permission to run backfilling server the capabilities API (see :doc:`capabilities`) call
will show additional information regarding backfilling capacity. The `free_resources` object contains three objects,
which show what are the maximum resources that can be use by a single backfilling server.

Here is an example capabilities call from a backfilling user:

.. literalinclude:: dumps/response_account_backfilling_caps
        :language: javascript

The following list summarises the information given by each `free_resources` object:

**total**

    This object shows what are the maximum CPU and memory available for backfilling servers. Note that these
    maximum values may be available on different hosts, so it may not be possible to start a server with this
    parameters.

**most_free_by_cpu**

    This object shows what is the maximum CPU available for a single server, and what is the amount of memory that
    is associated with this CPU. Use this object if you need as much CPU as possible.

**most_free_by_memory**

    This object shows what is the maximum memory available for a single server, and what is the amount of CPU
    associated with it. If you need as much RAM as possible in your server, use this object.

In general the maximum memory and maximum CPU will not be available on a single physical host, so you should use either
`most_free_by_cpu` or `most_free_by_memory` depending on whether your workload needs CPU or memory.

Listing
-------

.. http:get:: /bservers/

Gets the list of backfilling servers to which the authenticated user has access.

:statuscode 200: no error
:statuscode 403: Forbidden - your account doesn't have the backfilling feature enabled


**Example request**:

.. literalinclude:: dumps/request_bserver_list
    :language: http

**Example response**:

.. literalinclude:: dumps/response_bserver_list
    :language: javascript

If your account is not enabled for backfilling, you'll get the following response.

**Example response**:

.. literalinclude:: dumps/response_account_not_backfilling
    :language: javascript


Detailed listing
----------------

.. http:get:: /bservers/detail/

Gets the detailed list of servers to which the authenticated user has access.

:statuscode 200: no error


**Example request**:

.. literalinclude:: dumps/request_bserver_list_detail
    :language: http

**Example response**:

.. literalinclude:: dumps/response_bserver_list_detail
    :language: javascript


Creating
--------

.. http:post:: /bservers/

Creates a new virtual server or multiple servers. The minimial amount of information you need to set is as follows

:statuscode 201: object created

**Example request**:

.. literalinclude:: dumps/request_bserver_create_minimal
    :language: http

**Example response**:

.. literalinclude:: dumps/response_bserver_create_minimal
    :language: javascript


Editing
-------

.. http:put:: /bservers/{uuid}/

Edits a server. Used also for attaching NIC's and drives to servers. Note that if a server is running, only
``name``, ``meta``, and ``tags`` fields can be changed, and all other changes to the definition of a running server
will be ignored.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_bserver_edit_minimal
    :language: http

**Example response**:

.. literalinclude:: dumps/response_bserver_edit_minimal
    :language: javascript

Deleting
--------

.. http:delete:: /bservers/{uuid}/

Deletes a single server.

:statuscode 204: No content, object deletion started.

**Example request**:

.. literalinclude:: dumps/request_bserver_delete
    :language: http

**Example response**:

.. literalinclude:: dumps/response_bserver_delete
    :language: javascript

Server Runtime and Server Details
---------------------------------

.. http:get:: /bservers/{uuid}/

Gets detailed information for server identified by `server_uuid`.

:statuscode 200: no error

If the server is started the definition includes a `runtime` attribute. The runtime object contains information on,
when the server was started, and runtime information about the server NICs, such as how much traffic went through
the interface and what are the dynamic IPs assigned to the NIC. The NIC runtime is also available in the NIC
definition of the running server.

Note the `perf_factor` section in the `runtime` attribute - it is specific to backfilling servers and reflects
the ratio with which the CPU and MEM of the server are currently downsized.

**Example request**:

.. literalinclude:: dumps/request_bserver_get_running
    :language: http

**Example response**:

.. literalinclude:: dumps/response_bserver_get_running
    :language: javascript


Server Actions
--------------

Start
~~~~~

.. http:post:: /bservers/{uuid}/action/?do=start

Starts a server with specific UUID.

:statuscode 202: Action accepted, execution is proceeding.

**Example request**:

.. literalinclude:: dumps/request_bserver_start
    :language: http

**Example response**:

.. literalinclude:: dumps/response_bserver_start
    :language: javascript

.. warning::
    Servers have some default network restrictions, applied depending on your user state. Please refer to
    the :ref:`default restrictions <firewall_restrictions>` section the Firewall policies documentation

Stop
~~~~

.. http:post:: /bservers/{uuid}/action/?do=stop

Stops a server with specific UUID. This action is equivalent to pulling the power cord of a physical server. For
more graceful shutdown see :ref:`acpi_shutdown`.

:statuscode 202: Action accepted, execution is proceeding.

**Example request**:

.. literalinclude:: dumps/request_bserver_stop
    :language: http

**Example response**:

.. literalinclude:: dumps/response_bserver_stop
    :language: javascript


Compatibility with normal servers API and operations
----------------------------------------------------

For compatibility and interoperability reasons all the operations supported for normal servers and supported for the
backfilling ones as well. See the :doc:`servers` section for detailed documentation. In this regard backfilling servers
are a subset of all servers in the account. The API described in :doc:`servers` applies for all servers
(including the backfilling ones), but the API decribed in this section applies for backfilling servers only.

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

Schema
------

.. literalinclude:: dumps/response_bserver_schema
    :language: javascript

