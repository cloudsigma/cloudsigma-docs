Subscriptions
=============

Statuses
--------
    Every subscription has a status associated with it:

    .. _subscriptions-active:

    * ``active``: A subscription that is currently being used, either because the current time is between its start or end date or because it was the subscription for depletable resources (traffic) that is currently being used.

    .. _subscriptions-inactive:

    * ``inactive``: A subscription that is not currently being used, either because its not active yet or because there is another depletable resource (traffic) subscription being used.

    .. _subscriptions-expired:

    * ``expired``: A subscription that has either expired or that has been depleted.


Listing
-------

.. http:get:: /subscriptions/

Gets the list of subscriptions of the user.

:param status: filters only subscriptions in that status. Can be one of :ref:`active <subscriptions-active>` , :ref:`inactive <subscriptions-inactive>`, :ref:`expired <subscriptions-expired>`, ``all``, ``notexpired``. Default is ``all``.
:param resource: a list (comma separated) of resources. One or more of: ``dssd``, ``cpu``, ``mem``, ``tx``, ``ip``, ``vlan``.
:statuscode 200: no error

**Example request**:

.. literalinclude:: dumps/request_subscription_list
    :language: http


**Example response**:

.. literalinclude:: dumps/response_subscription_list
    :language: javascript





Subscription duration
---------------------

    There are three parameters that determine the subscription's duration. All times are in UTC. Not all combinations are valid:

    - ``start_time``: In `ISO 8601 <http://www.iso.org/iso/date_and_time_format>`_ format. Defaults to the current time.
    - ``end_time``: In `ISO 8601 <http://www.iso.org/iso/date_and_time_format>`_ format.
    - ``period``: Free form text describing the period. Ex: '2 months 1 week'.


==========  ========    =========   ======
   Inputs                           Result
---------------------------------   ------
start_time  end_time    period
==========  ========    =========   ======
True        True        True        Error: Ambiguous.
True        True        False       Between start_time and end_time.
True        False       True        Period from start_time.
True        False       False       Error: Not specific enough.
False       True        True        Period until end_time.
False       True        False       From now until end_time.
False       False       True        Period from now.
False       False       False       Error: Not specific enough.
==========  ========    =========   ======



Creating
--------

.. http:post:: /subscriptions/

    :statuscode 201: object created

    Creates a new subscription. There is a limit of 500 subscriptions that can be purchased in one request.

    The resource can be a :ref:`license <billing-license>` or one of: ``dssd`` (``hdd`` is an alias for this, but is being deprecated), ``cpu``, ``mem``, ``tx``, ``ip``, ``vlan``.

    When buying ``tx``, the time parameters are ignored.

    Trying to purchase a subscription for IP or VLAN with an amount bigger than one will generate several subscriptions of that type.

    Subscription times are rounded to noon UTC, using the following rules:

    * End time is always rounded to the next noon.
    * Start time is rounded to the maximum between the current time an the previous noon. This means that subscriptions bought for now do start now, but subscriptions for the future start at the previous noon.


        .. warning::
            Subscriptions are mostly immutable for the customer. The only parameter that can be changed is the auto renew.


**Example request**:

.. literalinclude:: request_subscription_create.json
    :language: javascript


**Example response**:

.. literalinclude:: response_subscription_create.json
    :language: javascript




Extending
---------

.. http:post:: /subscriptions/{id}/action/?do=extend

    :statuscode 200: no error

    Extends the subscription. An extended subscription is actually just another subscription that is linked to the original
    If a period or and end_time are specified in the request,they are used. If neither are specified, the creation length of the subscription is used.

    A caveat to this is that a subscription created initially with an end_time, the exact interval is used.
    Subscriptions that are created with a period have the period parsed again in the context of the new start_time.
    An example would be a subscription created on the 1st of February with a period of '1 month' will be extended for
    31 days, but one that was created with an end date of 1st of March will be extended for 28 days.

    If the specified subscription has actually been extended, it traverses and extends the last subscription in the chain.

.. _subscriptions-autorenewing:

Autorenewing
------------
.. http:post:: /subscriptions/{id}/action/?do=auto_renew

    Toggles the autorenew flag of the subscription. Optionally, the value can be specified in the request.

    :statuscode 200: no error

Schema
~~~~~~

   .. literalinclude:: dumps/response_subscription_schema
        :language: javascript


Grouped subscriptions
---------------------
.. http:get:: /groupedsubscriptions/

    Returns only the first subscriptions from a chain of extended subscriptions. The extensions are listed in the 'descendants' attribute and the end_time is that of the last subscription in the chain.

    :statuscode 200: no error

Calculator
----------

.. http:post:: /subscriptioncalculator/

    Returns the price of the subscriptions POSTed in the same format as the normal subscriptions.

    :statuscode 200: no error


    **Example request**:

    .. literalinclude:: dumps/request_subscriptioncalculator
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_subscriptioncalculator
        :language: javascript


    Similarly, the price of extending a subscription can be calculated.


    **Example request**:

    .. literalinclude:: dumps/request_subscriptioncalculator_extend
        :language: http


    **Example response**:

    .. literalinclude:: dumps/response_subscriptioncalculator_extend
        :language: javascript

