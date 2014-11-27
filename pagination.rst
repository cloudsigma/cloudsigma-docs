Pagination
==========

Options
-------

All the API requests that return lists of objects support pagination. This is done via two GET parameters:

* **offset** specifies the index at which to start returning objects. It is a zero based index.
* **limit** specifies the maximum number of objects to be returned. If set to 0, all resources will be returned.

    **Example request**:

    .. literalinclude:: dumps/request_server_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_server_list
        :language: javascript


Meta information
-----------------

The API returns an object with meta information about the request:

    .. includejson:: dumps/response_server_list
        :hide_header: true
        :keys: meta
