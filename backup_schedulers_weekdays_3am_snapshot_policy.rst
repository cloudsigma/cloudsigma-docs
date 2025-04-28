Weekdays 3AM Snapshot Policy
============================

Introduction
------------

This snapshot policy is designed to create automatic local snapshots of your drive every weekday at 3:00 AM UTC.
It uses a simple weekly retention strategy, ensuring that only the most recent three weeks of weekday snapshots are kept.

Scheduler Configuration
------------------------

- **Schedule**: Snapshots are taken Monday through Friday at 03:00 AM (UTC).
- **Time Zone**: UTC (`Etc/UTC`)
- **Retention Rule**:
  - Keep all weekday snapshots from the last 3 weeks.
  - Snapshots older than 3 weeks are automatically deleted.

Snapshot Timeline (1 Year)
--------------------------

- Snapshots are created 5 times a week (Monday–Friday).
- With the 3-week retention rule, only the most recent 15 snapshots are kept at any time:

::

  3 weeks × 5 days/week = 15 retained snapshots

- Older snapshots are automatically removed on a rolling basis.

API Summary
-----------

**Endpoint**::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

  {
    "type": "snapshot",
    "name": "Weekday 3AM Snapshot Policy",
    "enable_backup_policy_notifications": true,
    "enable_retention_policy_notifications": false,
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
    "user_timezone": "Etc/UTC"
  }
