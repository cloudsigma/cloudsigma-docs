Impersonation
===============================

Impersonation Management API

This API provides endpoints for managing user impersonation within the CloudSigma platform. It allows authorized users to enable/disable impersonation, manage groups of users allowed for impersonation, and view impersonation session history.

Resource: ``/api/2.0/impersonation/``

Authentication
--------------

All endpoints within this API require authentication using a valid CloudSigma API token.

Endpoints
---------

The `ImpersonationManagementResource` is located at: `/api/2.0/impersonation/`

Actions are performed via POST requests to this resource.
-----------------------

.. http:post:: /api/2.0/impersonation/?do=enable_impersonation

 Enables the ability for the currently authenticated user to be impersonated by others.

   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=enable_impersonation HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {}


    **Response**:
       .. parsed-literal::

          {"enabled": true}



.. http:post:: /api/2.0/impersonation/?do=disable_impersonation

Disables the ability for the currently authenticated user to be impersonated.
   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=disable_impersonation HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {}


    **Response**:
       .. parsed-literal::

          {"enabled": false}


.. http:post:: /api/2.0/impersonation/?do=enable_cs_staff_impersonation

Enables the ability for the currently authenticated user to be impersonated by CloudSigma staff user.
   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=enable_cs_staff_impersonation HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {}

    **Response**:
       .. parsed-literal::

          {"enabled": true}


.. http:post:: /api/2.0/impersonation/?do=disable_cs_staff_impersonation

Disables the ability for the currently authenticated user to be impersonated by CloudSigma staff users.
   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=disable_cs_staff_impersonation HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {}


    **Response**:
       .. parsed-literal::

          {"enabled": false}



.. http:post:: /api/2.0/impersonation/?do=enable_partner_staff_impersonation

Enables the ability for the currently authenticated user to be impersonated by CloudSigma Cloud Partner staff users.
   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=enable_partner_staff_impersonation HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {}


    **Response**:
       .. parsed-literal::

          {"enabled": true}



.. http:post:: /api/2.0/impersonation/?do=disable_partner_staff_impersonation

Disables the ability for the currently authenticated user to be impersonated by CloudSigma Cloud Partner staff users.
   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=disable_partner_staff_impersonation HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {}


    **Response**:
       .. parsed-literal::

          {"enabled": false}


.. http:post:: /api/2.0/impersonation/?do=add_user_to_personal_impersonation_group

Adds a user to the currently authenticated user's personal impersonation group, allowing the authenticated user to be impersonated by the that user.

   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=add_user_to_personal_impersonation_group HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

           {
               "uuid": "<target_user_uuid>",
               "label": "<optional_label_for_target_user>"
           }


    **Response**:
       .. parsed-literal::

          {}

.. http:post:: /api/2.0/impersonation/?do=remove_user_from_personal_impersonation_group

Removes a user to the currently authenticated user's personal impersonation group, preventing the authenticated user to be impersonated by the that user.

   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=remove_user_from_personal_impersonation_group HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

           {
               "uuid": "<target_user_uuid>"
           }


    **Response**:
       .. parsed-literal::

          {}


.. http:post:: /api/2.0/impersonation/?do=update_user_in_personal_impersonation_group

Update user label in currently authenticated user's personal impersonation group.

   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=update_user_in_personal_impersonation_group HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

         {
             "uuid": "<target_user_uuid>",
             "label": "<label>"
         }



    **Response**:
       .. parsed-literal::

          {}



.. http:post:: /api/2.0/impersonation/?do=list_groups

Lists the impersonation groups and their members for the currently authenticated user.
   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=list_groups HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

        {}


    **Response**:
       .. parsed-literal::

          {
               "cs_staff_group_enabled": true,
               "partner_staff_group_enabled": false,
               "personal_impersonation_group_members": [
                   {
                       "uuid": "<user_uuid>",
                       "label": "My Test User"
                   }
               ]
           }

.. http:post:: /api/2.0/impersonation/?do=list_last_impersonation_sessions

List last 10 impersonation sessions where authenticated user was impersonated.
   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=list_last_impersonation_sessions HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

        {}


    **Response**:
       .. parsed-literal::

           [
               {
                   "impersonator_uuid": "user_uuid",
                   "session_started_at": "2024-02-27 14:25:56.568465+00:00",
                   "session_ended_at": "2024-02-27 14:25:58.568465+00:00"
               }
           ]


.. http:post:: /api/2.0/impersonation/?do=list_allowed_to_impersonate

List of users that allow authenticated user to impersonate them.
   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=list_allowed_to_impersonate HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

        {}


    **Response**:
       .. parsed-literal::

           [
               {
                   "label": "My User to Impersonate",
                   "allower": "user@example.com"
               }
           ]





.. http:post:: /api/2.0/impersonation/?do=stop_impersonations

Stop all active impersonation sessions for authenticated user.

   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonation/?do=stop_impersonations HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

        {}



    **Response**:
       .. parsed-literal::

        {}

Impersonating and stop impersonating users
--------------

All endpoints within this API require authentication using a valid CloudSigma API token.

Authentication
--------------

All endpoints within this API require authentication using a valid CloudSigma API token.


Endpoints
---------
Resource: /api/2.0/impersonate/

.. http:post:: /api/2.0/impersonate/<user-uuid>/

Allow currently authenticated user to impersonate user with <user-uuid> if <user-uuid> has given all permissions.

   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonate/<user-id>/ HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

        {}



    **Response**:
       .. parsed-literal::

        {}


.. http:post:: /api/2.0/impersonate/stop/

Stop active impersonation session for currently authenticated user.

   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /api/2.0/impersonate/stop/ HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

        {}

    **Response**:
       .. parsed-literal::

        {}








