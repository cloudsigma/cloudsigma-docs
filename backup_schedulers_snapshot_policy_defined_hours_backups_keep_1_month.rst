Snapshot Policy: Defined Hours Backups (Keep 1 Month)
=====================================================

Introduction
------------

This snapshot policy is configured for manual snapshot execution at defined times on Saturdays and Sundays only. Unlike recurring schedules, this setup uses the ``manual_incremental_backup`` field to specify the exact times when snapshots are taken.

**Manual Backup Times:**
Snapshots are created at 02:00, 06:00, 20:00, and 22:15 UTC.

**Active Days:**
Only on weekends (Saturday and Sunday).

**Retention Period:**
Snapshots are kept for 1 month before being automatically deleted.

Scheduler Configuration
------------------------

The ``start_time`` and ``end_time`` fields restrict when snapshots are allowed to occur. Manual snapshots will only run within this defined window.

Snapshot Retention (1-Year Estimate)
------------------------------------

- Snapshots occur 4 times per day, only on weekends.
- 2 weekend days per week = 8 snapshots per week.
- Over 1 month (approximately 4 weeks):
  → **4 snapshots × 2 days × 4 weeks = 32 snapshots retained at any time.**
- After one year, the number of retained snapshots remains **32**, as the retention policy only keeps the last month's snapshots.

API Summary
-----------

**Endpoint:**

::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

  {
    "type": "snapshot",
    "name": "Defined hours backups",
    "enable_backup_policy_notifications": true,
    "enable_retention_policy_notifications": false,
    "is_enabled": true,
    "is_default": false,
    "manual_incremental_backup": "02:00,06:00,20:00,22:15",
    "retention_policy": {
      "name": "Keep 1 Day",
      "rules": [
        {
          "period": "months",
          "quantity": 1
        }
      ]
    },
    "incremental_backup": {
      "day_of_month": "",
      "month": "",
      "hour": "",
      "minute": "",
      "day_of_week": ["sat", "sun"],
      "start_time": { "hour": 7, "minute": 0 },
      "end_time": { "hour": 6, "minute": 45 },
      "repeat": { "hour": "", "minute": "" }
    },
    "user_timezone": "Etc/UTC"
  }
