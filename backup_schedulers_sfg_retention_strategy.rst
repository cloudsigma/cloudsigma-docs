Son, Father, Grandfather (SFG) Retention Strategy
=================================================

Introduction
------------

The Son, Father, Grandfather (SFG) strategy is a standard industry approach to balance frequent backups with long-term storage efficiency:

- **Son (Daily):** Keeps the most recent snapshots from the last 7 days.
- **Father (Weekly):** Keeps the Monday snapshot from the previous 4 weeks.
- **Grandfather (Monthly):** Keeps the snapshot taken on the 23rd of each month for the last 12 months.

This layered structure ensures both short-term recovery and long-term archiving.

Scheduler Configuration
------------------------

- **Frequency:** Snapshots are taken daily at 01:00 AM GMT+12.
- **Retention Rules:**
  - 7 daily snapshots (Son)
  - 4 weekly snapshots (Father – every Monday)
  - 12 monthly snapshots (Grandfather – 23rd of each month)

Snapshot Timeline (1 Year)
---------------------------

After one year, you will retain:

- 7 daily snapshots
- 4 weekly snapshots (Mondays)
- 12 monthly snapshots (23rd of each month)

**Total retained snapshots after 1 year:**

::

  7 + 4 + 12 = 23 snapshots

All older snapshots are automatically deleted based on the rules.

API Summary
-----------

**Create the Snapshot Policy**

**Endpoint:**

::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

  {
    "type": "snapshot",
    "name": "Son, Father, GrandFather Policy",
    "enable_backup_policy_notifications": true,
    "enable_retention_policy_notifications": false,
    "is_enabled": true,
    "is_default": false,
    "manual_incremental_backup": "",
    "retention_policy": {
      "name": "Son, Father, GrandFather Policy",
      "rules": [
        { "period": "days", "quantity": 7 },
        { "period": "weeks", "quantity": 4, "time_option": 1 },
        { "period": "months", "quantity": 12, "time_option": 23 }
      ]
    },
    "initial_backup": {
      "day_of_week": ["*"],
      "start_time": { "hour": 12, "minute": 0 },
      "end_time": { "hour": 11, "minute": 45 }
    },
    "incremental_backup": {
      "day_of_month": "*",
      "day_of_week": ["*"],
      "month": "*",
      "hour": "1",
      "minute": "0",
      "repeat": { "hour": "", "minute": "" },
      "start_time": { "hour": 12, "minute": 0 },
      "end_time": { "hour": 11, "minute": 45 }
    },
    "user_timezone": "Etc/GMT+12"
  }
