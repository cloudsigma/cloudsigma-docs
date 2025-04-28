Backup Scheduler: Every Sunday at 23:00
=======================================

Overview
--------

This backup scheduler is designed to create a local snapshot every Sunday at 23:00 in the Europe/London timezone. It uses a simple
configuration based on the day of the week and time, with no repeated interval.

A retention policy of 4 weeks ensures that only the latest four weekly snapshots are retained. This setup is ideal for low-frequency,
weekly backup requirements such as routine system state or configuration snapshots.

Scheduler Configuration
-----------------------

- **Backups per week**: 1 (every Sunday at 23:00)
- **Retention window**: 4 weeks
- **Total retained snapshots at any time**: 4
- **Older snapshots** are automatically deleted as new ones are created weekly.

API Summary
-----------

**Endpoint:**

::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

    {
      "incremental_backup": {
        "day_of_month": "*",
        "day_of_week": ["sun"],
        "end_time": {
          "hour": "",
          "minute": ""
        },
        "hour": "23",
        "minute": "00",
        "month": "*",
        "repeat": {
          "hour": "",
          "minute": ""
        },
        "start_time": {
          "hour": "",
          "minute": ""
        }
      },
      "is_default": false,
      "is_enabled": true,
      "manual_incremental_backup": "",
      "name": "Every sunday at 23:00",
      "enable_backup_policy_notifications": true,
      "enable_retention_policy_notifications": false,
      "retention_policy": {
        "name": "Last 4 weeks",
        "rules": [
          {
            "period": "weeks",
            "quantity": 4
          }
        ]
      },
      "tags": [],
      "type": "snapshot",
      "user_timezone": "Europe/London"
    }
