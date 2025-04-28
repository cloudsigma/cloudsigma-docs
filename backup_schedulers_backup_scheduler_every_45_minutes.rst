Backup Scheduler: Every 45 Minutes
==================================

Overview
--------

This backup scheduler automatically creates backups every 45 minutes.

The retention policy is configured to keep backups for the last **2 days** only.
After this period, older backups are automatically deleted to manage storage usage.

Scheduler Configuration
-----------------------

- **Backup Frequency**: Every 45 minutes
- **Backup Type**: Remote backup
- **Active Days**: Every day (`day_of_week: ["*"]`)
- **Time Window**: All day (no start or end time defined)
- **Repeat Interval**: Every 45 minutes (`repeat.minute: "*/45"`)
- **Retention Policy**: Keep last 2 days
- **Timezone**: Europe/London
- **Remote Location**: ZRH (Zurich)

Snapshot Timeline (1 Year)
--------------------------

- **Backups per hour**: ~1.33
- **Backups per day**: ~32 (calculated as 24 × 60 ÷ 45)
- **Retention Window**: 2 days
- **Total backups retained at any time**: 32 × 2 = **64 backups**

Older backups are automatically deleted once they fall outside the 2-day retention period.

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
          "hour": "",
          "minute": ""
        },
        "hour": "*",
        "minute": "*",
        "month": "*",
        "repeat": {
          "hour": "",
          "minute": "*/45"
        },
        "start_time": {
          "hour": "",
          "minute": ""
        }
      },
      "is_default": false,
      "is_enabled": true,
      "manual_incremental_backup": "",
      "name": "Every 45 minutes",
      "enable_backup_policy_notifications": true,
      "enable_retention_policy_notifications": false,
      "remote_location": "ZRH",
      "retention_policy": {
        "name": "Last 2 days",
        "rules": [
          {
            "period": "days",
            "quantity": 2
          }
        ]
      },
      "tags": [],
      "type": "backup",
      "user_timezone": "Europe/London"
    }
