Tags
======

Allowed HTTP methods
--------------------

+--------+--------------------------+
| Method | Description              |
+========+==========================+
| GET    | get / list object/s      |
+--------+--------------------------+
| POST   | create new object/s      |
+--------+--------------------------+
| PUT    | update / modify object/s |
+--------+--------------------------+
| DELETE | delete object/s          |
+--------+--------------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
-------

.. http:get:: /tags/

Gets the list of tags to which the authenticated user has access.

:statuscode 200: no error


**Example request**:

.. literalinclude:: dumps/request_tags_list
    :language: http


**Example response**:


.. literalinclude:: dumps/response_tags_list
    :language: javascript


List single tag
-----------------

.. http:get:: /tag/(uuid:tag_uuid)/

Gets detailed information for tag identified by `tag_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_tags_get
    :language: http


**Example response**:


.. literalinclude:: dumps/response_tags_get
    :language: javascript

Creating
--------

.. http:post:: /tags/

Creates a new tag or multiple tags.

:statuscode 201: object created

**Example request**:

.. literalinclude:: dumps/request_tags_create
    :language: http


**Example response**:


.. literalinclude:: dumps/response_tags_create
    :language: javascript

It is possible to add resources to a tag at creation time. Just specify their UUIDs the `resources` list:

**Example request**:

.. literalinclude:: dumps/request_tags_create_with_resource
    :language: http


**Example response**:


.. literalinclude:: dumps/response_tags_create_with_resource
    :language: javascript


Editing
-------

.. http:put:: /tags/{uuid}/

Edits a tag. It is possible to add or remove resources to a tag by replacing the `resources` list with a new one:

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_tags_update_resources
    :language: http

**Example response**:

.. literalinclude:: dumps/response_tags_update_resources
    :language: javascript

It is also possible to edit the tags on the resource itself by replacing the `tags` list. For example here is how to
add a tag from a server:

**Example request**:

.. literalinclude:: dumps/request_tags_update_tag_from_resource
    :language: http

**Example response**:

.. literalinclude:: dumps/response_tags_update_tag_from_resource
    :language: javascript

Deleting
--------

.. http:delete:: /tags/{uuid}/

Deletes a single tag.

:statuscode 204: No content, object deletion started.

**Example request**:

.. literalinclude:: dumps/request_tags_delete
    :language: http

**Example response**:

.. literalinclude:: dumps/response_tags_delete
    :language: javascript




Filter Servers, Drives, IPs or VLANs listing by tag
----------------------------------------------------

.. http:get:: /tags/{uuid}/{resource_type}/

Lists the objects of the given *resource_type* which is one of 'servers', 'drives', 'ips', 'vlans'.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_tags_list_resource
    :language: http

**Example response**:

.. literalinclude:: dumps/response_tags_list_resource
    :language: javascript




