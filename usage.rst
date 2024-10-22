Usage
----------

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

.. http:get:: /usage/

    Retrieve the usage data for a specific time range. The start and end times are specified using the `poll_time_gt` (greater than) and `poll_time_lt` (less than) query parameters, along with an optional `limit` parameter to define the number of results returned.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_usage_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_usage_list
        :language: javascript

    **Example**:

    To retrieve user usage data for the entire day of **April 1st, 2024**, the query parameters would be set like this:

    .. code-block:: bash

        poll_time_gt=2024-04-01&poll_time_lt=2024-04-02&limit=1500

    This request will fetch all usage data between **2024-04-01 00:00:00** and **2024-04-02 00:00:00**. The `limit=1500` parameter restricts the response to 1500 records.