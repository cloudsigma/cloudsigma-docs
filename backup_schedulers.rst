Backup Schedulers
=================

Backup schedulers are a set of rules to automate the creation and
deletion of remote snapshots. It is possible to configure a backup scheduler
to periodically create remote snapshots , e.g. daily, weekly or monthly. Also,
it is possible to configure the retention policy to automate the deletion of
the remote snapshots created by the scheduler.

There are three different types of schedulers:

* dr
* migration
* backup

.. note::

    This document is related to backup schedulers only.

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

.. http:get:: /backupschedulers/

    Gets the list of backup schedulers to which the authenticated user has
    access.

    :param fields: A set of field names specifying the returned fields.
    :statuscode 200: no error

    **Example request - default list**:

    .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_backups_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/backupschedulers/response_backup_scheduler_backups_list
        :language: javascript

Listing schedulers by type
--------------------------

.. http:get:: /backupschedulers/?type=scheduler_type

    Gets the list of backups schedulers to which the authenticated user has
    access and are from type specified in the filters.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_backups_list_type
        :language: http


    **Example response**:

    .. literalinclude:: dumps/backupschedulers/response_backup_scheduler_backups_list_type
        :language: javascript


Detailed listing
----------------

.. http:get:: /backupschedulers/detail/

    Gets the detailed list of backup schedulers with additional information to
    which the authenticated user has access.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_backups_list_detail_type
        :language: http


    **Example response**:

    .. literalinclude:: dumps/backupschedulers/response_backup_scheduler_backups_list_detail_type
        :language: javascript

Detailed listing schedulers by type
-----------------------------------

.. http:get:: /backupschedulers/detail/?type=scheduler_type

    Gets the detailed list of backup schedulers to which the authenticated user
    has access and are from type specified in the filters.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_backups_list_detail_type
        :language: http


    **Example response**:

    .. literalinclude:: dumps/backupschedulers/response_backup_scheduler_backups_list_detail_type
        :language: javascript

List single backup scheduler
----------------------------

.. http:get:: /backupschedulers/{backupscheduler_uuid}/

    Gets detailed information on a backup scheduler identified by
    `backupscheduler_uuid`.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_backup_get
        :language: http


    **Example response**:

    .. literalinclude::  dumps/backupschedulers/response_backup_scheduler_backup_get
        :language: javascript

Creating
--------

.. http:post:: /backupschedulers/

     Creates a new backup scheduler.

    :statuscode 201: object created

    **Example request**:

    .. includejson:: dumps/backupschedulers/request_backup_scheduler_create
        :accessor: objects.0

    **Example response**

    .. literalinclude:: dumps/backupschedulers/response_backup_scheduler_create
        :language: javascript

Editing
-------

.. http:put:: /backupschedulers/{backupscheduler_uuid}/

    Edits a backup scheduler identified by `backupscheduler_uuid`.

    :statuscode 200: no errors

    **Example request**:

    .. literalinclude::  dumps/backupschedulers/request_backup_scheduler_backup_update
        :language: http

    **Example response**:

    .. literalinclude:: dumps/backupschedulers/response_backup_scheduler_backup_update
        :language: javascript

Deleting
--------

Single backup scheduler
~~~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /backupschedulers/{uuid}/

    Deletes a single backup scheduler.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_delete
        :language: http


    **Example response**:

    .. literalinclude:: dumps/backupschedulers/response_backup_scheduler_delete
        :language: javascript

Deletes multiple backup schedulers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. http:delete:: /backupschedulers/

   Deletes multiple backup schedulers specified by their UUIDs.

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

Set scheduler to a drive
------------------------

.. http:post:: /drives/{drive_uuid}/action/?do=set_scheduler

    Link a scheduler to a drive identified by `drive_uuid`.

    :statuscode 202: Action accepted, execution is proceeding

    **Example request**:

    .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_set_drive
        :language: javascript

    **Example response**

    .. literalinclude:: dumps/backupschedulers/response_backup_scheduler_set_drive
        :language: javascript

Allowed timezones
-----------------
The following list are the allowed timezone values for the fields
orchestrator_timezone and user_timezone.

   .. literalinclude:: dumps/backupschedulers/backup_scheduler_timezones
         :language: javascript

Examples of backup schedulers and retention policies
----------------------------------------------------

Configure a backup scheduler to create a remote snapshot every 45 minutes and
only keep those remote snapshots that were taken in the past 2 days.

   .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_periodic_example_1
          :language: javascript

Configure a backup scheduler to create a remote snapshot every hour between
20:00 hours to 23:00 hours and only keeps those that were taken in the past 7
days.

   .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_periodic_example_2
          :language: javascript

Configure a weekly backup scheduler to create a remote snapshot every sunday
at 23:00 hours and only keeps those that were taken in the past 4 weeks.

   .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_periodic_example_3
          :language: javascript

Configure a monthly backup scheduler to create a remote snapshot every first
of month at 23:59 hours and only keeps those that were taken in the past 6
months.

   .. literalinclude:: dumps/backupschedulers/request_backup_scheduler_periodic_example_4
          :language: javascript

Schema
------

   .. literalinclude:: dumps/backupschedulers/response_backupscheduler_schema
        :language: javascript

