Audit logs
==========

.. note::
    
    See :rfc:`2616#section-9` for more details on HTTP methods semantics

General
-------
Audit logs are used to track changes made on your resources, either by you or by other parties, like CloudSigma
staff or people that have permission to access you resources.

Querying is done as follows:

.. http:get:: /logs/

    :statuscode 200: no error

    .. literalinclude:: dumps/request_audit_log_list
        :language: http

    .. literalinclude:: dumps/response_audit_log_list
        :language: javascript


Actions
-------
Actions give information about the operation that created the log. They go in a few categories.

* General actions - related to most resource types like servers, drives and snapshots:
    - **create:** During resource creation
    - **update:** During resource update
    - **delete:** During resource deletion
    - **change_owner:** The ownership of the resource has changed. Currently only CloudSigma staff can
      change ownership of a resource.
    - **clone_src:** Resource is used as a cloning source
    - **clone_dst:** Resource is a cloning destination - the newly cloned drive.

* Drive specific actions - these only relate to drives:
    - **move:** Drive is moved to another physical storage. Only staff members can move drives.
    - **convert_to_library:** Drive is converted to a library drive. Only staff members can convert drives.
    - **converted_from_library:** Drive is converted to a regular drive from a library drive.
      Only staff members can convert drives.
    - **init_upload:** Drive upload is initialized.

* Server specific actions - these only relate to servers:
    - **start_send:** An attempt to start a server
    - **boot:** The result of a start operation.
    - **stop_send:** An attempt to stop a server.
    - **stop:** The result of a stop operation
    - **open_vnc:** Open VNC channel to a server
    - **close_vnc:** Close VNC channel to a server
    - **shutdown_ACPI_send:** An ACPI shutdown request is send to the server.
    - **heal:** Server got healed, because its recorded state did not match the physical infrastructure.
      For example, a server is marked as unavailable, but it is actually running fine.

Errors
------
If the field **success** is marked as **False**, that means that an error occurred during the operation.
The error details are saved in the following fields:

    * **error_type** - States the type of the error
    * **error_point** - Points to cause of the error and is mainly used for validation errors
    * **error_message** - Human readable message associated with the error

Example
-------
The following example will show all the logged information during a server's lifecycle.

First we create a server:

    .. literalinclude:: dumps/request_create_server_for_audit
        :language: http

    .. literalinclude:: dumps/response_create_server_for_audit
        :language: javascript


Upon completion you will see the following log at the top of the audit log list:

    .. literalinclude:: dumps/request_create_server_audit_log
        :language: http

    .. literalinclude:: dumps/response_create_server_audit_log
        :language: javascript

- **action** states that we wanted to create a server
- **details** state the parameters of the create call
- **actor** states the user which executed the operation
- **success** is *true*, so the operation completed successfully.
- **uuid** matches the server's uuid


Then we start the server:

    .. literalinclude:: dumps/request_start_server_for_audit
        :language: http

    .. literalinclude:: dumps/response_start_server_for_audit
        :language: javascript


We check the logs again. We see that the action is **start_send** and **success** is **true**:

    .. literalinclude:: dumps/response_start_server_audit_log
        :language: javascript


If the server is fully booted and operational, its status will change to **running**.
If it failed to boot for some reason, the **error_type**, **error_point** and **error_message** fields will
explain why that happened. In this particular case, we had a successful start, so the audit log looks like this:

    .. literalinclude:: dumps/response_start_server_audit_log_complete
        :language: javascript


The pattern is the same when stopping a server:
    * an audit log with action **stop_send** is saved, representing the status of the request to stop a server.
    * If that succeeded i.e. the request to stop a server is successfully send, you can expect a log with action
      **stop**, representing the status of the stop operation i.e. the server actually stopped.


.. note::
    If you stop a server from inside, only a log entry with **stop** action will be added.
    This way, you can figure out if the server got stopped from the API or not:

        * If there are 2 logs **stop_send** and **stop**, it is stopped via an API request
        * If only **stop** is present ( no **stop_send** ), it means that the server is stopped by other
          means (stopped from inside, crashed, etc).


Schema
------

.. http:get:: /logs/schema/

    .. literalinclude:: dumps/request_audit_log_schema
        :language: http

    .. literalinclude:: dumps/response_audit_log_schema
        :language: javascript
