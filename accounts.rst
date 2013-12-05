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

    Create an account on the system.

   :statuscode 200: no error
   :param email: The email of the account to be created


Login/Logout
------------


.. http:post:: /accounts/action/?do=login

   Login to the system using cookie auth

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

   Check if you are logged in the system

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

