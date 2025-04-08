Snapshot Policy: Every 12 Hours. Keep Last 2 Days
==================================================

Introduction
------------

This snapshot policy creates two daily snapshots, spaced 12 hours apart, and retains only the most recent 2 days of backups.

Scheduler Configuration
-----------------------

- **Type:** snapshot
- **Frequency:** Every 12 hours
- **Time window:** From 07:00 UTC to 06:45 UTC (next day) — ensures 24h coverage
- **Repeat rule:** */12  (every 12 hours)
- **User Timezone:** Etc/UTC

Retention Rules
---------------

- Keep snapshots from the last 2 days
- Automatically delete anything older

Snapshot Timeline (1 Year)
---------------------------

- **Snapshots per day:** 2 (1 every 12 hours)
- **Retention window:** 2 days
- **Total retained snapshots at any time:** 4

No matter how many are created over time, the system will only keep the most recent four snapshots (2 per day × 2 days).

**Total snapshots after 1 year:** Still four snapshots
*(Older ones are deleted automatically by the retention policy.)*

API Summary
-----------

**Endpoint:**

::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

  {
    "type": "snapshot",
    "name": "Every 12 hours. Last 2 days",
    "is_default": false,
    "is_enabled": true,
    "manual_incremental_backup": "",
    "retention_policy": {
      "name": "Keep 12 Month",
      "rules": [
        {
          "period": "days",
          "quantity": 2
        }
      ]
    },
    "incremental_backup": {
      "day_of_week": [],
      "day_of_month": "",
      "month": "",
      "hour": "",
      "minute": "",
      "repeat": {
        "hour": "*/12",
        "minute": ""
      },
      "start_time": {
        "hour": 7,
        "minute": 0
      },
      "end_time": {
        "hour": 6,
        "minute": 45
      }
    },
    "user_timezone": "Etc/UTC"
  }
