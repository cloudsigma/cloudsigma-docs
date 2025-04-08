Backup Scheduler: Every First of the Month at 23:59
====================================================

Overview
--------

This scheduler creates a local backup once a month, specifically on the 1st day of each month at 23:59 (London time).
The retention policy ensures that only the most recent six monthly backups are kept.

Scheduler Configuration
-----------------------

- **Frequency:** Monthly, on the 1st at 23:59
- **Time Window:** Not restricted (`start_time` and `end_time` are unset)
- **Retention Policy:** Keep the last 6 monthly backups
- **Backup Type:** Local backup
- **Day of Month:** 1
- **Hour:** 23
- **Minute:** 59
- **Timezone:** Europe/London

Snapshot Timeline (1 Year)
--------------------------

- **Backups per year:** 12 (1 per month)
- **Retention window:** 6 most recent backups
- **Total retained backups at any given time:** 6
- Older backups will be automatically deleted once a new backup surpasses the 6-month limit.

API Summary
-----------

**Endpoint:**

::

  POST /api/2.0/backupschedulers/

**JSON Payload**::

   {
     "incremental_backup": {
       "day_of_month": "1",
       "day_of_week": ["*"],
       "end_time": {
         "hour": "",
         "minute": ""
       },
       "hour": "23",
       "minute": "59",
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
     "name": "Every first of month at 23:59",
     "retention_policy": {
       "name": "Last 6 months",
       "rules": [
         {
           "period": "months",
           "quantity": 6
         }
       ]
     },
     "tags": [],
     "type": "backup",
     "user_timezone": "Europe/London"
   }
