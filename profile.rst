=======
Profile
=======

Allowed HTTP methods
--------------------

+--------+---------------------------+
| Method | Description               |
+========+===========================+
| GET    | get the profile object    |
+--------+---------------------------+
| PUT    | update the profile object |
+--------+---------------------------+

.. note::
    
    See :rfc:`2616#section-9` for more details on HTTP methods semantics

.. _profile_get:

Listing
-------

.. http:get:: /profile/

Gets the user profile. Note that *profile* is a single object so the API does not return a list.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_profile
    :language: http


**Example response**:

.. literalinclude:: dumps/response_profile
    :language: javascript

Editing
-------

.. http:put:: /profile/

:statuscode 200: no error

Edits a user profile.
(We want to change the company name for example)

**Example request**:

.. literalinclude:: dumps/request_profile_update
    :language: http


**Example response**:

.. literalinclude:: dumps/response_profile_update
    :language: javascript

Schema
------

.. literalinclude:: dumps/response_profile_schema
    :language: javascript

