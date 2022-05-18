Virtual Routers Firewall Policies
=================================


Allowed HTTP methods
--------------------

+--------+--------------------------+
| Method | Description              |
+========+==========================+
| GET    | get / list object/s      |
+--------+--------------------------+
| POST   | create new object/s      |
+--------+--------------------------+
| DELETE | delete object/s          |
+--------+--------------------------+


List single policy
------------------

.. http:get:: /vrfwpolicies/{vrfwpolicy_uuid}/

Gets detailed information on a policy identified by `vrfwpolicy_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/vrouters/request_vrfwpolicy_get
    :language: http


**Example response**:


.. literalinclude:: dumps/vrouters/response_vrfwpolicy_get
    :language: javascript


Creating
--------

.. http:post:: /vrfwpolicies/

    Creates a new virtual router firewall policy.

    :statuscode 201: object created

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwpolicy_create
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwpolicy_create
        :language: javascript

Editing
-------

.. http:put:: /vrfwpolicies/{uuid}/

    Edits a virtual router firewall policy. In case the policy is
    activated, all the filters are going to be applied. Also in case the policy
    is deactivated, all the filters are going to be removed from Firewall.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwpolicy_update
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwpolicy_update
        :language: javascript

Deleting
--------

.. http:delete:: /vrfwpolicies/{vrfwpolicy_uuid}/

    Deletes a single virtual router firewall policy.

    :statuscode 204: No content, object deletion started.

    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwpolicy_delete
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwpolicy_delete
        :language: javascript


Enable Policy
-----------------------

.. http:post:: /vrfwpolicies/{vrfwpolicy_uuid}/action/?do=enable

    Enables the Policy and all its filters.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwpolicy_enable
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwpolicy_enable
        :language: javascript


Disable Policy
------------------------

.. http:post:: /vrfwpolicies/{vrfwpolicy_uuid}/action/?do=disable

    Disables the Policy and all its filters.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/vrouters/request_vrfwpolicy_disable
        :language: http

    **Example response**:

    .. literalinclude:: dumps/vrouters/response_vrfwpolicy_disable
        :language: javascript


.. _vrfwpolicies_schema:

Schema
------

.. literalinclude:: dumps/vrouters/response_vrfwpolicy_schema
    :language: javascript
