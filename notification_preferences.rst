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

