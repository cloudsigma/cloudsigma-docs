===========
Burst Usage
===========

Allowed HTTP methods
--------------------

+--------+--------------------------------------------------+
| Method | Description                                      |
+========+==================================================+
| GET    | get / list object/s                              |
+--------+--------------------------------------------------+

.. note::
    
    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
-------

.. http:get:: /burstusage/

    Get the burst usage of the authenticated user for the specified period (last 30 days by default).


    :statuscode 200: no error

   
    **Example request**:

    .. sourcecode:: http

      GET /api/2.0/burstusage/ HTTP/1.1
      Content-Type: application/json
      Authorization: Basic SWYgeW91IGZvdW5kIHRoaXMsIGhhdmUgYSBjb29raWUsIHlvdSBkZXNlcnZlIGl0IDop

    **Example response**:

    .. sourcecode:: javascript

        HTTP/1.0 200 OK
        Content-Type: application/json; charset=utf-8

        {
            "objects": [
                {
                     "uuid": "75fbf5d6-4ef6-11e4-9ce3-8bd2cacc5639",
                     "amount": 0.01000000000000000000,
                     "resource_type": "ip",
                     "usage": 1
                },
                {
                     "uuid": "f2669d85-2dbd-4f0d-8a1f-40a06deb3233",
                     "amount": 0.03010000000000000000,
                     "resource_type": "cpu",
                     "usage": 12000
                },
                {
                     "uuid": "1e170e6e-5339-477d-a29d-c3e6533a1825",
                     "amount": 0.02000000000000000000,
                     "resource_type": "mem",
                     "usage": 9663676416
                },
                {
                     "uuid": "42b2af55-ec3c-4066-a152-66d201c59576",
                     "amount": 0.01000000000000000000,
                     "resource_type": "dssd",
                     "usage": 107374182400
                },
            ]
        }


Filtering
---------

It's possible to specify period of burst usage using :ref:`filtering <filtering>` by date:

* Exact: `?date=2014-10-21`
* Lower than: `?date__lt=2014-10-21`
* Lower than or equal: `?date__lte=2014-10-21`
* Greater than: `?date__gt=2014-10-21`
* Greater than or equal: `?date__gte=2014-10-21`

    **Example for retreiving burst usage for the whole July 2014**:

    .. sourcecode:: http

      GET /api/2.0/burstusage/?date__gte=2014-07-01&date__lt=2014-08-01 HTTP/1.1
      Content-Type: application/json
      Authorization: Basic SWYgeW91IGZvdW5kIHRoaXMsIGhhdmUgYSBjb29raWUsIHlvdSBkZXNlcnZlIGl0IDop



=================
Daily Burst Usage
=================

Allowed HTTP methods
--------------------

+--------+--------------------------------------------------+
| Method | Description                                      |
+========+==================================================+
| GET    | get / list object/s                              |
+--------+--------------------------------------------------+

.. note::

    See :rfc:`2616#section-9` for more details on HTTP methods semantics


Listing
-------

.. http:get:: /dailyburstusage/

    Get the daily burst usage of the authenticated user for the specified period (last 30 days by default).


    :statuscode 200: no error


    **Example request**:

    .. sourcecode:: http

      GET /api/2.0/dailyburstusage/?date__gt=2014-11-15&date__lt=2014-11-19 HTTP/1.1
      Content-Type: application/json
      Authorization: Basic SWYgeW91IGZvdW5kIHRoaXMsIGhhdmUgYSBjb29raWUsIHlvdSBkZXNlcnZlIGl0IDop


    **Example response**:

    .. sourcecode:: javascript

        HTTP/1.0 200 OK
        Content-Type: application/json; charset=utf-8

        {
            "meta": {
                "limit": 20,
                "offset": 0,
                "total_count": 4
            },
            "objects": [
                {
                    "amount": "0.00886683986848225317",
                    "date": "2014-11-17",
                    "resource_type": "dssd",
                    "usage": 309237645312
                },
                {
                    "amount": "0.00886684598104320994",
                    "date": "2014-11-16",
                    "resource_type": "dssd",
                    "usage": 309237645312
                },
                {
                    "amount": "0.00514153897280246914",
                    "date": "2014-11-18",
                    "resource_type": "dssd",
                    "usage": 179314884608
                },
                {
                    "amount": "0.00886683701903935188",
                    "date": "2014-11-15",
                    "resource_type": "dssd",
                    "usage": 309237645312
                }
            ]
        }


Filtering
---------

It's possible to specify period of burst usage using :ref:`filtering <filtering>` by date:

* Lower than: `?date__lt=2014-10-21`
* Greater than: `?date__gt=2014-10-21`

    **Example for retreiving burst usage for the whole July 2014**:

    .. sourcecode:: http

      GET /api/2.0/dailyburstusage/?date__gt=2014-07-01&date__lt=2014-08-01 HTTP/1.1
      Content-Type: application/json
      Authorization: Basic SWYgeW91IGZvdW5kIHRoaXMsIGhhdmUgYSBjb29raWUsIHlvdSBkZXNlcnZlIGl0IDop


.. note::
    The date is actually a full time, which means that 2014-11-11 is actually 2014-11-11 00:00. This matters when trying
    to filter because when using less than, it will not include the day, whereas it will be included for greater then.
