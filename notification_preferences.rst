Notification contacts
=====================

Listing
-------------

.. http:get:: /notification_contacts/

    Gets the list of contacts configured for the account.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_notification_contacts_list_1
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_notification_contacts_list_1
        :language: javascript



Creating
--------

.. http:post:: /notification_contacts/

    Creates a new contact.

    :statuscode 201: object created

    **Example request**:

    .. literalinclude:: dumps/request_notification_contacts_create
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_notification_contacts_create
        :language: javascript


Editing
-------

.. http:put:: /notification_contacts/{uuid}/

    Edits a notification contact. Note that changing the main user's email is not recommended, as if the account email changes, so will the main contact.

    :statuscode 200: no errors

    **Example request**:

    .. literalinclude:: dumps/request_notification_contacts_update
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_notification_contacts_update
        :language: javascript

Deleting
--------

.. http:delete:: /notification_contacts/{uuid}/

    Delete a notification contact. Note that you cannot delete the main contact.

    :statuscode 204: no errors

    **Example request**:

    .. literalinclude:: dumps/request_notification_contacts_delete
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_notification_contacts_delete
        :language: javascript




Notification preferences
========================

Listing
-------------

.. http:get:: /notification_preferences/

    Gets the list of contacts configured for the account.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_notification_preferences_list_1
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_notification_preferences_list_1
        :language: javascript


Updating
---------

.. http:put:: /notification_preferences/

    Updates the specified preferences. Only the ones in the request are modified.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_notification_preferences_update
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_notification_preferences_update
        :language: javascript


    Multiple objects can be specified in the request.

    **Example request**:

    .. literalinclude:: dumps/request_notification_preferences_update_multiple
        :language: http

    **Example response**:

    .. literalinclude:: dumps/response_notification_preferences_update_multiple
        :language: javascript

