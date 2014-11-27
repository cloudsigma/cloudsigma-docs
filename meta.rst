Objects' metadata field
=======================

Objects, such as servers, drives, IPs, and VLANs have a ``meta`` field. This field can be used to store arbitrary
information in key-value form. There is no predefined structure for the ``meta`` attribute, only keys are limited to 32
characters, and values should be strings. The Web UI uses the ``meta`` to store drive and server descriptions.

Note that the whole meta is updated completely so all old key-value pairs should be present in new definition, when
updating ``meta``, unless they are to be deleted.


Server's metadata fields with special meaning
---------------------------------------------

- ``ssh_public_key`` is filled with the contents of the "SSH Key" field from the server's properties section
- ``cloudinit-user-data`` if available (and cloud-init 0.7.5 or newer is installed on the server) this field should
  contains valid cloud-init user data, that will be taken into account from the cloud-init
- ``base64_fields`` contains comma-separated meta keys in the metadata that are encoded in base64. This feature is useful
  when a meta field has more than one lines of text. cloud-init (0.7.5 or newer) for example will automatically
  decode from base64 the contents of ``cloudinit-user-data`` if the name of the meta key is in ``base64_fields``


Drive's metadata fields with special meaning
--------------------------------------------

When drive is cloned from the library we copy its Metadata to the new drive's meta as:

- ``os`` - drive's operating system (e.g. GNU/Linux, BSD, Windows...)
- ``arch`` - the architecture of the OS (e.g. 32-bit or 64-bit)
- ``distribution`` - for GNU/Linux and BSD operating systems (e.g. Debian, Fedora, FreeBSD...)
- ``version`` - distribution's version (if any)
- ``default_user`` - used in pre-installed images in order to specify the default user in the installed OS
- ``install notes`` - used if the image is not pre-installed
- ``url`` - URL to the official website of the OS
- ``description`` - description of what the drive contains
- ``image_type`` - type of the image on the drive (e.g. Live CD, Install CD, Pre-install)
- ``category`` - states what this image is most suitable for (e.g. dbserver, webserver, router, networking, ...)
- ``paid`` - this boolean field states if cloning the drive from the library is being charged
- ``favorite`` - this boolean field states if this drive is among the most popular library drives


These fields with special meaning could still be changed and deleted (even created if missing) just like every other
metadata field. Their content don't change server/drive's behavior nor any one of them is required.


Examples
--------

**Add meta to a drive:**

To add ``meta`` to the following drive:

.. literalinclude:: dumps/response_drive_get_unmounted
    :language: javascript

one has to use update call:

.. literalinclude:: dumps/request_drive_update_meta
    :language: http

Response is:

.. literalinclude:: dumps/response_drive_update_meta
    :language: javascript

**Update server meta, by removing one key and adding another:**

Suppose a server is updated to have the following definition:

.. literalinclude:: dumps/response_server_add_meta
    :language: javascript

In order to remove *meta_key1*, it is just skipped in the ``meta`` definition. Keeping *meta_key2* with its value is
achieved by redefining it, and new key *meta_key3* is added by defining it:

.. literalinclude:: dumps/request_server_edit_meta
    :language: http

The final result is:

.. literalinclude:: dumps/response_server_edit_meta
    :language: javascript
