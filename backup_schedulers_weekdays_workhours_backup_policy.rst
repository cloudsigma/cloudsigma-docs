Weekdays Workhours Backup Policy
================================

Introduction
------------

This backup scheduler automates the creation of remote snapshots during weekday working hours. It ensures that critical data is consistently protected during active business periods—Monday, Wednesday, and Friday—every 12 hours from 07:00 to 19:00 UTC.

Scheduler Configuration
------------------------

- **Type**: backup (remote snapshot)
- **Days**: Monday, Wednesday, Friday
- **Time Window**: 07:00 to 19:00 UTC
- **Frequency**: Every 12 hours (2 backups per day)
- **Timezone**: Etc/UTC

Retention Policy
----------------

- **Retention Period**: Keep remote snapshots from the last 1 month
- **Retention Rule**: Any backup older than one calendar month will be automatically deleted, ensuring that a rotating monthly window of backups is always retained.

Remote Snapshot Timeline (1 Year)
---------------------------------

- **Backups Per Week**:
  3 days/week × 2 backups/day = 6 backups/week

- **Backups Per Month**:
  Approx. 4.33 weeks/month × 6 = ~26 backups retained at a time

::

  After one year you will always have the most recent ~26 remote snapshots,
  and older ones will be deleted automatically.

The total number of retained remote snapshots does not grow over time—it stays fixed around 26, thanks to the monthly retention rule.

API Summary
-----------

**Endpoint**::

  POST /api/2.0/backupschedulers/

**JSON Payload**

.. code-block:: json

    {
      "type": "backup",
      "name": "Weekdays Workhours Backup Policy",
     "enable_backup_policy_notifications": true,
     "enable_retention_policy_notifications": false,
      "is_default": false,
      "is_enabled": true,
      "manual_incremental_backup": "",
      "retention_policy": {
        "name": "Keep 1 Month",
        "rules": [
          {
            "period": "months",
            "quantity": 1
          }
        ]
      },
      "incremental_backup": {
        "day_of_week": ["mon", "wed", "fri"],
        "day_of_month": "*",
        "month": "*",
        "hour": "",
        "minute": "",
        "repeat": {
          "hour": "*/12",
          "minute": ""
        },
        "start_time": { "hour": 7, "minute": 0 },
        "end_time": { "hour": 19, "minute": 0 }
      },
      "user_timezone": "Etc/UTC"
    }
