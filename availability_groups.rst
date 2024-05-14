Availability Grouping and Avoid
===============================

Resources requested by the user are usually allocated to maximize performance. However, this can lead to a situation, where
the user's servers or drives share the same compute or storage host. This may be undesirable if the user attempts to build,
a redundant setup, as in the unlikely event of hardware failure, servers sharing the same field compute host will crash
at the same time, and drives sharing the same failed storage host will become unavailable at the same time.

To improve the robustness of redundant setups, it is possible to hint in the system, which resources are preferred to be
on separated physical hosts. This is achieved through the *Avoid* functionality for starting servers, and for
creating/cloning drives.

To check the grouping of running servers on compute hosts or the grouping of drives on storage hosts, one can use the
corresponding ``availaility_groups`` API calls.


Checking Availability Groups for Drives and Servers
----------------------------------------------------

The ``availability_groups`` call returns which resources are grouped on the same physical host.


.. _server-availability:

Server availability groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /servers/availability_groups/

:statuscode 200: no error

Returns that running servers share the same physical computer host. Returns an array containing arrays.
Each inner array holds the UUIDs of servers that reside on the same physical host. Non-running servers are not in the
array as they are on any host.

.. http:get:: /servers/availability_groups/{uuid}/

:statuscode 200: no error

Queries in which other servers share the same physical host as the given one. Returns an array holding server UUIDs. The
response includes also the UUID of the queried server. If the queried server is not running, the array will be empty.

.. _drive-availability:

Drives availability groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:get:: /drives/availability_groups/

:statuscode 200: no error

Returns that drive share the same physical storage host. Returns an array containing arrays.
Each inner array holds the UUIDs of drives that reside on the same physical host.

.. http:get:: /drives/availability_groups/{uuid}/

:statuscode 200: no error

Queries with other drives share the same physical storage host as the given one. Returns an array holding drives UUIDs.
The response includes also the UUID of the queried drive.

Examples
~~~~~~~~~

**Example request - servers availability**:

.. sourcecode:: http

      GET /2.0/servers/availability_groups/ HTTP/1.1

**Example response - servers availability**:

.. sourcecode:: http

    HTTP/1.0 200 OK
    Content-Type: application/json; charset=utf-8

    [
     [
        "313e73a4-592f-48cf-81c4-a6c079d005a5",
        "e035a488-8587-4a15-ab25-9b7343236bc9"
     ],
     [
        "313e73a4-592f-48cf-81c4-a6c079d005a5",
        "e035a488-8587-4a15-ab25-9b7343236bc9"
     ]
    ]

**Example request - single-server availability**:

.. sourcecode:: http

    GET /2.0/servers/availability_groups/313e73a4-592f-48cf-81c4-a6c079d005a5/ HTTP/1.1

**Example response - single-server availability**:

.. sourcecode:: http

    HTTP/1.0 200 OK
    Content-Type: application/json; charset=utf-8

    [
     "313e73a4-592f-48cf-81c4-a6c079d005a5",
     "e035a488-8587-4a15-ab25-9b7343236bc9"
    ]

General Notes on Avoid Functionality
-------------------------------------

Avoiding functionality is **best effort**. This means that requests containing avoid will succeed even if the avoid can not
be satisfied and the requested resource ends in the same availability group as an avoid resource.

The **order of the avoid argument UUIDs also specifies the order of preference to avoid**. This means that avoid requests
are satisfied from left to right, and if it is not possible to satisfy the full avoid list, only part of the avoid
list will be satisfied and it will consist of UUIDs from the left part of the list. For example, if there are only three
hosts that can satisfy a request, and there are three avoid resources on these hosts, the newly requested resource, will
end up on the same host as the avoid resource which appears last in the list.

Avoiding functionality may incur **performance penalty**. Specifying avoid for drives cloning and servers cloning, as it
also clones attached drives, usually slow down significantly the clone operation, as the drive data has to be moved
over the network between storage hosts.

.. _servers-avoid:

Starting Servers in a Different Availability Group (Start Avoid)
-----------------------------------------------------------------

.. http:post:: /servers/{uuid}/action/?do=start&avoid={<server1_uuid>,<server2_uuid>,...}

:statuscode 202: Action accepted, execution is proceeding.

Starts a server with a specific UUID attempting to run it on a different physical infrastructure host from the other
servers specified in the `avoid` argument which is a single server UUID or a comma-separated list of server UUIDs. This
way the server specified by `uuid` may be run in a distinct availability group from the other listed servers.

Note that it might not always be possible to run a server in a different availability group, therefore the order of the
`avoid` list also signifies the priority of avoiding other servers.

**Example request**:

.. sourcecode:: http

    POST /2.0/servers/2767d839-3a9d-4bd5-983b-676d1307438f/action/?do=start&avoid=bb1d5184-ebcc-4f33-867e-db654eb2d17e,dc3dd6d4-9b2d-44e6-bc40-e927950e8b77 HTTP/1.1

.. _drives-avoid:

Creating Drives in a Different Availability Group (Create/Clone Avoid)
------------------------------------------------------------------------

.. http:post:: /drives/{uuid}/action/?do=clone&avoid={<server_or_drive_uuid1>,<server_or_drive_uuid2>,...}

:statuscode 202: Action accepted, execution is proceeding.

.. http:post:: /drives/?avoid={<server_or_drive_uuid1>,<server_or_drive_uuid2>,...}

:statuscode 201: object created

.. http:post:: /servers/{server_uuid}/action/?do=clone&avoid={<server_or_drive_uuid1>,<server_or_drive_uuid2>,...}

:statuscode 202: Action accepted, execution is proceeding.

It is possible to hint at the system in which drives are preferred to be on separate physical storage hosts. Avoid can be
specified on all drive creation operations: create, clone drive, and clone server. The value of the ``avoid`` GET
parameter may contain a single or a comma-separated list of drive or server UUIDs. If a server uuid is in the ``avoid``
parameter, this is interpreted as avoiding all the drives attached to the server.

Note that it might not always create a drive in a different availability group, therefore the order of the
`avoid` list also signifies the priority of avoiding other drives. Since it is not possible to specify the order of
drives attached to a server, if a drive from a server needs to be avoided with high priority, it may be specified in
addition to the server UUID. For example ``avoid={important_to_avoid_drive_uuid},{server_uuid_to_which_drive_is_attached}``.

Recipe for Creating a Redundant Server Backed by Separate Infrastructure
-------------------------------------------------------------------------

The best way to create a clone of a server that does not share hardware with the original is to clone the origin server
with avoiding itself, and to start the clone by avoiding the origin:

.. sourcecode:: http

    POST /2.0/servers/2767d839-3a9d-4bd5-983b-676d1307438f/action/?do=clone&avoid=2767d839-3a9d-4bd5-983b-676d1307438f HTTP/1.1

If the created server uuid is *bb1d5184-ebcc-4f33-867e-db654eb2d17e*:

.. sourcecode:: http

    POST /2.0/servers/bb1d5184-ebcc-4f33-867e-db654eb2d17e/action/?do=start&avoid=2767d839-3a9d-4bd5-983b-676d1307438f HTTP/1.1


