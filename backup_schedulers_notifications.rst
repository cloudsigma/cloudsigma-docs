Notification for Backup Schedulers
=========================================

1. Introduction
---------------

When using the :doc:`backup schedulers <backup_schedulers>`, you can receive email notifications when certain actions occur—like when a :doc:`remote snapshot <remote_snapshots>` is created or deleted by the scheduler. This guide explains:

- What types of notifications are supported
- How and when they are triggered
- How to correctly configure your API requests

2. Notification Types
----------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - ``backup_scheduler_creation``
     - Sent when the :doc:`backup schedulers <backup_schedulers>` successfully creates a :doc:`remote snapshot <remote_snapshots>` or :doc:`local snapshot <snapshots>` item.
   * - ``backup_scheduler_deletion``
     - Sent when the :doc:`backup schedulers <backup_schedulers>` deletes a :doc:`remote snapshot <remote_snapshots>` or :doc:`local snapshot <snapshots>`, due to retention policies automated cleanup actions.

3. Default Behavior & Preferences
----------------------------------

- Notifications are delivered via **email**.
- Notification preferences are **enabled by default** for all **new users** with account status ``REGULAR`` or ``INACTIVE``.

.. warning::

   Even with the correct API fields, notifications will not be sent if the user has disabled them in their preferences.

   More information about how to configure them can be found in:

   - :doc:`Notification Preferences <notification_preferences>`
   - :doc:`Notification Contacts <notification_contacts>`

4. Notification Requirements
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Notification Type
     - Required Field in API Payload
   * - ``backup_scheduler_creation``
     - ``enable_backup_policy_notifications: true``
   * - ``backup_scheduler_deletion``
     - ``enable_retention_policy_notifications: true``

.. note::

   ✅ Both fields are set to ``true`` by default when creating :doc:`backup schedulers <backup_schedulers>`.

5. Example Behavior
--------------------

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - API Field Values
     - Notifications Sent
   * - Both flags set to ``false``
     - ❌ None
   * - Only ``enable_backup_policy_notifications = true``
     - ✅ Only creation notifications
   * - Only ``enable_retention_policy_notifications = true``
     - ✅ Only deletion notifications
   * - Both flags set to ``true``
     - ✅ All notifications

6. How to Use This in the API
------------------------------

When creating or updating a :doc:`backup schedulers <backup_schedulers>`, you can control whether notifications are sent by adjusting the enable flags.

Here's an example payload that **disables both notifications**:

.. code-block:: json

   {
     "type": "snapshot",
     "name": "Weekday 3AM Snapshot Policy",
     "is_default": false,
     "is_enabled": true,
     "manual_incremental_backup": "",
     "retention_policy": {
       "name": "Keep 3 Weeks",
       "rules": [
         {
           "period": "weeks",
           "quantity": 3
         }
       ]
     },
     "incremental_backup": {
       "day_of_week": ["mon", "tue", "wed", "thu", "fri"],
       "day_of_month": "*",
       "month": "*",
       "hour": "3",
       "minute": "0",
       "repeat": {
         "hour": "",
         "minute": ""
       },
       "start_time": {
         "hour": 12,
         "minute": 0
       },
       "end_time": {
         "hour": 11,
         "minute": 45
       }
     },
     "enable_backup_policy_notifications": false,
     "enable_retention_policy_notifications": false,
     "user_timezone": "Etc/UTC"
   }
