Backup Scheduler API – Field Reference
======================================

Overview
--------

The :doc:`Backup Scheduler API <backup_schedulers>` allows you to automate the creation and retention
of snapshots or backups. You can configure when backups happen and how long to keep them, helping ensure disaster recovery and data lifecycle policies are respected.


Required Fields
---------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Field
     - Type
     - Description
   * - type
     - string
     - Type of scheduler. Allowed values: "snapshot" or "backup"
   * - name
     - string
     - Descriptive name of the scheduler policy.
   * - is_enabled
     - boolean
     - Enables or disables the policy.
   * - is_default
     - boolean
     - This field sets the DR schedule operational period as Continous(is_default=True) or Restricted(is_default=False).
   * - enable_backup_policy_notifications
     - boolean
     - When set to True, the backup scheduler will trigger backup-related notifications (such as scheduled actions and creation events) if the corresponding notification type is also enabled in the user preferences.
   * - enable_retention_policy_notifications
     - boolean
     - When set to True, the backup scheduler will trigger retention-related  notifications (such as snapshot or backup deletions) if the corresponding  notification type is also enabled in the user preferences.

   * - retention_policy
     - object
     - Rules to automatically delete old backups.
   * - incremental_backup
     - object
     - Defines the time(s) when backups occur.
   * - user_timezone
     - string
     - The timezone used for schedule evaluation (e.g., "Etc/UTC").

Optional Fields
---------------

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Field
     - Type
     - Description
   * - manual_incremental_backup
     - string
     - Comma-separated list of specific times in "HH:MM" format.
   * - initial_backup
     - object
     - Defines an optional one-time backup configuration.

       Used on migration schedules.

       Set the time for the initial full backup.
   * - remote_location
     - string
     - Location where backups will be stored (e.g., "ZRH").
   * - meta
     - dict
     - Optional metadata for custom integrations.
   * - tags
     - list
     - Optional tags for categorization or filtering.

manual_incremental_backup
--------------------------

Use when specific times like "02:00,14:00" are required. Only runs backups at the explicitly listed times. No other intervals will be used.

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Property
     - Description
   * - Format
     - "HH:MM" (24-hour format), comma-separated
   * - Example
     - "02:00,06:00,20:00,22:15"
   * - Can be used in combination with incremental_backup fields
     - ``day_of_week``, ``start_time``, ``end_time``

incremental_backup
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Field
     - Type
     - Description
   * - day_of_week
     - list[string]
     - Weekdays to run backups. Valid values: "mon", "tue", ..., "sun" or "*".
   * - day_of_month
     - string
     - Days of month (e.g., "1,15", or "*" for any day).
   * - month
     - string/list
     - Months (e.g., "1,3,12" or "*", which means every month).
   * - hour
     - string
     - Specific hour(s) to run backups (e.g., "1", "1,13", or "*", if used with repeat).
   * - minute
     - string
     - Specific minute(s) to run backups (e.g., "0", "0,30", or "*", if used with repeat).
   * - repeat
     - dict
     - Specifies repeat interval. E.g., "{"hour": "*/12"}" or "{"minute": "*/15"}".
   * - start_time / end_time
     - object
     - Defines the time range within which scheduled or manual backups can run.

retention_policy.rules
-----------------------------

Each rule defines how long snapshots are retained based on time periods.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Field
     - Type
     - Description
   * - period
     - string
     - Time unit for retention. Allowed values: "days", "weeks", "months".
   * - quantity
     - integer
     - How many units of the specified period to retain (e.g., 2, 4, 12).
   * - time_option
     - integer (optional)
     - Restricts the rule to a specific day:
       - For weeks: Day of the week ("0"=Sunday, "6"=Saturday)
       - For months: Day of the month ("1" to "31")

Example Rules
-------------

.. code-block:: json

   "retention_policy": {
       "name": "SFG Policy",
       "rules": [
           { "period": "days", "quantity": 7 },
           { "period": "weeks", "quantity": 4, "time_option": 1 },
           { "period": "months", "quantity": 12, "time_option": 23 }
       ]
   }
**Notes:**

- Rules are evaluated together, keeping snapshots that match any rule.
- Snapshots outside all rules are deleted automatically.
