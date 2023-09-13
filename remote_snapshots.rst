Remote Snapshots
================

Remote snapshots are point-in-time versions of a drive. They can be 
:ref:`cloned <remote_snapshot_cloning>` to a full drive, which
makes it possible to restore an older version of a VM image.

Remote snapshots are our backup solution. If the drive gets deleted and
the remote snapshot is created, the remote snapshot won't disappear.
All remote snapshots (backups) of deleted drives can be found in the
UI -> Storage -> Backups.
But the remote snapshots of active drives can be found at the
Storage -> Drives -> A drive in detailed view -> Backups section.

Remote snapshots are billed based on their occupied size. Since only the 
differences from the current drive image are stored, a
single remote snapshot's size will be equal to the size of the data which has
changed since the remote snapshot has taken. If no data
has changed, the remote snapshot's size will be zero.

Note that remote snapshots are billed as ``backup``, so backup subscriptions
should be bought in order not to burst on remote snapshots usage.

We have remote snapshots in the following locations:
``GVA, ZRH, FRA, CWL, LON, and DUB``

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

    See :rfc:`2616#section-9` for more details on HTTP methods semantics.


Listing
-------

.. http:get:: /remotesnapshots/

    Gets the list of remote snapshots to which the authenticated user has access.

    :param fields: A set of field names specifying the returned fields.
    :statuscode 200: no error

    **Example request - default list**:

    .. literalinclude:: dumps/request_snapshot_list
        :language: http

    **Example response - default list**:

    .. literalinclude:: dumps/response_snapshot_list
        :language: javascript

Detailed listing
----------------

.. http:get:: /remotesnapshots/detail/

    Gets the detailed list of remote snapshots with additional information to which the authenticated user has access.


    :param fields: No parameters.
    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_snapshot_list_detail
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_snapshot_list_detail
        :language: javascript

List single remote snapshot
---------------------------

.. http:get:: /remotesnapshots/{uuid}/

    Gets detailed information on a remote snapshot identified by `snapshot_uuid`.


    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_snapshot_get
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_snapshot_get
        :language: javascript

Creating
--------
Please note that you cannot create more than one remote snapshot of a drive within 30 minutes.
And also you cannot create a second remote snapshot of a drive when the previous one is in ``transferring`` or ``creating`` state.

.. http:post:: /remotesnapshots/

    Creates a new remote snapshot.

    :statuscode 201: object created

    **Example request**:

    Create a remote snapshot

    .. includejson:: dumps/request_snapshot_create
        :accessor: objects.0

    **Example response**

    .. literalinclude:: dumps/response_snapshot_create
        :language: javascript

Editing
-------
Please note that you cannot edit a remote snapshot when the state is ``transferring`` or ``creating``.

.. http:put:: /remotesnapshots/{uuid}/

    Edits a remote snapshot.

    :statuscode 200: no errors

    **Example request**:

    .. literalinclude:: dumps/request_snapshot_edit
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_snapshot_edit
        :language: javascript

Metadata
--------

It is possible to add arbitrary key-value data to a remote snapshot definition.
See
:doc:`meta` for more information.

Deleting
--------
Please note that you cannot delete a remote snapshot when the state is ``transferring`` or ``creating``.

Single Remote snapshot
~~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /remotesnapshots/{uuid}/

    Deletes a single remote snapshot.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/request_snapshot_delete
        :language: http


    **Example response**:
   
    .. literalinclude:: dumps/response_snapshot_delete
        :language: javascript

Multiple remote snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /remotesnapshots/

   Deletes multiple remote snapshots specified by their UUIDs.


      :statuscode 204: No content, object deletion started.

   **Example request**:

   Request body

   .. parsed-literal::

      {"objects":
        [
          {
           "uuid":"b137e217-42b6-4ecf-8575-d72efc2d3dbd",
          },
          {
           "uuid":"e035a488-8587-4a15-ab25-9b7343236bc9",
          },
          {
           "uuid":"feded33c-106f-49fa-a1c4-be5c718ad1b5",
          }
        ]
      }


   **Example response**:
   
   .. sourcecode:: http
   
      HTTP/1.0 204 NO CONTENT
   
.. _remote_snapshot_cloning:

Cloning
-------
Please note that you cannot clone (promote to a full drive) a remote snapshot when the state is ``transferring`` or ``creating``.

.. http:post:: /remotesnapshots/{uuid}/action/?do=clone

    Clones a remote snapshot to a drive. Request body is optional and any or
    all of the key/value pairs can be omitted.

    :statuscode 202: Action accepted, execution is proceeding.

    **Example request**:

    .. literalinclude:: dumps/request_snapshot_clone
        :language: http

    **Example response**:
    The response is actually a drive definition.

    .. literalinclude:: dumps/response_snapshot_clone
        :language: javascript

.. note::

    The name of the cloned drive will be changed using the clone naming strategy set in the profile.
    See :doc:`clone_naming` for more information.

Listing a drive's remote snapshots
----------------------------------

There are 2 ways of getting all the remote snapshots of a drive.

By filtering remote snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can apply a drive filter to remote snapshots.

.. http:get:: /remotesnapshots/{uuid}/?drive={drive_uuid}

    **Example request**:

    .. literalinclude:: dumps/request_snapshot_list_for_drive
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_snapshot_list_for_drive
        :language: javascript

In drive definition
~~~~~~~~~~~~~~~~~~~

In the detailed drive definition there is a "remote_snapshots" field.


.. http:get:: /drives/{drive_uuid}/

    **Example request**:

    .. literalinclude:: dumps/request_snapshots_in_drive_def
        :language: javascript

    **Example response**:

    .. literalinclude:: dumps/response_snapshots_in_drive_def
        :language: javascript

Request schema
~~~~~~~~~~~~~~

   .. parsed-literal::

      {
         "description":"Clone remote snapshot",
         "properties":{
         	"name":{
         		"description": "Name of the cloned remote snapshot",
         	}
         	"media":{
         		"description": "Media of the cloned remote snapshot",
         	}
         	"affinities":{
         		"description": "Affinities of the cloned remote snapshot",
         	}
         }
      }


Schema
------

   .. literalinclude:: dumps/response_snapshot_schema
        :language: javascript

