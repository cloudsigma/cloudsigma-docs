Current usage
=============

Allowed HTTP methods
~~~~~~~~~~~~~~~~~~~~

+--------+---------------------+
| Method | Description         |
+========+=====================+
| GET    | get / list object/s |
+--------+---------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
~~~~~~~

.. http:get:: /currentusage/

    Get the current usage of the user.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_currentusage_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_currentusage_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_currentusage_schema
        :language: javascript