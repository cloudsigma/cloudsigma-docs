Bi-monthly Backup Policy
========================

Introduction
------------

This policy creates a remote snapshot every two months and retains them for up to 6 months, ensuring a balance
between storage conservation and restore availability.

Scheduler Configuration
-----------------------

- **Snapshot Frequency**: Every two months on the 1st day at 17:00 UTC
- **Months**: February, April, June, August, October, December
- **Retention Rule**: Keep all snapshots for the last 6 months
- **Time Window**: The backup window runs daily from 07:00 to 19:00 UTC.
  This policy only uses it to scope execution.

Snapshot Timeline (1 Year)
--------------------------

Let’s break it down over one calendar year:

- Snapshots are taken on:
  - Feb 1, Apr 1, Jun 1, Aug 1, Oct 1, Dec 1

- At any given time, up to 3 most recent snapshots will be retained, due to the 6-month retention rule.
  - Example: In July, only Feb 1, Apr 1, and Jun 1 snapshots remain.

**Total retained snapshots after 1 year**:

::

  3 snapshots. Snapshots older than 6 months are automatically deleted.

API Summary
-----------

**Endpoint:**

::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

  {
    "type": "backup",
    "name": "BiMonthly Snapshot Policy",
    "is_default": false,
    "is_enabled": true,
    "manual_incremental_backup": "",
    "retention_policy": {
      "name": "Keep 12 Month",
      "rules": [
        {
          "period": "months",
          "quantity": 6
        }
      ]
    },
    "incremental_backup": {
      "day_of_week": [],
      "day_of_month": "1",
      "month": "2,4,6,8,10,12",
      "hour": "17",
      "minute": "0",
      "repeat": {
        "hour": "",
        "minute": ""
      },
      "start_time": {
        "hour": 7,
        "minute": 0
      },
      "end_time": {
        "hour": 19,
        "minute": 0
      }
    },
    "user_timezone": "Etc/UTC"
  }

