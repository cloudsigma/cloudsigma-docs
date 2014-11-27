Library Drives
==============

Allowed HTTP methods
--------------------

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
-------

.. http:get:: /libdrives/

Gets the list of library drives to which the authenticated user has access.

:param fields: A set of field names specifying the returned fields
:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_libdrive_list
    :language: http

**Example response**:

.. literalinclude:: dumps/response_libdrive_list
    :language: javascript


Detailed listing
----------------
.. note::
    For consistency, we left **/libdrives/detail/** url enabled, but it returns the same level of
    detail as the list call.



List single drive
-----------------

.. http:get:: /libdrives/{uuid}/

Gets detailed information for library drive identified by `uuid`.

:statuscode 200: no error


**Example request**:

.. literalinclude:: dumps/request_libdrive_get
    :language: http


**Example response**:

.. literalinclude:: dumps/response_libdrive_get
    :language: javascript

Attaching library drive
-----------------------
If the library drive is a CDROM media, you can attach it directly to an owned server the same way
you :ref:`attach a regular drive <attach_drive>` - specifying the library drive uuid.


Cloning library drive
---------------------
.. http:post:: /libdrives/{uuid}/action/?do=clone

    If a library drive is not a CDROM, you have to clone it in your account in order to use it. You can clone a library
    drive the same way you :ref:`clone a regular drive <drive_cloning>`.

.. _libdrives-licensed:

Licensed drive images
---------------------

Some drives in the library may require additional subscriptions or payment to be used.
This is visible from the ``licenses`` field in the drive definition. When you clone such image from drives library to your account,
the licenses remain bound to the cloned drive and can't be altered upon drive edit. See also :ref:`billing-license` regarding how to
list all defined licenses.


Recognizing library drives
--------------------------

Note that library drives can be queried through regular drives API using ``/drives/{uuid}/``. If the drive uuid happens
to be the uuid of a library drive, the drive defintion will be retrieved. In order to differentiate between owned and
library drive, one can check the ``owner`` attribute, which is ``null`` for library drives.

It is possible to get a library drive through the drives API, because there isn't a way to know in advance whether an
attached drive in a server definition is owned by the user or one from library.

Library drives are not listed in the list and detailed list for ordinary drives.


**Example:**

Get the drive from ``/drives/{uuid}/``:

.. literalinclude:: dumps/request_librdrive_get_through_drives
    :language: http

.. literalinclude:: dumps/response_librdrive_get_through_drives
    :language: javascript

Notice that there is no owner (it is ``null``).

Get the same drive from ``/libdrives/{uuid}/``:

.. literalinclude:: dumps/request_libdrive_get
    :language: http

.. literalinclude:: dumps/response_libdrive_get
    :language: javascript

Schema
------

.. literalinclude:: dumps/response_libdrive_schema
    :language: javascript
