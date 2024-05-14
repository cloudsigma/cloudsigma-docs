ACLs (Access Control Lists)
===========================

Access Control Lists (ACLs) can be used to grant permissions to another user to manage your resources. For example it
is possible to permit another user to start or stop your servers or to allow another user to connect their servers
to your private network (VLAN).

Permissions can be granted on servers, drives, network resources, and firewall policies. All of these resources support
``LIST`` and ``EDIT`` permissions, which respectively allow the grantee to see the resources when listing them and to
edit resources. When a user is granted a ``LIST`` permission, this resource appears in the grantee's resource list. For
example, granting ``LIST`` on a drive will make it appear in the list with grantees' drives, when they make a GET request
to */drives*. Own resources can be differentiated from granted resources, by the ``owner`` field.

Some resources have additional permissions. Drives have ``ATTACH`` permission which allows another user to use the
drive on their server. IPs, VLANs, and Firewall policies have ``ATTACH`` which will allow another user to assign these
network resources to NICs on their server. Servers have ``START`` and ``STOP``, ``OPEN_VNC`` permissions which allow
another user to start or stop the server, or to open the server console through VNC. Note that ACLs may contain
permissions that are not directly applicable to some resources, for example, it is possible to have ``STOP``
permission in an ACL on tag which refers only to drives. Drives and servers support ``CLONE`` permission, which allows
cloning them to the grantee account. Note that to clone someone else's server, you need ``CLONE`` permission
on both the owner's server and on the attached non-cdrom drives. For cdrom drives, the user will need an ``ATTACH``
permission. The table below summarizes the permissions applicable to each resource:

=========================       ===========================================================
Resource                        Permissions
=========================       ===========================================================
Server                          ``LIST`` ``EDIT`` ``CLONE`` ``START`` ``STOP`` ``OPEN_VNC``
Drive                           ``LIST`` ``EDIT`` ``CLONE`` ``ATTACH``
IP, VLAN, Firewall Policy       ``LIST`` ``EDIT`` ``ATTACH``
=========================       ===========================================================


ACLs are granted on tags and apply to all the tagged resources. One ACL can be attached to multiple tags, and will
apply to the set of all resources tagged by these tags. It is also possible to have multiple ACLs on a tag, in which
case the permissions on the tagged resources are the combination of all ACLs rules.

Each ACL can have one or more grantee users. Each ACL object has a list of rules, that specify what permissions are
given by the ACL.

Permissions are not transferable to third parties, i.e. if you grant permission to someone, they can't grant it to a
third user. Only owners can grant permissions.


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

.. http:get:: /acls/

Gets the list of ACLs defined by the authenticated user.

:statuscode 200: no error


**Example request**:

.. literalinclude:: dumps/request_acls_list
    :language: http


**Example response**:


.. literalinclude:: dumps/response_acls_list
    :language: javascript

List Single ACL
---------------

.. http:get:: /acls/(uuid:acl_uuid)/

Gets detailed information for an ACL identified by `acl_uuid`.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_acls_get
    :language: http


**Example response**:


.. literalinclude:: dumps/response_acls_get
    :language: javascript

Creating
--------

.. http:post:: /acls/

Creates a new ACL.

:statuscode 201: object created

**Example request**:

.. literalinclude:: dumps/request_acls_create
    :language: http


**Example response**:


.. literalinclude:: dumps/response_acls_create
    :language: javascript

It is possible to define the grantees, tags, and rules at creation time. Just specify their UUIDs in the `grantees` list:

**Example request**:

.. literalinclude:: dumps/request_acls_create_with_grantees
    :language: http


**Example response**:


.. literalinclude:: dumps/response_acls_create_with_grantees
    :language: javascript



Editing
-------

.. http:put:: /acls/{uuid}/

Edits an ACL.

:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_acls_update
    :language: http

**Example response**:

.. literalinclude:: dumps/response_acls_update
    :language: javascript


Deleting
--------

.. http:delete:: /acls/{uuid}/

Deletes a single ACL.

:statuscode 204: No content, object deletion started.

**Example request**:

.. literalinclude:: dumps/request_acls_delete
    :language: http

**Example response**:

.. literalinclude:: dumps/response_acls_delete
    :language: javascript

Full Example of Sharing a Resource
----------------------------------

First, let's create a tag that will be shared with another user:

**Request**:

.. literalinclude:: dumps/request_tag_for_acls
    :language: http

**Response**:

.. literalinclude:: dumps/response_tag_for_acls
    :language: javascript

Let's create a drive tagged with the new tag:

**Request**:

.. literalinclude:: dumps/request_create_drive_for_acls
    :language: http

**Response**:

.. literalinclude:: dumps/response_create_drive_for_acls
    :language: javascript

It is also possible to tag an existing drive. Since there is no ACL on the tag, the ``grantees`` attribute
of the drive is empty.

Now let's add the tag to an ACL. Notice that we may add several tags to the ACL:

**Request**:

.. literalinclude:: dumps/request_acls_create_with_grantees
    :language: http

**Response**:

.. literalinclude:: dumps/response_acls_create_with_grantees
    :language: javascript

If we get the drive definition we will see the grantee in the ``grantees`` attribute:

.. literalinclude:: dumps/request_own_drive_grantees
    :language: http

.. literalinclude:: dumps/response_own_drive_grantees
    :language: javascript

Since there is an ACL on the tag all resources created with this tag will be shared. For example, if we create a
server with the same tag, we see that it also shows ``grantees``:

.. literalinclude:: dumps/request_server_with_acl
    :language: http

.. literalinclude:: dumps/response_server_with_acl
    :language: javascript

*The units for CPU, MEM, and SSD/DSSD are:*

CPU: GHz

MEM: Bytes

SSD / DSSD: Bytes

Permissions on Resources Attached to a Server
---------------------------------------------

When updating another user's server, the attached resources, such as drives, IPs, VLANs, or firewall policies, should
be available for the server owner. This means that either the attached resource should be owned by the server owner
or the owner should be given ``ATTACH`` permission on the attached resource. For example, if user A shares a
server with ``EDIT`` permission to user B, and user B wants to attach their drive to the server, user B will have to
grant ``ATTACH`` permission on the drive so that the owner of the server can start it. Trying to attach a
drive, on which there is no permission for the owner of the server will result in an error.

Recognizing Shared Resources and What Permissions Are Given on Them
-------------------------------------------------------------------

Finding out which resources were shared with you
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Resources shared with you appear in the resource list along with your resources. To differentiate between
owner, and shared with you resources you have to look at the ``owner`` field. If the user is the same as you, the
resource is yours. Non-owned resource have their respective owner uuid in the ``owner`` field. The examples in the
next two subsections show the same drive from the viewpoint of permission grantor and grantee. Notice how ``owner``
is the same.

Finding what permissions are granted to you on a resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While it is possible to follow the ACL-tag-resource graph to find out what are the resulting permissions on a
resource, it hard to do so in a simple script. That is why each resource has ``permissions`` field, which shows the
effective permissions the current user has on the resource. The ``permissions`` field is empty if the owner is the same
as the current user.

For example, if you get the definition of a drive shared by another user with you:

.. literalinclude:: dumps/request_foreign_drive_permissions
    :language: http

.. literalinclude:: dumps/response_foreign_drive_permissions
    :language: javascript

The definition includes non-empty ``permissions`` attribute:

.. includejson:: dumps/response_foreign_drive_permissions
    :keys: permissions
    :hide_header: true

In the next subsection, there is an example of the same drive but from the viewpoint of the drive owner.

Finding what permissions you have granted on a resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As is the case with finding out what permissions are given to the current user, it is also hard to find out, to find out
what is granted to other users, as users may be granted different permissions through several ACLs referring to
different tags. Therefore each resource has read-only field ``grantees``. Each object of the ``grantees`` list contains
references to the grantee user and a list of the permissions granted to them.

For example, if you get the definition of your drive shared with another user:

.. literalinclude:: dumps/request_own_drive_grantees
    :language: http

.. literalinclude:: dumps/response_own_drive_grantees
    :language: javascript

The definition includes non-empty ``grantees`` attribute:

.. includejson:: dumps/response_own_drive_grantees
    :keys: grantees
    :hide_header: true

In the previous subsection, there is an example of the same drive definition but from the viewpoint of the permissions
grantee.

Schema
------

.. literalinclude:: dumps/response_acls_schema
    :language: javascript
