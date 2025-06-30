Backup Schedulers
=================

Backup Schedulers automate the creation and deletion of snapshots for your drives. There are two types of snapshots that can be scheduled:

Local Snapshots: Created and stored within the same infrastructure as the original drive. They are fast to create and useful for short-term recovery.

Remote Snapshots: Stored in a different location (data center), making them ideal for disaster recovery or geographic redundancy.

With a scheduler, you can define when snapshots should be created—daily, weekly, monthly, or at custom intervals (e.g. every 12 hours, or only on weekdays). The scheduler ensures snapshots are taken automatically without user intervention.

Each scheduler also includes a retention policy, which defines how long snapshots are kept before being deleted. For example, you might keep daily snapshots for 7 days or monthly ones for 12 months. This ensures your storage doesn't grow indefinitely and your snapshot history stays clean and manageable.

Schedulers are flexible and can be tailored to your backup and recovery strategy—whether you're looking for frequent local snapshots for fast rollback, or long-term remote backups for compliance and safety.

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

.. literalinclude:: dumps/backupschedulers/request_backup_scheduler_backups_list_detail
    :language: http


**Example response**:

.. literalinclude:: dumps/backupschedulers/response_backup_scheduler_backups_list_detail
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

Deletes multiple backup schedulers specified by their UUID's.

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
The following list are the allowed timezone values for the field user_timezone.

.. literalinclude:: dumps/backupschedulers/backup_scheduler_timezones
     :language: javascript

Field reference
----------------------------------------------------

.. toctree::
    :maxdepth: 1

    backup_schedulers_field_reference

Examples of backup schedulers and retention policies
----------------------------------------------------

.. toctree::
    :maxdepth: 1

    backup_schedulers_backup_scheduler_every_45_minutes
    backup_schedulers_snapshot_every_12_hours_keep_last_2_days
    backup_schedulers_every_sunday_23_00
    backup_schedulers_every_first_of_month_2359
    backup_schedulers_backup_scheduler_every_hour_20_00_23_00
    backup_schedulers_snapshot_policy_defined_hours_backups_keep_1_month
    backup_schedulers_weekdays_3am_snapshot_policy
    backup_schedulers_weekdays_workhours_backup_policy
    backup_schedulers_bi_monthly_snapshot_policy
    backup_schedulers_backup_policy_1st_of_month
    backup_schedulers_sfg_retention_strategy

Notifications
------

When using the :doc:`backup schedulers <backup_schedulers>`, you can receive email notifications when certain actions occur—like when a :doc:`remote snapshot <remote_snapshots>` is created or deleted by the scheduler.

.. toctree::
    :maxdepth: 1

    backup_schedulers_notifications

Schema
------

.. literalinclude:: dumps/backupschedulers/response_backupscheduler_schema
    :language: javascript
