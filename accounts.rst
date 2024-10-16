Accounts
========

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics

General
-------
The accounts API supports the following actions

Create account
--------------

.. http:post:: /accounts/action/?do=create

    Creates an account on the system. In case of success, the user has to check
    his email for a confirmation link, which will ask him to create a password
    for the account.

   :statuscode 200: no error
   :param email: The email of the account to be created
   :param promo: Promo code for initial subscriptions and demo server (optional)

   **Example request**:

   .. literalinclude:: dumps/request_account_create
       :language: http

   **Example response**:

   .. literalinclude:: dumps/response_account_create
       :language: javascript

Login/Logout
------------


.. http:post:: /accounts/action/?do=login

   Log in to the system using cookie auth

   :statuscode 200: no error
   :statuscode 401: unauthorized

   **Example request**:

    .. sourcecode:: http

      POST /accounts/action/?do=login HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {
          'username':'123@asd.com',
          'password':'parola'

          }


    **Response**:
        *Empty*


.. http:post:: /accounts/action/?do=logout

   Logout from the system when using cookie auth

   :statuscode 200: no error

   **Example request**:
    .. sourcecode:: http

          POST /accounts/action/?do=logout HTTP/1.1
          Host: api.cloudsigma.com
          Accept: application/json


    Request body

       .. parsed-literal::

          {}


    **Response**:
        *Empty*


.. http:post:: /accounts/action/?do=check_login

   Check if you are logged in to the system

   :statuscode 200: no error

   **Example request**:

    .. sourcecode:: http

      POST /accounts/action/?do=check_login HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {}


    **Response**:
        *Empty*

.. http:post:: accounts/action/?do=check_login_with_return_uuid

   Check how an authenticated service can get a user uuid via Cloudsigma API

   :statuscode 200: no error

   **Example request**:

    .. sourcecode:: http

      POST accounts/action/?do=check_login_with_return_uuid HTTP/1.1
      Host: api.cloudsigma.com
      Accept: application/json


    Request body

       .. parsed-literal::

          {
            curl --location --request POST 'https://tbc.cloudsigma.com/api/2.0/accounts/action/?do=check_login_with_return_uuid' \
            --header 'Cookie: csrftoken=zIiunVyYStnrRXxB1CmatfKsosHuaI6gYJw1P88r18pFCZ3YklNR7uEqEcQQOdze; sessionid=esqi1j0bpe2cto9ca59hw1k1kw7m95xd' \
            --header 'Referer: https://tbc.cloudsigma.com/ui/5.0/passs' \
            --header 'Content-Type: application/json' \
            --data-raw '{"username": "email", "password":"passwd"}'
          }


    **Response**:
        *Empty*

