Jobs
====
Jobs are used to track progress of long running tasks. A good example for a long running task is cloning of drives and
servers. Depending on the current cloud resource usage and the users preferences ( :ref:`drives-avoid` ), a drive clone
operation can take a while.

Currently, the operations that create a job for tracking are:
    * Drive cloning
    * Server cloning

Schema
------

   .. literalinclude:: dumps/response_jobs_schema
        :language: javascript

How it works
------------

* Drive cloning
After successfully starting a cloning operation via the API, you will receive the definition of the newly created
drive. All drives have a **jobs** field, containing references to the all the long running tasks executed on them.
The destination, since it is a newly created drive, references only 1 job - the currently running one. The source might
contain more jobs, depending on how many times it was cloned. **History of completed jobs is kept for 3 days**.
Older jobs are discarded.


* Server cloning
Cloning a server is a bit more complex. Since servers generally contain drives, drives must also be cloned. That is
why **jobs support sub-jobs**. When you send a clone server request, you receive the definition of the newly created
server. It also has a **jobs** field containing theD





