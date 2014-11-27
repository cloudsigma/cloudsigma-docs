Billing
=======

.. _balance:

Balance
-------

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

.. http:get:: /balance/

    Get the balance and currency of the current account.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_balance_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_balance_list
        :language: javascript

Schema
~~~~~~

   .. literalinclude:: dumps/response_balance_schema
        :language: javascript


Pricing
-------

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

.. http:get:: /pricing/

    Gets the pricing information that are applicable to the cloud. Subscription prices use a burst level of 0.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_pricing_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_pricing_list
        :language: javascript


Burst levels
~~~~~~~~~~~~
    The current and future burst levels are provided in objects at the root of the response. The burst levels are calculated every 5 minutes based on the usage of the cloud and are applied 5 minutes later (when the next burst levels are calculated)

    .. includejson:: dumps/response_pricing_list
        :keys: current,next

Schema
~~~~~~

   .. literalinclude:: dumps/response_pricing_schema
        :language: javascript

Discounts
---------

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

.. http:get:: /discount/

   Get discount information.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_discount_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_discount_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_discount_schema
        :language: javascript




Transaction list
----------------

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

.. http:get:: /ledger/

   Get the transactions for the account.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_ledger_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_ledger_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_ledger_schema
        :language: javascript



Discounts
---------

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

.. http:get:: /discount/

   Get discount information.

    :statuscode 200: no error

    **Example request**:

    .. literalinclude:: dumps/request_discount_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_discount_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_discount_schema
        :language: javascript

.. _current-usage:

Current usage
-------------

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


.. _billing-license:

Licenses list
-------------

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

.. http:get:: /licenses/

   Get the licenses available on the cloud. The type of the license can be one of:

   :statuscode 200: no error

   * install - These licenses are billed per installation, regardless of whether it is attached to a running server or not.
   * instance - These licenses are billed per running instance of a server. A license attached to a guest that's stopped is not billed.
   * stub - These licenses are billed per a metric specified by the customer (i.e. per number of users license)

   The user metric field specifies what attribute on the instance of the server is used for determining the number of
   licenses. For example, "smp" will count one license for each CPU/core in the virtual machine.

    **Example request**:

    .. literalinclude:: dumps/request_licenses_list
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_licenses_list
        :language: javascript


Schema
~~~~~~

   .. literalinclude:: dumps/response_licenses_schema
        :language: javascript

