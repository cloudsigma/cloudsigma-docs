Backup Scheduler: Every Hour (20:00–23:00)
==========================================

Overview
--------

This scheduler is designed to create remote backups every hour, but only during a defined evening window—from 20:00 to 23:00 (8 PM to 11 PM), in the Europe/London timezone.

The retention policy retains backups for the last seven days, ensuring there is a full week of hourly backups within the evening window. Older ones are automatically deleted to save space.

Scheduler Configuration
------------------------

- **Backups per day:** 4 (once every hour between 20:00 and 23:00)
- **Retention window:** 7 days
- **Total retained backups at any time:** 4 × 7 = 28 backups
- **Old backups:** Automatically deleted after 7 days

Snapshot Timeline (1 Year)
-----------
- **Backups per day:** 4 (once every hour between 20:00 and 23:00)
- **Retention window:** 7 days
- **Total retained backups at any time:** 4 × 7 = 28 backups
- Backups older than 7 days are automatically deleted.

API Summary
-----------

**Endpoint:**

::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

    {
      "incremental_backup": {
        "day_of_month": "*",
        "day_of_week": ["*"],
        "end_time": {
          "hour": "23",
          "minute": "00"
        },
        "hour": "*",
        "minute": "*",
        "month": "*",
        "repeat": {
          "hour": "*/1",
          "minute": ""
        },
        "start_time": {
          "hour": "20",
          "minute": "00"
        }
      },
      "is_default": false,
      "is_enabled": true,
      "manual_incremental_backup": "",
      "name": "Every hour",
      "enable_backup_policy_notifications": true,
      "enable_retention_policy_notifications": false,
      "remote_location": "ZRH",
      "retention_policy": {
        "name": "Last 7 days",
        "rules": [
          {
            "period": "days",
            "quantity": 7
          }
        ]
      },
      "tags": [],
      "type": "backup",
      "user_timezone": "Europe/London"
    }
