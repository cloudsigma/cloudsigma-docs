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

.. http:post:: /api/2.0/impersonation/?do=enable_impersonation

Enables the ability for the currently authenticated user

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

Disable Personal Impersonation
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


.. http:post:: /api/2.0/impersonation/?do=disable_impersonation

Disable Personal Impersonation
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

Enable CloudSigma Staff Impersonation Group. Any CloudSigma Staff user with approriate permissions given by CloudSigma can impersonate user`s account. 
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

Disable CloudSigma Staff Impersonation Group. Disables the ability for the currently authenticated user to be impersonated by CloudSigma staff users.
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

