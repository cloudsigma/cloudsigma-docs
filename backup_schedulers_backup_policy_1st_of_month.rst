1st of the Month Backup Policy
==============================

Introduction
------------

This backup policy is designed to take one remote snapshot per month, specifically on the 1st day of each month at 23:00 UTC.
It uses a monthly retention strategy, keeping one backup per month for the last 12 months.

Scheduler Configuration
------------------------

- **Frequency**: Monthly, on the 1st day of every month at 23:00 UTC

- **Retention Rule**:
  - Keep one backup per month for the last 12 months

Snapshot Timeline (1 Year)
---------------------------

After one year of operation:

- You will have 12 monthly backups (one for each of the past 12 months)
- Older backups (beyond 12 months) are automatically deleted

**Total snapshots retained after 1 year**: 12

API Summary
-----------

**Endpoint:**

::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

   {
     "type": "backup",
     "name": "1st of the month backup",
     "enable_backup_policy_notifications": true,
     "enable_retention_policy_notifications": false,
     "is_default": false,
     "is_enabled": true,
     "manual_incremental_backup": "",
     "retention_policy": {
       "name": "Keep 12 Month",
       "rules": [
         {
           "period": "months",
           "quantity": 12
         }
       ]
     },
     "incremental_backup": {
       "day_of_week": [],
       "day_of_month": "1",
       "month": "",
       "hour": "23",
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
         "hour": 6,
         "minute": 45
       }
     },
     "user_timezone": "Etc/UTC",
     "remote_location": "TBC"
   }
