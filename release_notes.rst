Release Notes
=============

Chlorine Release
----------------

Chlorine-17.2309
~~~~~~~~~~~~~~~~

**Date Released:** 2023-09-11

* We're adding lots of features under the hood that will be available in our WebUI soon.
* We're enabling support for zones in different data centers and the capability to create remote snapshots in multiple clusters as well.
* We're also making account inactivity settings configurable, which will make it to our shiny new WebApp anytime soon.
* And other bugs and improvements (13 to be precise).


Chlorine-17.2308
~~~~~~~~~~~~~~~~

**Date Released:** 2023-08-15

* We fixed an issue that prevented our system from sending automated monthly transactions and subscription reports. Your highly valuable report is back in action now!
* We've disabled the account country change per API call. If you need to change your country, please contact our support department.
* We've improved payment method creation logic, so your payment experience is better and our bank account - is happier!
* And many others, which are not-so-interesting.


Chlorine-17.2307
~~~~~~~~~~~~~~~~

**Date Released:** 2023-07-19

* We fixed a minor issue regarding drive resizing by the grantee when a drive is shared with them.
* We've fixed a rarely occurring issue related to our scheduler for migrations.
* Some of our clouds are receiving better stability when operating with GPUs in pass-through mode.
* We are making further improvements under the hood so that our next-gen UI can bring your beloved cloud experience.


Chlorine-17.2306
~~~~~~~~~~~~~~~~

**Date Released:** 2023-06-15

* This month's release mainly focuses on making our platform shinier behind the scenes. While nothing major to report, we have a few things to note.
* We've improved an out-of-memory notification event.
* We improved the invoice generation capabilities that were having a hiccup with some languages.
* We added support for our new soon-to-be-announced location under the hood.
* A number of other Bug Fixes & minor UI Improvements.


Chlorine-17.2305
~~~~~~~~~~~~~~~~

**Date Released:** 2023-05-10

* We are proud to announce that our cloud is growing with another new location, CWL - "Newport, Wales".
* We have tweaked the subject of our email notifications to be more informational by including the cloud location 3-letter code.
* We changed the API call to create drives, if no drive type is specified, we will take a default input as defined per cloud location.
* We did a lot of under-the-hood work, to make your cloud computing experience seamless.
* A number of other Bug Fixes & minor UI Improvements.


Chlorine-17.2304
~~~~~~~~~~~~~~~~

**Date Released:** 2023-04-11

* We enabled a new SSH Key type (ED25519) as an option for new VM creation and new SSH key creation.
* We are improving the SQL server experience. After a SQL Server subscription has expired, the resource will continue to operate on burst pricing, instead of stopping abruptly.
* A new notification type for SQL Server bursting is introduced.
* An issue regarding metadata was resolved (SSH keys remain in Metadata after deletion).
* A number of other Bug Fixes & minor UI Improvements.


Chlorine-17.2303
~~~~~~~~~~~~~~~~

**Date Released:** 2023-03-16

* A name adjustment for our UK, London location.
* A new notification is introduced, which will send a digest with all subscriptions and notifications on the first day of each month.
* A new storage type is introduced to our infrastructure - NVMe.
* A number of other Bug Fixes & minor UI Improvements.


Chlorine-17.2302
~~~~~~~~~~~~~~~~

**Date Released:** 2023-02-16

* Password Reset Link requests now expires after 24 hours.
* Fixed an issue related to notification text when an account has no saved credit card.
* Fixed an issue related to the error message "incorrect email", when a customer already activated a Guest session from the same IP.
* A number of other Bug Fixes & minor UI Improvements.


Silicon Release
---------------

**Date Released:** 2015-03-26

* Allow resources to be shared and accessed between accounts :doc:`Access Control Lists <acls>`

* Allow SSH keys to be imported and managed by the cloud and attached to servers :doc:`SSH key pairs <keypairs>`


Aluminium Release
-----------------

**Date Released:** 2014-11-26

* Extended :doc:`Capabilities <capabilities>` call

* Support of Zadara storage type :doc:`Drives <drives>`

* Better explained firewall restrictions depending on account state :doc:`Firewall Policies <fwpolicies>`

* Fixed list of API endpoints in :doc:`general` and :doc:`locations`

* We now support Solaris Kernel Zones in some cloud locations. Improved details and split sections depending
  on hypervisor - see :doc:`servers`, :doc:`servers_kvm` and :doc:`servers_solariskz`

* Support for serial console to a server -  see :doc:`servers`. Servers running under KVM hypervisor
  also allow VNC as before - :doc:`servers_kvm`.


Magnesium Release
-----------------

**Date Released:** 2014-09-08

* Various stability and performance improvements.

* Better explanation of :ref:`storage types <storage_type>` and explanation of default
  :ref:`network restrictions <firewall_restrictions>`.

* Support for Juju simple streams.

* Now it is possible to specify size for :ref:`drive clone <drive_cloning>` call, so that the new drive is bigger than
  the original.


Sodium Release
--------------

**Date Released:** 2014-05-20

* Documented the :doc:`Firewall Policies <fwpolicies>` delete request.

* Detailed documentation for the special :doc:`Metadata <meta>` fields.

* Better explanation for using :doc:`Server Context <server_context>`.

* Documented server ACPI shutdown API request - :ref:`ACPI Shutdown <acpi_shutdown>`.


Neon Release
------------

**Date Released:** 2014-01-29

* New drive parameter allowing changing the :ref:`storage type <storage_type>`.

* Most API calls now support standardised :ref:`filtering <filtering>`.

* Asnychronous operations now are exposed via a :doc:`jobs <jobs>` API.

* Cloning drives and servers can now :doc:`change <clone_naming>` the destinations' names to differentiate between
  source and destination.

* Added :doc:`audit log <audit_logs>` documentation.


Fluorine Release
----------------

**Date Released:** 2013-12-10

* Notification preferences functionality allowing multiple recipients. See :doc:`notification_preferences`.

* Server runtime details now report I/O statistics for the attached drives in the ``drives/runtime/io`` object from
  the response. See :ref:`server-runtime`.

* Capabilities call now includes the count allowed snapshots in the ``snapshots`` object from the response.
  See :doc:`capabilities`.

* API now returns all numbers as integer literals instead of string literals


**Date Released:** 2013-11-18

* Global server context is a place to hold server context information, which is common to all user's servers.
  See :ref:`global-context`.

* A call for querying the account current usage :ref:`current-usage`.

* Clarifications regarding drive resize :ref:`drive-resize`.

* Section describing allowed names :ref:`permitted-characters`.

* Fixed documentation of response status codes :doc:`servers`, :doc:`snapshots`, :ref:`drive_cloning`.

* More flexible call for subscriptions auto-renew :ref:`subscriptions-autorenewing`.

* Login call returns a json object with the user UUID

* Server firewall updates are applied every 30 seconds, as opposed to previous versions, when they were applied
  immediately on change.

* We now support bursting on IP resources. After the IP subscription has expired, all servers that have the IP attached
  as static will continue to operate until the user runs out of money. All other servers, will block outgoing traffic
  originating from that IP - i.e. the IP will stop working on servers on which the user configured it manually.

* Manually configuring an IP, given to the user via DHCP, to another server owned by the same user, is now prohibited.

* Buying a new IP resource, will make the same available on all of the user's servers without power-cycling them.
  The user can manually configure it on his public network interfaces and it will JUST work.

Oxygen Release
--------------

**Date Released:** 2013-10-07

*   Server context can be updated for a running server, by updating server or drive definition. See below.

*   It is possible to update ``name``, ``meta``, and ``tags`` on a running server or a drive mounted on a running
    server. See :ref:`server edit <server_edit>` and :ref:`drive edit <drive-edit>`.

*   Added an action to update a drive, which will fail to update if the drive is mounted on a running serve. It is
    called ``resize`` because size is the only drive attribute which cannot be changed on a drive mounted on a running
    server. See :ref:`drive-resize`.

*   It is possible to create snapshots for a drive, and later clone the snapshot to a full drive. This makes it
    possible to restore from a point-in-time version of the snapshot. See :doc:`snapshots`.

*   Added documentation for uploading drive images though simple HTTP POST. See :doc:`upload_download`.


Nitrogen Release
----------------

**Date Released:** 2013-08-01

*   Server context. Server context makes it possible to get configuration information about the server from within the
    virtual machine. :doc:`server_context`

*   It is possible to request the system to separate a drive physically from one or more other drives.
    See :ref:`drives-avoid`.

Carbon Release
--------------

**Date Released:** 2013-07-08

*   Recursive deletion of servers - ability to delete a server and its attached drives with a single API call.
    See :ref:`servers-delete-recursive`.

**Date Released:** 2013-05-22

*   Firewall functionality. The user can attach firewall policies to NICs. Each policy may have multiple rules for
    filtering traffic. See My Network -> policies in WebApp or check :doc:`fwpolicies` section for API documentation.

*   Web VNC. Users can open VNC sessions directly in WebApp. The browser needs to support websockets. To open a Web VNC
    session go to server properties on a running server, open VNC tunnel, click on the VNC button and choose whether to
    open the session in the same browser window or in a new browser window/tab.

*   The old ``hdd`` resource is renamed to ``dssd`` (Distributed SSD). This is reflected in all areas of the API.
    The subscriptions API still accepts ``hdd`` as an alias, but returns ``dssd``. The capabilities API
    returns ``dssd``.

*   OAuth support for single sign-on in WebApp. Users can authenticate in WebApp with an existing account from Google,
    Twitter, LinkedIn, or Facebook. See Profile -> settings to connect you CloudSigma account with an existing OAuth
    provider.

*   Drive images licenses. Servers running with drives from drives library, which contain software that requires a
    license need a subscriptions in order to be started. Check Subscriptions -> Purchase -> Software licenses in
    WebApp to list or purchase software licenses. See :doc:`subscriptions` for API docs on purchasing licenses,
    and :ref:`Licenses list <billing-license>` for listing purchased licenses.

*   NIC runtime information, when listing running servers, now is also added to the NIC definition, so that it is
    easier to access NIC runtime info from the NIC object itself rather than the server runtime. The old NIC runtime
    information in the server runtime is retained for backward compatibility.

*   Drives attached to stopped servers can now be deleted.


Boron Release
-------------

**Date Released:** 2013-03-19 

API HTTP response status code changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* HTTP status for PUT (update) requests is changed from 202 Accepted to 200 OK.
* HTTP status for creation of objects is changed from 202 Accepted to 201 Created. This affects Subscription, Servers,
  Drives, and Tags creation.
* HTTP status for Subscriptions Calcultaor is changed from 202 Accepted to 200 OK.
* HTTP status for actions with asynchronous results is changed from 200 to 202. This affects action calls on
  Servers (start, stop, clone, open_vnc, close_vnc) and Drives (clone).

Berilium Release
----------------

**Date Released:** 2013-01-16

