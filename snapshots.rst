Snapshots
===========

Snapshots are point-in-time versions of a drive. They can be :ref:`cloned <snapshot_cloning>` to a full drive, which
makes it possible to restore an older version of a VM image.

Snapshots are billed based on their occupied size. Since only the difference from the current drive image is stored, a
single snapshot's size will be equal to the size of the data which was changed since the snapshot was taken. If no data
was changed, the snapshot's size will be zero.

Note that snapshots are billed as ``drive``, so drive subscriptions should be bought in order not to burst on snapshots
usage.

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


Listing
-------

.. http:get:: /snapshots/

    Gets the list of snapshot to which the authenticated user has access.

    :param fields: A set of field names specifying the returned fields
    :statuscode 200: no error

    **Example request - default list**:

    .. literalinclude:: dumps/request_snapshot_list
        :language: http

    **Example response - default list**:

    .. literalinclude:: dumps/response_snapshot_list
        :language: javascript

Detailed listing
----------------

.. http:get:: /snapshots/detail/

    Gets the detailed list of snapshots with additional information to which the authenticated user has access.
   
    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_snapshot_list_detail
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_snapshot_list_detail
        :language: javascript

List single snapshot
--------------------

.. http:get:: /snapshots/{uuid}/

    Gets detailed information for snapshot identified by `snapshot_uuid`.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_snapshot_get
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_snapshot_get
        :language: javascript

Creating
--------

.. http:post:: /snapshots/

    Creates a new snapshot.

    :statuscode 201: object created

    **Example request**:

    Create a snapshot

    .. includejson:: dumps/request_snapshot_create
        :accessor: objects.0

    **Example response**

    .. literalinclude:: dumps/response_snapshot_create
        :language: javascript

Editing
-------

.. http:put:: /snapshots/{uuid}/

    Edits a snapshot.

    :statuscode 200: no errors

    **Example request**:

    .. literalinclude:: dumps/request_snapshot_edit
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_snapshot_edit
        :language: javascript

Metadata
--------

It is possible to add arbitrary key-value data to a snapshot definition. See :doc:`meta` for more information.

Deleting
--------

Single snapshot
~~~~~~~~~~~~~~~

.. http:delete:: /snapshots/{uuid}/

    Deletes a single snapshot.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/request_snapshot_delete
        :language: http


    **Example response**:
   
    .. literalinclude:: dumps/response_snapshot_delete
        :language: javascript

Multiple snapshots
~~~~~~~~~~~~~~~~~~

.. http:delete:: /snapshots/

   Deletes multiple snapshots specified by their UUIDs.

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
   
.. _snapshot_cloning:

Cloning
-------

.. http:post:: /snapshots/{uuid}/action/?do=clone

    Clones a snapshot to a drive. Request body is optional and any or all of the key/value
    pairs can be omitted.

    :statuscode 202: Action accepted, execution is proceeding.

    **Example request**:

    .. literalinclude:: dumps/request_snapshot_clone
        :language: http

    **Example response**:
    The response is actually a drive definition

    .. literalinclude:: dumps/response_snapshot_clone
        :language: javascript

.. note::

    The name of the cloned drive will be changed using the clone naming strategy set in the profile.
    See :doc:`clone_naming` for more information 

Listing drive snapshots
-----------------------

There are 2 ways of getting all snapshots of a drive

By filtering snapshots
~~~~~~~~~~~~~~~~~~~~~~

You can apply drive filter to snapshots

.. http:get:: /snapshots/{uuid}/?drive={drive_uuid}

    .. includejson:: dumps/request_snapshot_list_for_drive

    .. includejson:: dumps/response_snapshot_list_for_drive

In drive definition
~~~~~~~~~~~~~~~~~~~

In the detailed drive definition there is "snapshots" field

.. http:get:: /drives/{drive_uuid}/

    .. includejson:: dumps/request_snapshots_in_drive_def

    .. includejson:: dumps/response_snapshots_in_drive_def
        :keys: snapshots

Request schema
~~~~~~~~~~~~~~

   .. parsed-literal::

      {
         "description":"Clone snapshot",
         "properties":{
         	"name":{
         		"description": "Name of the cloned snapshot",
         	}
         	"media":{
         		"description": "Media of the cloned snapshot",
         	}
         	"affinities":{
         		"description": "Affinities of the cloned snapshot",
         	}
         }
      }


Schema
------

   .. literalinclude:: dumps/response_snapshot_schema
        :language: javascript

