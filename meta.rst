Objects' meta field
====================

Objects, such as servers, drives, IPs, and VLANs have a ``meta`` field. This field can be used to store arbitrary
information in key-value form. There is no predefined structure for the ``meta`` attribute, only keys are limited to 32
characters, and values should be strings. The Web UI uses the ``meta`` to store drive and server descriptions.

Note that the whole meta is updated completely so all old key-value pairs should be present in new definition, when
updating ``meta``, unless they are to be deleted.

Examples
--------

**Add meta to a drive:**

To add ``meta`` to the following drive:

.. literalinclude:: dumps/response_drive_get_unmounted
    :language: javascript

one has to use update call:

.. literalinclude:: dumps/request_drive_update_meta
    :language: javascript

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
    :language: javascript

The final result is:

.. literalinclude:: dumps/response_server_edit_meta
    :language: javascript
