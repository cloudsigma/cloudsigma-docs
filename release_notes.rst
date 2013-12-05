Release Notes
=============

Fluorine Release
-----------------

**Date Released:** 2013-11-18

* Global server context is a place to hold server context information, which is common to all user's servers.
  See :ref:`global-context`.

* A call for querying the account current usage :ref:`current-usage`.

* Clarifications regarding drive resize :ref:`drive-resize`.

* Section describing allowed names :ref:`permitted-characters`.

* Fixed documentation of response status codes :doc:`servers`, :doc:`snapshots`, :ref:`drive_cloning`.

* More flexible call for subscriptions auto-renew :ref:`subscriptions-autorenewing`.

* Login call returns a json object with the user UUID

* Guest firewall updates are applied every 30 seconds, as opposed to previous versions, when they were applied
  immediately on change.

* We now support bursting on IP resources. After the IP subscription has expired, all servers that have the IP attached
  as static will continue to operate until the user runs out of money. All other servers, will block outgoing traffic
  originating from that IP - i.e. the IP will stop working on servers on which the user configured it manually.

* Manually configuring an IP, given to the user via DHCP, to another server owned by the same user, is now prohibited.

* Buying a new IP resource, will make the same available on all of the user's servers without power-cycling them.
  The user can manually configure it on his public network interfaces and it will JUST work.

Oxygen Release
----------------

**Date Released:** 2013-10-07

*   Server context can be updated for a running server, by updating server or drive definition. See below.

*   It is possible to update ``name``, ``meta``, and ``tags`` on a running server or a drive mounted on a running
    server. See :ref:`server edit <server_edit>` and :ref:`drive edit <drive-edit>`.

*   Added an action to update a drive, which will fail to update if the drive is mounted on a running serve. It is
    called ``resize`` because size is the only drive attribute which cannot be changed on a drive mounted on a running
    guest. See :ref:`drive-resize`.

*   It is possible to create snapshots for a drive, and later clone the snapshot to a full drive. This makes it
    possible to restore from a point-in-time version of the snapshot. See :doc:`snapshots`.

*   Added documentation for uploading drive images though simple HTTP POST. See :doc:`upload_download`.


Nitrogen Release
-----------------

**Date Released:** 2013-08-01

*   Server context. Server context makes it possible to get configuration information about the server from within the
    virtual machine. :doc:`server_context`

*   It is possible to request the system to separate a drive physically from one or more other drives.
    See :ref:`drives-avoid`.

Carbon Release
---------------

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

*   NIC runtime information, when listing running guests, now is also added to the NIC definition, so that it is easier
    to access NIC runtime info from the NIC object itself rather than the server runtime. The old NIC runtime
    information in the server runtime is retained for backward compatibility.

*   Drives attached to stopped guests can now be deleted.


Boron Release
-------------

**Date Released:** 2013-03-19 

API HTTP response status code changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* HTTP status for PUT (update) requests is changed from 202 Accepted to 200 OK.
* HTTP status for creation of objects is changed from 202 Accepted to 201 Created. This affects Subscription, Servers, Drives, and Tags creation.
* HTTP status for Subscriptions Calcultaor is changed from 202 Accepted to 200 OK.
* HTTP status for actions with asynchronous results is changed from 200 to 202. This affects action calls on Servers (start, stop, clone, open_vnc, close_vnc) and Drives (clone).

Berilium Release
----------------

**Date Released:** 2013-01-16

